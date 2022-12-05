def main():
    # Prompt user for input
    plate = input("Plate: ")

    # Check whether plate number is valid or not
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check whether length of plate is valid or not
    if (len(s) < 2) or (len(s) > 6):
        return False
    
    # Check whether plate has punctutaction symbols or not
    elif not(s.isalnum()):
        return False

    # Check whether plate starts with letters or numbers
    elif not(s[0:2].isalpha()):
        return False

    # If there are digits on the plate, validate the number
    else:
        # Count number of digits in plate
        count_digit = sum(c.isdigit() for c in s)

        # If digits on the plate
        if count_digit > 0:
            # Numbers must come at the end
            if not(s[-count_digit:].isdigit()):
                return False
            # Numeric part of the plate must not start with zero
            elif int(s[-count_digit]) == 0:
                return False

    # This line is reached only if a valid plate number was entered
    return True

# Run 'main' function
if __name__ == "__main__":
    main()
