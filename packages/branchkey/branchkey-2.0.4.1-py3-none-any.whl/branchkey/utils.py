import jwt

AGGREGATED_OUTPUT_DIR = "./aggregated_output"


def parse_jwt(data: str):
    val = jwt.decode(data, algorithms='HS256', options={
                     "verify_signature": False})
    return val
