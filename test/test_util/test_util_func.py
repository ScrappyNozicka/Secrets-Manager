from src.util.util_func import (
    write_secret,
    list_secrets,
    retrieve_secret,
    delete_secret,
    update_secret,
    randomise_secret,
    get_non_empty_input,
)
import boto3
from moto import mock_aws
import string
from unittest.mock import patch


@mock_aws
def test_write_secret():
    """Test the write_secret function returns expected result."""

    secretsmanager = boto3.client("secretsmanager", region_name="eu-west-2")

    test_identifier = "SteveBigSsecretVer01"
    test_user_id = "Steve2001"
    test_password = "IAmtheKingOfTheWorld2001"

    write_result = write_secret(
        test_identifier,
        test_user_id,
        test_password,
        secretsmanager_client=secretsmanager,
    )
    assert write_result["Name"] == "SteveBigSsecretVer01"
    assert write_result["ResponseMetadata"]["HTTPStatusCode"] == 200


@mock_aws
def test_list_secrets():
    """Test the list_secrets function returns expected list of secrets."""

    secretsmanager = boto3.client("secretsmanager", region_name="eu-west-2")

    test_identifier_01 = "SteveBigSsecretVer02"
    test_user_id_01 = "Steve2002"
    test_password_01 = "IAmtheKingOfTheWorld2002"

    test_identifier_02 = "SteveBigSsecretVer03"
    test_user_id_02 = "Steve2003"
    test_password_02 = "IAmtheKingOfTheWorld2003"

    write_secret(
        test_identifier_01,
        test_user_id_01,
        test_password_01,
        secretsmanager_client=secretsmanager,
    )
    write_secret(
        test_identifier_02,
        test_user_id_02,
        test_password_02,
        secretsmanager_client=secretsmanager,
    )

    result = list_secrets(secretsmanager_client=secretsmanager)

    assert len(result) == 2
    assert result == ["SteveBigSsecretVer02", "SteveBigSsecretVer03"]


@mock_aws
def test_retrieve_secret():
    """Test the retrieve_secret function returns expected file."""

    secretsmanager = boto3.client("secretsmanager", region_name="eu-west-2")

    test_identifier = "SteveBigSsecretVer04"
    test_user_id = "Steve2004"
    test_password = "IAmtheKingOfTheWorld2004"

    write_secret(
        test_identifier,
        test_user_id,
        test_password,
        secretsmanager_client=secretsmanager,
    )

    result = retrieve_secret(
        test_identifier, secretsmanager_client=secretsmanager
    )

    assert (
        result["SecretString"]
        == '{"username": "Steve2004", "password": "IAmtheKingOfTheWorld2004"}'
    )
    with open("secrets.txt", "r", encoding="UTF-8") as file:
        assert file
        assert file.read() == (
            '{"username": "Steve2004", '
            '"password": "IAmtheKingOfTheWorld2004"}'
        )


@mock_aws
def test_delete_secret():
    """Test the delete_secret function deletes expected file."""

    secretsmanager = boto3.client("secretsmanager", region_name="eu-west-2")

    test_identifier_01 = "SteveBigSsecretVer05"
    test_user_id_01 = "Steve2005"
    test_password_01 = "IAmtheKingOfTheWorld2005"

    test_identifier_02 = "SteveBigSsecretVer06"
    test_user_id_02 = "Steve2006"
    test_password_02 = "IAmtheKingOfTheWorld2006"

    test_identifier_03 = "SteveBigSsecretVer07"
    test_user_id_03 = "Steve2007"
    test_password_03 = "IAmtheKingOfTheWorld2007"

    write_secret(
        test_identifier_01,
        test_user_id_01,
        test_password_01,
        secretsmanager_client=secretsmanager,
    )
    write_secret(
        test_identifier_02,
        test_user_id_02,
        test_password_02,
        secretsmanager_client=secretsmanager,
    )
    write_result = write_secret(
        test_identifier_03,
        test_user_id_03,
        test_password_03,
        secretsmanager_client=secretsmanager,
    )

    assert write_result["Name"] == "SteveBigSsecretVer07"
    assert write_result["ResponseMetadata"]["HTTPStatusCode"] == 200

    result_all = list_secrets(secretsmanager_client=secretsmanager)

    assert len(result_all) == 3
    assert result_all == [
        "SteveBigSsecretVer05",
        "SteveBigSsecretVer06",
        "SteveBigSsecretVer07",
    ]

    delete_secret(test_identifier_03, secretsmanager_client=secretsmanager)

    result_deletion = list_secrets(secretsmanager_client=secretsmanager)

    assert len(result_deletion) == 2
    assert result_deletion == ["SteveBigSsecretVer05", "SteveBigSsecretVer06"]


@mock_aws
def test_update_secret():
    """Test the update_secret function update secret with expected values."""

    secretsmanager = boto3.client("secretsmanager", region_name="eu-west-2")

    test_identifier = "SteveBigSsecretVer08"
    test_user_id_01 = "Steve2008"
    test_password_01 = "IAmtheKingOfTheWorld2008"
    test_user_id_02 = "Steve2009"
    test_password_02 = "IAmtheKingOfTheWorld2009"

    write_result = write_secret(
        test_identifier,
        test_user_id_01,
        test_password_01,
        secretsmanager_client=secretsmanager,
    )
    assert write_result["Name"] == "SteveBigSsecretVer08"
    assert write_result["ResponseMetadata"]["HTTPStatusCode"] == 200

    result_01 = retrieve_secret(
        test_identifier, secretsmanager_client=secretsmanager
    )

    assert (
        result_01["SecretString"]
        == '{"username": "Steve2008", "password": "IAmtheKingOfTheWorld2008"}'
    )

    update_result = update_secret(
        test_identifier,
        test_user_id_02,
        test_password_02,
        secretsmanager_client=secretsmanager,
    )
    assert update_result["Name"] == "SteveBigSsecretVer08"
    assert update_result["ResponseMetadata"]["HTTPStatusCode"] == 200

    result_02 = retrieve_secret(
        test_identifier, secretsmanager_client=secretsmanager
    )

    assert (
        result_02["SecretString"]
        == '{"username": "Steve2009", "password": "IAmtheKingOfTheWorld2009"}'
    )


@mock_aws
def test_randomise_secret():
    """Test the randomise_secret function create randomised password."""

    secretsmanager = boto3.client("secretsmanager", region_name="eu-west-2")

    excluded_characters = r"\"#$%&'()*,:;<>?[\]^`{|}~"
    included_characters = string.ascii_letters + string.digits + r"-/_+=.@!"

    randomise_result = randomise_secret(secretsmanager_client=secretsmanager)

    assert randomise_result["RandomPassword"] is not None
    assert randomise_result["ResponseMetadata"]["HTTPStatusCode"] == 200
    assert len(randomise_result["RandomPassword"]) == 20
    for char in randomise_result["RandomPassword"]:
        assert char not in excluded_characters
        assert char in included_characters
        assert char != " "


def test_get_non_empty_input():
    """Test the get_non_empty_input function handles input as expected."""

    with patch("builtins.input", return_value="testing"):
        assert get_non_empty_input("") is not None
        assert get_non_empty_input("") == "testing"


def test_get_empty_input_and_non_empty_input(capsys):
    """Test the get_non_empty_input function handles no input as expected."""

    with patch("builtins.input", side_effect=["", "testing"]):
        result = get_non_empty_input("")
        assert result == "testing"
        captured = capsys.readouterr()
        assert "Input cannot be empty, please try again." in captured.out
