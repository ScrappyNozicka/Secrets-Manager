from src.util.util_func import (
    write_secret,
    list_secrets,
    retrieve_secret,
    delete_secret,
    update_secret,
    randomise_secret
)
import re

def password_manager():
    response = str(input("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:"))
    while response.lower() not in "erdlxua":
        response = str(input("Invalid input. Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, [u]pdate, r[a]ndomise or e[x]it:"))
    
    if response.lower() == "x":
        print("Thank you. Goodbye.")
        return

    if response.lower() == "e":
        secret_identifier = str(input("Secret Identifier:"))
        user_id = str(input("UserID:"))
        password = str(input("Password:"))
        if re.match(r'^[a-zA-Z0-9\-/_+=\.@!]*$', secret_identifier):
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
        response = str(input("Specify secret to retrieve:"))
        try:
            retrieve_secret(response)
            print("Secrets stored in local file secrets.txt")
        except:
            print("That is not a valid secret.")
        password_manager()

    if response.lower() == "d":
        response = str(input("Specify secret to delete:"))
        if response in list_secrets():
            delete_secret(response)
            print("Deleted.")
        else:
            print("Secret not found, please try again.")
        password_manager()

    if response.lower() == "u":
        secret_identifier = str(input("Secret Id:"))
        user_id = str(input("New UserID:"))
        password = str(input("New Password:"))
        if secret_identifier in list_secrets():
            update_secret(secret_identifier, user_id, password)
            print("Secret updated.")
        else:
            print("Secret not found, please try again.")
        password_manager()

    if response.lower() == "a":
        secret_identifier = str(input("Secret Id:"))
        user_id = str(input("New UserID:"))
        password = randomise_secret()
        print("Random password generated:{password}")
        if re.match(r'^[a-zA-Z0-9\-/_+=\.@!]*$', secret_identifier):
            write_secret(secret_identifier, user_id, password)
            print("Secret saved.")
        else:
            print("Invalid name. Must be a valid name containing alphanumeric characters, or any of the following: -/_+=.@!")
        password_manager()

if __name__ == "__main__":
    password_manager()
