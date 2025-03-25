from src.util.util_func import (
    write_secret,
    list_secrets,
    retrieve_secret,
    delete_secret,
)
import boto3
from moto import mock_secretsmanager
import os
import pytest


@pytest.fixture(scope="function", autouse=True)
def aws_mock():
    with mock_secretsmanager():
        os.environ["AWS_ACCESS_KEY_ID"] = "testing"
        os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
        os.environ["AWS_SECURITY_TOKEN"] = "testing"
        os.environ["AWS_SESSION_TOKEN"] = "testing"
        os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"

        secretsmanager = boto3.client(
            "secretsmanager", region_name="eu-west-2"
        )
        yield secretsmanager


def test_write_secret(aws_mock):
    secretsmanager = aws_mock

    test_identifier = "SteveBigSsecretVer01"
    test_user_id = "Steve2000"
    test_password = "IAmtheKingOfTheWorld2000"

    # delete_secret(
    #     secret_identifier=test_identifier, secretsmanager_client=secretsmanager
    # )

    write_result = write_secret(
        test_identifier,
        test_user_id,
        test_password,
        aws_mock,
    )
    assert write_result["Name"] == "SteveBigSsecretVer01"
    assert write_result["ResponseMetadata"]["HTTPStatusCode"] == 200


# def test_list_secrets(aws_mock):
#     secretsmanager = aws_mock

#     test_identifier1 = "SteveBigSsecretVer02"
#     test_user_id1 = "Steve2001"
#     test_password1 = "IAmtheKingOfTheWorld2001"
#     test_identifier2 = "SteveBigSsecretVer03"
#     test_user_id2 = "Steve2002"
#     test_password2 = "IAmtheKingOfTheWorld2002"

#     write_secret(
#         test_identifier1,
#         test_user_id1,
#         test_password1,
#         secretsmanager_client=secretsmanager,
#     )
#     write_secret(
#         test_identifier2,
#         test_user_id2,
#         test_password2,
#         secretsmanager_client=secretsmanager,
#     )

#     result = list_secrets(secretsmanager_client=secretsmanager)

#     assert len(result) == 2
#     assert result == ["SteveBigSsecretVer02", "SteveBigSsecretVer03"]


# def test_retrieve_secret(aws_mock):
#     secretsmanager = aws_mock
    

#     test_identifier = "SteveBigSsecretVer07"

#     result = retrieve_secret(
#         test_identifier, secretsmanager_client=secretsmanager
#     )
#     assert (
#         result["SecretString"]
#         == '{"username": "Steve2000", "password": "IAmtheKingOfTheWorld2001"}'
#     )
#     with open("SteveBigSsecretVer07.txt", "r", encoding="UTF-8") as file:
#         assert file
#         assert (
#             file.read()
#             == """{
#             "username": "Steve2000",
#             "password": "IAmtheKingOfTheWorld2001"
#             }"""
#         )


# def test_delete_password(aws_mock):
#     secretsmanager = aws_mock

#     test_identifier = "SteveBigSsecretVer11"
#     test_user_id = "Steve2000"
#     test_password = "IAmtheKingOfTheWorld2001"

#     write_result = write_secret(
#         test_identifier,
#         test_user_id,
#         test_password,
#         secretsmanager_client=secretsmanager,
#     )
#     assert write_result["Name"] == "SteveBigSsecretVer11"
#     assert write_result["ResponseMetadata"]["HTTPStatusCode"] == 200

#     result = list_secrets(secretsmanager_client=secretsmanager)

#     assert len(result) == 5
#     assert result == [
#         "SteveBigSsecretVer08",
#         "SteveBigSsecretVer09",
#         "SteveBigSsecretVer07",
#         "SteveBigSsecretVer10",
#         "SteveBigSsecretVer100",
#     ]
