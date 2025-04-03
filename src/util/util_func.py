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


def write_secret(
    secret_identifier, user_id, password, secretsmanager_client=client
):
    """
    Handler of creation and saving of new secret in Password Manager.

    Args:
        secret_identifier: User-defined secret identifier.
        user_id: User-defined user id.
        password: User-defined password.
        secretsmanager_client: Connection to AWS's Secret Manager.
    """

    secret_string = json.dumps({"username": user_id, "password": password})
    response = secretsmanager_client.create_secret(
        Name=secret_identifier, SecretString=secret_string
    )
    return response


def list_secrets(secretsmanager_client=client):
    """
    Handler of listing of all secrets stored in Password Manager.

    Args:
        secretsmanager_client: Connection to AWS's Secret Manager.
    """

    response = secretsmanager_client.list_secrets(SortOrder="asc")
    secret_names_list = []
    for secret in response["SecretList"]:
        secret_names_list.append(
            response["SecretList"][response["SecretList"].index(secret)][
                "Name"
            ]
        )

    return secret_names_list


def retrieve_secret(secret_identifier, secretsmanager_client=client):
    """
    Handler of location and extraction of secret from Password Manager locally.

    Args:
        secret_identifier: Pre-existing user-defined secret identifier.
        secretsmanager_client: Connection to AWS's Secret Manager.
    """

    response = secretsmanager_client.get_secret_value(
        SecretId=secret_identifier
    )
    with open("secrets.txt", "w", encoding="UTF-8") as file:
        file.write(str(response["SecretString"]))
    return response


def delete_secret(secret_identifier, secretsmanager_client=client):
    """
    Handler of deletion of pre-existing secret from Password Manager.

    Args:
        secret_identifier: Pre-existing user-defined secret identifier.
        secretsmanager_client: Connection to AWS's Secret Manager.
    """

    secretsmanager_client.delete_secret(
        SecretId=secret_identifier, ForceDeleteWithoutRecovery=True
    )


def update_secret(
    secret_identifier, user_id, password, secretsmanager_client=client
):
    """
    Handler of updating of pre-existing secret in Password Manager.

    Args:
        secret_identifier: Pre-existing user-defined secret identifier.
        user_id: New user-defined user id.
        password: New user-defined password.
        secretsmanager_client: Connection to AWS's Secret Manager.
    """

    secret_string = json.dumps({"username": user_id, "password": password})
    response = secretsmanager_client.update_secret(
        SecretId=secret_identifier, SecretString=secret_string
    )
    return response


def randomise_secret(secretsmanager_client=client):
    """
    Handler of creation of randomised password in Password Manager.

    Args:
        secretsmanager_client: Connection to AWS's Secret Manager.
    """

    response = secretsmanager_client.get_random_password(
        PasswordLength=20,
        ExcludeCharacters=r"\"#$%&'()*,:;<>?[\]^`{|}~",
        IncludeSpace=False,
    )
    return response


def get_non_empty_input(prompt):
    """
    Handler of empty input in main script of Password Manager.

    Args:
        promt: User input.
    """

    while True:
        user_input = input(prompt)
        if not user_input:
            print("Input cannot be empty, please try again.")
            continue
        return user_input
