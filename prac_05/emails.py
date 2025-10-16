"""
Emails
Estimate: 30 minutes
Actual: 1 hour, 8 minutes
"""

names_to_emails = {}


def main():
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        choice = input(f"Is your name {name}? [Y/n] ")
        if choice in "Yy" or choice == "":
            names_to_emails[f"{name}"] = email
        else:
            name = input("Name: ")
            names_to_emails[f"{name}"] = email
        email = input("Email: ")
    print('\n')
    for name, email in names_to_emails.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    email_parts = email.split('@')
    name_parts = str(email_parts[0])
    name_parts = name_parts.split('.')
    name_parts = [word.title() for word in name_parts]
    name = ' '.join(name_parts)
    return name


main()

