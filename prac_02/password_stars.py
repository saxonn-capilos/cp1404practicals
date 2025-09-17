password = input("Enter your password: ")
while len(password) < 5:
    print("Password needs to be at least 5 characters long")
    password = input("Enter your password: ")
print("*" * len(password))
