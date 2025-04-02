from unittest.mock import patch, call
from moto import mock_aws
from src.password_manager import password_manager

@mock_aws
@patch("builtins.input", side_effect=["e", "test-secret_123", "user_1", "password123", "x"])
@patch("builtins.print")
@patch("src.util.util_func.write_secret")
def test_password_manager_entry_valid_chars(mock_input, mock_print, mock_write_secret):

    password_manager()

    mock_write_secret.assert_any_call("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:")
    mock_write_secret.assert_any_call("Secret Identifier:")
    mock_write_secret.assert_any_call("UserID:")
    mock_write_secret.assert_any_call("Password:")

    mock_print.assert_any_call("Secret saved.")
    mock_print.assert_any_call("Thank you. Goodbye.")

@mock_aws
@patch("builtins.input", side_effect=["e", "<~~~~~~>", "x"])
@patch("builtins.print")
@patch("src.util.util_func.write_secret")
def test_password_manager_entry_invalid_chars(mock_input, mock_print, mock_write_secret):
    
    password_manager()

    mock_write_secret.assert_any_call("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:")
    mock_write_secret.assert_any_call("Secret Identifier:")

    mock_print.assert_any_call("Invalid name. Must be a valid name containing alphanumeric characters, or any of the following: -/_+=.@!")
    mock_print.assert_any_call("Thank you. Goodbye.")

@mock_aws
@patch("builtins.input", side_effect=["e", "test-secret_123", "user_1", "password123", "r", "test-secret_123", "x"])
@patch("builtins.print")
@patch("src.util.util_func.retrieve_secret")
def test_password_manager_retrieval_valid_input(mock_input, mock_print, mock_retrieve_secret):

    password_manager()

    mock_retrieve_secret.assert_any_call("Specify secret to retrieve:")

    mock_print.assert_any_call("Secrets stored in local file secrets.txt")
    mock_print.assert_any_call("Thank you. Goodbye.")

@mock_aws
@patch("builtins.input", side_effect=["r", "test-secret_123", "x"])
@patch("builtins.print")
@patch("src.util.util_func.retrieve_secret")
def test_password_manager_retrieval_invalid_input(mock_input, mock_print, mock_retrieve_secret):

    password_manager()

    mock_retrieve_secret.assert_any_call("Specify secret to retrieve:")

    mock_print.assert_any_call("That is not a valid secret.")
    mock_print.assert_any_call("Thank you. Goodbye.")





@mock_aws
@patch("builtins.input", side_effect=["e", "test-secret_123", "user_1", "password123", "d", "test-secret_123", "x"])
@patch("builtins.print")
@patch("src.util.util_func.delete_secret")
def test_password_manager_deletion_valid_input(mock_input, mock_print, mock_delete_secret):

    password_manager()

    mock_delete_secret.assert_any_call("Specify secret to delete:")

    mock_print.assert_any_call("Deleted.")
    mock_print.assert_any_call("Thank you. Goodbye.")


@mock_aws
@patch("builtins.input", side_effect=["d", "test-secret_123", "x"])
@patch("builtins.print")
@patch("src.util.util_func.delete_secret")
def test_password_manager_deletion_invalid_input(mock_input, mock_print, mock_delete_secret):

    password_manager()

    mock_delete_secret.assert_any_call("Specify secret to delete:")

    mock_print.assert_any_call("Secret not found, please try again.")
    mock_print.assert_any_call("Thank you. Goodbye.")


@mock_aws
@patch("builtins.input", side_effect=["l", "x"])
@patch("builtins.print")
@patch("src.util.util_func.list_secrets")
def test_password_manager_listing_none_secret(mock_input, mock_print, mock_list_secrets):

    password_manager()

    mock_print.assert_any_call("0 secrets available.\n[]")
    mock_print.assert_any_call("Thank you. Goodbye.")


@mock_aws
@patch("builtins.input", side_effect=["e", "test-secret_123", "user_1", "password123", "l", "x"])
@patch("builtins.print")
@patch("src.util.util_func.list_secrets")
def test_password_manager_listing_one_secret(mock_input, mock_print, mock_list_secrets):

    password_manager()

    mock_print.assert_any_call("1 secrets available.\n['test-secret_123']")
    mock_print.assert_any_call("Thank you. Goodbye.")


@mock_aws
@patch("builtins.input", side_effect=["e", "test-secret_123", "user_1", "password123", "e", "test-secret_456", "user_2", "password456", "e", "test-secret_789", "user_3", "password789", "l", "x"])
@patch("builtins.print")
@patch("src.util.util_func.list_secrets")
def test_password_manager_listing_multiple_secrets(mock_input, mock_print, mock_list_secrets):

    password_manager()

    mock_print.assert_any_call("3 secrets available.\n['test-secret_123', 'test-secret_456', 'test-secret_789']")
    mock_print.assert_any_call("Thank you. Goodbye.")



