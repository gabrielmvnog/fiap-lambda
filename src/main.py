import os
from base64 import b64decode
import boto3


def lambda_handler(event, context) -> bool:
    document_number = event["documentNumber"]
    password = event["password"]

    if document_number == "documentNumber" and password == "password":
        return True

    return False


def database_connection():
    DB_HOST = os.environ["DB_HOST"]
    DB_USER = os.environ["DB_USER"]

    DB_PASS_ENCRYPTED = os.environ["DB_PASS"]
    cipherTextBlob = b64decode(DB_PASS_ENCRYPTED)
    DB_PASS_DECRYPTED = boto3.client("kms").decrypt(CiphertextBlob=cipherTextBlob)[
        "Plaintext"
    ]

    print(DB_HOST, DB_USER, DB_PASS_DECRYPTED)
