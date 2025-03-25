from src.util.util_func import (
    write_secret,
    list_secrets,
    retrieve_secret,
    delete_secret,
)


def password_manager():
    print("""Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:
    """)
    response = str(input())
    if response.lower() not in "erdlx":
        print("Invalid input. Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:")
        response = str(input())

    if response.lower() == "x":
        print("Thank you. Goodbye.")

    if response.lower() == "e":
        secret_identifier = str(input("Secret Identifier:"))
        user_id = str(input("UserID:"))
        password = str(input("Password:"))
        try:
            write_secret(secret_identifier, user_id, password)
            print("Secret saved.")
        except:
            print("Invalid name. Must be a valid name containing alphanumeric characters, or any of the following: -/_+=.@!")
        initial_script()

    if response.lower() == "l":
        result = list_secrets()
        print(f"{len(result)} secrets available.\n{result}")
        initial_script()

    if response.lower() == "r":
        response = str(input("Specifiy secret to retrieve:"))
        try:
            retrieve_secret(response)
            print("Secrets stored in local file secrets.txt")
        except:
            print("That is not a valid secret.")
        initial_script()

    if response.lower() == "d":
        response = str(input("Specifiy secret to delete:"))
        if response in list_secrets():
            delete_secret(response)
            print("Deleted.")
        else:
            print("Secret not found, please try again.")
        initial_script()


if __name__ == "__main__":
    initial_script()
