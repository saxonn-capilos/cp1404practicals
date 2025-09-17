def main():
    password = get_password()
    while len(password) < 5:
        print("Password needs to be at least 5 characters long")
        password = get_password()
    print_password(password)


def print_password(password):
    print("*" * len(password))


def get_password():
    password = input("Enter your password: ")
    return password


main()

