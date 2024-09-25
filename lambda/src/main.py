def validate_document_number(document_number):
    if len(document_number) == 11:
        return True

    return False


def lambda_handler(event, context):
    print(event)

    headers = event.get("headers", {})
    document_number = headers.get("documentNumber")

    is_valid_document_number = validate_document_number(document_number)

    if not is_valid_document_number:
        return {
            "statusCode": 401,
            "headers": {"Content-Type": "*/*"},
        }

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "*/*"},
    }
