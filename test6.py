import string

def check_password_strength(password: str) -> int:
    """Returns a score indicating the strength of the password.
    A higher score means the password is stronger.
    """
    score = 0

    # Check for the presence of various character classes
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    # Increase score based on character class checks
    score += has_upper + has_lower + has_digit + has_special

    # Check if the password length is strong
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    if len(password) >= 20:
        score += 1

    return score, has_upper, has_lower, has_digit, has_special

def check_password(password: str) -> None:
    """Checks the password for various issues and prints a message indicating its strength."""

    # Read the list of common passwords from the file
    with open("common.txt", "r") as f:
        common_passwords = set(f.read().splitlines())

    # Check if the password is too common
    if password in common_passwords:
        print("Password is too common. Your password strength is 0.")
        return

    # Check the password strength and character class details
    score, has_upper, has_lower, has_digit, has_special = check_password_strength(password)

    # Give feedback based on character class deficiencies
    missing_classes = []
    if not has_upper:
        missing_classes.append("uppercase letter")
    if not has_lower:
        missing_classes.append("lowercase letter")
    if not has_digit:
        missing_classes.append("digit")
    if not has_special:
        missing_classes.append("special character")

    if missing_classes:
        print(f"Password is missing: {', '.join(missing_classes)}")

    # Provide feedback on the strength score
    if score <= 2:
        print("Password is weak.")
    elif score == 3:
        print("Password is average.")
    elif score == 4:
        print("Password is strong.")
    elif score >= 5:
        print("Password is extremely strong.")

# Main loop to check passwords
while True:
    password = input("Enter password: ")
    check_password(password)
