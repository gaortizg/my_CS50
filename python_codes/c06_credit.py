from cs50 import get_int

# TEST:
# AMEX: 378282246310005, 371449635398431, 378734493671000
# MASTERCARD:   5555555555554444, 5105105105105100, 5199999999999991
#               5299999999999990, 5105105105105100, 5560136761278244
#               5454545454545454, 5105105105105100
# VISA: 4003600000000014, 4111111111111111, 4012888888881881, 4222222222222
#       4999991111111113, 4999992222222229, 4111111111111111, 4012888888881881
#       4012000033330026

def main():
    # Prompt for Credit Card number
    card = get_int("Number: ")

    # Calculate checksum
    check = checksum(card)

    # If checksum is not valid, then print INVALID, otherwise, continue
    if check == False:
        print("INVALID")
    else:
        # validate card
        v = validate_card(card)

        # print result
        print(f"{v}")

def checksum(n):
    # Calculate checksum using Luhn's algorithm
    i = 1
    total = 0
    while True:
        # Fetch last digit of card
        tmp = n % 10

        # Check digit to see whether we need to multiply by two or not
        if (i % 2) == 0:
            total += ((2*tmp) // 10) + ((2*tmp) % 10)
        else:
            total += tmp

        # Remove last digit
        n = n // 10
        i += 1

        # Check whether we break from while loop or not
        if n <= 0:
            break

    # Validate checksum
    if (total % 10) == 0:
        return True
    else:
        return False

def validate_card(n):
    # Convert card number to string
    card = str(n)

    # Compute card length and first digits of the card
    l = len(card)
    if l == 13:
        if int(card[0]) == 4:
            result = "VISA"
    elif l == 15:
        if int(card[0:2]) in [34, 37]:
            result = "AMEX"
    elif l == 16:
        if int(card[0]) == 4:
            result = "VISA"
        elif int(card[0:2]) in range(51, 56):
            result = "MASTERCARD"
    else:
        result = "INVALID"

    return result

# Run main function
main()
