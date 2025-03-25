import boto3
import json
import os

AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]

client = boto3.client(
    "secretsmanager",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name="eu-west-2",
)

# def test_environment_variables():
#     print("AWS_ACCESS_KEY_ID:", os.getenv("AWS_ACCESS_KEY_ID"))
#     assert os.environ.get("AWS_ACCESS_KEY_ID") == "fake_access_key"
#     assert os.environ.get("AWS_SECRET_ACCESS_KEY") == "fake_secret_key"


def write_secret(
    secret_identifier, user_id, password, secretsmanager_client=client
):
    secret_string = json.dumps({"username": user_id, "password": password})
    response = client.create_secret(
        Name=secret_identifier, SecretString=secret_string
    )
    return response


def list_secrets(secretsmanager_client=client):
    response = client.list_secrets(SortOrder="asc")
    secret_names_list = []
    for secret in response["SecretList"]:
        secret_names_list.append(
            response["SecretList"][response["SecretList"].index(secret)][
                "Name"
            ]
        )

    return secret_names_list


def retrieve_secret(secret_identifier, secretsmanager_client=client):
    response = client.get_secret_value(SecretId=secret_identifier)
    with open("secrets.txt", "w", encoding="UTF-8") as file:
        file.write(str(response["SecretString"]))
    return response


def delete_secret(secret_identifier, secretsmanager_client=client):
    client.delete_secret(
        SecretId=secret_identifier, ForceDeleteWithoutRecovery=True
    )
