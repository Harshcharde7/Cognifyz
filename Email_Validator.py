import re

def is_valid_email(email):
    # Regular expression for a basic email validation
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    # Check if the email matches the pattern
    return bool(re.match(email_pattern, email))

# Example usage:
email_address = input("\n\t\tEnter an email address: ")

if is_valid_email(email_address):
    print(f"\t\t{email_address} is a valid email address.")
else:
    print(f"\t\t{email_address} is not a valid email address.\n")
