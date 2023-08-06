import pika
from queue import Queue
from threading import Thread
from pika.exchange_type import ExchangeType
import sys

from .utils import RABBITMQ_EXCHANGE


class Consumer:
    def __init__(self, rabbitmq_config: dict, msg_queue: Queue):
        self.msg_queue = msg_queue
        self.rabbitmq_config = rabbitmq_config
        self.conn = self.__get_connection()
        self.channel = self.conn.channel()

        self.channel.exchange_declare(
            RABBITMQ_EXCHANGE, ExchangeType.fanout, durable=True)

        self.channel.queue_declare(
            self.rabbitmq_config["queue"], durable=True)

        self.channel.queue_bind(
            self.rabbitmq_config["queue"], RABBITMQ_EXCHANGE)

    def __get_connection(self):
        try:
            creds = pika.PlainCredentials(
                self.rabbitmq_config["leaf"], self.rabbitmq_config["password"])

            conn = pika.BlockingConnection(pika.ConnectionParameters(
                host=self.rabbitmq_config["host"],
                port=self.rabbitmq_config["port"],
                credentials=creds,
                heartbeat=int(self.rabbitmq_config["heartbeat_time_s"]),
                connection_attempts=int(self.rabbitmq_config["conn_retries"]),
                retry_delay=int(self.rabbitmq_config["conn_retry_delay_s"])
            ))

        except Exception as e:
            sys.exit("Error while connecting to rabbitmq: " + str(e))

        else:
            return conn

    def __callback(self, ch, method, properties, body):
        msg = body.decode()
        print("Message received: " + msg)

        self.msg_queue.put(msg, block=False)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def start(self):
        self.channel.basic_consume(
            queue=self.rabbitmq_config["queue"], on_message_callback=self.__callback)
        try:
            print("[Consumer] Starting rabbitmq consumer")
            self.channel.start_consuming()

        except Exception as e:
            self.stop()

    def stop(self, err=None):
        print("[Consumer] Stopping rabbitmq consumer: " + str(err))
        self.channel.stop_consuming()
        self.conn.close()

    def spawn_consumer_thread(self):
        t = Thread(target=self.start, daemon=True)
        t.start()
