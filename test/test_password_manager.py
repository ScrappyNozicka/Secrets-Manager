from unittest.mock import patch

from src.password_manager import password_manager

@patch("builtins.input", side_effect=["e", "test-secret_123", "user_1", "password123", "x"])
@patch("src.util.util_func.write_secret")
def test_password_manager_entry_valid_chars(mock_input, mock_write_secret):

    password_manager()

    mock_write_secret.assert_any_call('Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:')
    mock_write_secret.assert_any_call('Secret Identifier:')
    mock_write_secret.assert_any_call('UserID:')
    mock_write_secret.assert_any_call('Password:')

#@patch("builtins.print")
    # @patch("src.util.util_func.client.create_secret") 

    # mock_write_secret.return_value = {
    #     "Name": "test-secret_123",
    #     "ResponseMetadata": {"HTTPStatusCode": 200}
    # }
    # mock_create_secret.return_value = {
    #     "Name": "test-secret_123",
    #     "ResponseMetadata": {"HTTPStatusCode": 200}
    # }

    # mock_print.assert_any_call('Secret saved.')
    # mock_print.assert_any_call('Thank you. Goodbye.')





# @patch("builtins.input", side_effect=["e", "test_secret<~~~>", "user_1", "password123", "x"])
# @patch("src.util.util_func.write_secret")
# @patch("builtins.print")
# def test_password_manager_entry_invalid_chars(mock_input, mock_write_secret, mock_print):
#     mock_write_secret.return_value = None

#     password_manager()

#     mock_write_secret.assert_any_call('Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:')
#     mock_write_secret.assert_any_call('Secret Identifier:')
#     mock_write_secret.assert_any_call('UserID:')
#     mock_write_secret.assert_any_call('Password:')

#     mock_print.assert_any_call("Invalid name. Must be a valid name containing alphanumeric characters, or any of the following: -/_+=.@!")


# def test_password_manager_retrieval_valid_input(mock_input, mock_list_secret):
# def test_password_manager_retrieval_invalid_input(mock_input, mock_list_secret):
# def test_password_manager_deletion_valid_input(mock_input, mock_list_secret):
# def test_password_manager_deletion_invalid_input(mock_input, mock_list_secret):
# def test_password_manager_listing_none_secret(mock_input, mock_list_secret):
# def test_password_manager_listing_one_secret(mock_input, mock_list_secret):
# def test_password_manager_listing_multiple_secrets(mock_input, mock_list_secret):
# def test_password_manager_exit(mock_input, mock_list_secret):