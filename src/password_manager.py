from src.util.util_func import (
    write_secret,
    list_secrets,
    retrieve_secret,
    delete_secret,
    update_secret,
    randomise_secret,
    get_non_empty_input
)
import re

def password_manager():    
    """
   Main script for Password Manager.
   Runs the terminal script using input from user.
  
   Requirements(.env):
       - AWS credentials
   """
       
    response = get_non_empty_input("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:")
    while response.lower() not in "erdlxua":
        response = get_non_empty_input("Invalid input. Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:")
    
    if response.lower() == "x":
        print("Thank you. Goodbye.")
        return

    if response.lower() == "e":
        secret_identifier = get_non_empty_input("Secret Identifier:")
        if re.match(r'^[a-zA-Z0-9\-/_+=\.@!]*$', secret_identifier):
            user_id = get_non_empty_input("UserID:")
            password = get_non_empty_input("Password:")
            write_secret(secret_identifier, user_id, password)
            print("Secret saved.")
        else:
            print("Invalid name. Must be a valid name containing alphanumeric characters, or any of the following: -/_+=.@!")
        password_manager()

    if response.lower() == "l":
        result = list_secrets()
        print(f"{len(result)} secrets available.\n{result}")
        password_manager()

    if response.lower() == "r":
        response = get_non_empty_input("Specify secret to retrieve:")
        try:
            retrieve_secret(response)
            print("Secrets stored in local file secrets.txt")
        except:
            print("That is not a valid secret.")
        password_manager()

    if response.lower() == "d":
        response = get_non_empty_input("Specify secret to delete:")
        if response in list_secrets():
            delete_secret(response)
            print("Deleted.")
        else:
            print("Secret not found, please try again.")
        password_manager()

    if response.lower() == "u":
        secret_identifier = get_non_empty_input("Secret Identifier:")
        if secret_identifier in list_secrets():
            user_id = get_non_empty_input("New UserID:")
            password = get_non_empty_input("New Password:")
            update_secret(secret_identifier, user_id, password)
            print("Secret updated.")
        else:
            print("Secret not found, please try again.")
        password_manager()

    if response.lower() == "a":
        secret_identifier = get_non_empty_input("Secret Identifier:")
        if re.match(r'^[a-zA-Z0-9\-/_+=\.@!]*$', secret_identifier):
            user_id = get_non_empty_input("UserID:")
            password = randomise_secret()
            print("Random password generated:{password}")
            write_secret(secret_identifier, user_id, password)
            print("Secret saved.")
        else:
            print("Invalid name. Must be a valid name containing alphanumeric characters, or any of the following: -/_+=.@!")
        password_manager()

if __name__ == "__main__":
    password_manager()
