import re

def password_strength_checker(password):
    # Check the length of the password
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

    # Check for the presence of uppercase and lowercase letters
    if not any(c.isupper() for c in password) or not any(c.islower() for c in password):
        return "Weak: Password should contain both uppercase and lowercase letters."

    # Check for the presence of digits
    if not any(c.isdigit() for c in password):
        return "Weak: Password should contain at least one digit."

    # Check for the presence of special characters
    special_characters = re.compile(r'[^A-Za-z0-9]')
    if not special_characters.search(password):
        return "Weak: Password should contain at least one special character."

    # If all checks pass, consider the password strong
    return "Strong: Password meets all criteria."

if __name__ == "__main__":
    user_password = input("\nEnter your password: ")
    strength_result = password_strength_checker(user_password)
    print(strength_result)