@mock_aws
@patch("builtins.input", side_effect=["x"])
@patch("builtins.print")
@patch("src.util.util_func.write_secret")
def test_password_manager_exit(mock_input, mock_print, mock_write_secret):

    password_manager()

    mock_print.assert_any_call("Thank you. Goodbye.")



@mock_aws
@patch("builtins.input", side_effect=["c", "x"])
@patch("builtins.print")
@patch("src.util.util_func.write_secret")
def test_password_manager_invalid_one_input(mock_input, mock_print, mock_write_secret):

    password_manager()

    mock_write_secret.assert_any_call("Invalid input. Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:")


@mock_aws
@patch("builtins.input", side_effect=["t", "s", "n", "x"])
@patch("builtins.print")
@patch("src.util.util_func.write_secret")
def test_password_manager_invalid_multi_input(mock_input, mock_print, mock_write_secret):

    password_manager()

    mock_write_secret.assert_has_calls(
        [
        call("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:"),
        call("Invalid input. Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:"),
        call("Invalid input. Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:"),
        call("Invalid input. Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:")
        ]
        )

    mock_print.assert_any_call("Thank you. Goodbye.")

@mock_aws
@patch("builtins.input", side_effect=["t", "e", "test-secret_123", "user_1", "password123",  "x"])
@patch("builtins.print")
@patch("src.util.util_func.write_secret")
def test_password_manager_invalid_input_and_valid_input_after(mock_input, mock_print, mock_write_secret):

    password_manager()

    mock_write_secret.assert_has_calls(
        [
        call("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:"),
        call("Invalid input. Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:"),
        call("Secret Identifier:"),
        call("UserID:"),
        call("Password:")
        ]
        )
    
    mock_print.assert_any_call("Secret saved.")
    mock_print.assert_any_call("Thank you. Goodbye.")

@mock_aws
@patch("builtins.input", side_effect=["e", "test-secret_123", "user_1", "password123", "t", "x"])
@patch("builtins.print")
@patch("src.util.util_func.write_secret")
def test_password_manager_valid_input_and_invalid_input_after(mock_input, mock_print, mock_write_secret):

    password_manager()

    mock_write_secret.assert_has_calls(
        [
        call("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:"),
        call("Secret Identifier:"),
        call("UserID:"),
        call("Password:"),
        call("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:"),
        call("Invalid input. Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:")
        ]
        )
    
    mock_print.assert_any_call("Secret saved.")
    mock_print.assert_any_call("Thank you. Goodbye.")


@mock_aws
@patch("builtins.input", side_effect=["e", "test-secret_123", "user_1", "password123", "u", "test-secret_123", "user_2", "password456", "x"])
@patch("builtins.print")
@patch("src.util.util_func.update_secret")
def test_password_manager_update_secret_valid_input(mock_input, mock_print, mock_update_secret):

    password_manager()

    mock_update_secret.assert_has_calls(
        [
        call("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:"),
        call("Secret Identifier:"),
        call("UserID:"),
        call("Password:"),
        call("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:"),
        call("Secret Identifier:"),
        call("New UserID:"),
        call("New Password:"),
        call("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:")
        ]
        )

    mock_print.assert_any_call("Secret saved.")
    mock_print.assert_any_call("Thank you. Goodbye.")

@mock_aws
@patch("builtins.input", side_effect=["u", "test-secret_123", "user_2", "password456", "x"])
@patch("builtins.print")
@patch("src.util.util_func.update_secret")
def test_password_manager_update_secret_invalid_input(mock_input, mock_print, mock_update_secret):

    password_manager()

    mock_update_secret.assert_has_calls(
        [
        call("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:"),
        call("Secret Identifier:")
        ]
        )

    mock_print.assert_any_call("Secret not found, please try again.")
    mock_print.assert_any_call("Thank you. Goodbye.")


@mock_aws
@patch("builtins.input", side_effect=["a", "test-secret_123", "user_1", "x"])
@patch("builtins.print")
@patch("src.util.util_func.randomise_secret")
def test_password_manager_randomise_password_valid_input(mock_input, mock_print, mock_randomise_secret):

    password_manager()

    mock_randomise_secret.assert_has_calls(
        [
        call("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:"),
        call("Secret Identifier:"),
        call("UserID:"),
        call("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:")
        ]
        )

    mock_print.assert_any_call("Random password generated:{password}")    
    mock_print.assert_any_call("Secret saved.")
    mock_print.assert_any_call("Thank you. Goodbye.")

@mock_aws
@patch("builtins.input", side_effect=["a", "<~~~~~~~~>", "x"])
@patch("builtins.print")
@patch("src.util.util_func.randomise_secret")
def test_password_manager_randomise_password_invalid_input(mock_input, mock_print, mock_randomise_secret):

    password_manager()

    mock_randomise_secret.assert_has_calls(
        [
        call("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:"),
        call("Secret Identifier:")
        ]
        )

    mock_print.assert_any_call("Invalid name. Must be a valid name containing alphanumeric characters, or any of the following: -/_+=.@!")
    mock_print.assert_any_call("Thank you. Goodbye.")   

# def test_password_manager_entry_none_chars(mock_input, mock_print, mock_write_secret):
