from validator_collection import validators, errors

def main():
    # Validate email address
    try:
        validators.email(input("What's your email address? "))
    except (errors.EmptyValueError, errors.InvalidEmailError):
        print("Invalid")
    else:
        print("Valid")


# Run 'main' function
if __name__ == "__main__":
    main()