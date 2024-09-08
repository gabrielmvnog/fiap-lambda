import os
from base64 import b64decode
import boto3
import sqlalchemy


def lambda_handler(event, context) -> bool:
    document_number = event["documentNumber"]
    password = event["password"]

    if document_number == "documentNumber" and password == "password":
        return True

    return False


def database_connection():
    DB_HOST = os.environ["DB_HOST"]
    DB_USER = os.environ["DB_USER"]
    DB_TABLE = os.environ["DB_TABLE"]
    DB_PASS = os.environ["DB_PASS"]

    return sqlalchemy.create_engine(
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_TABLE}"
    )
