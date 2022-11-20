from cs50 import get_int

def main():
    # Ask how any cents the customer is owed and validate entry
    while True:
        cents = get_int("Change owed: ")
        if (cents > 0) and (cents <= 99):
            break

    # Calculate number of quarters to give the customer
    quarters = cents // 25
    cents = cents - quarters * 25

    # Calculate number of dimes to give the customer
    dimes = cents // 10
    cents = cents - dimes * 10

    # Calculate number of nickels to give the customer
    # Coins left are considered pennies by default
    nickels = cents // 5
    pennies = cents - nickels * 5

    # Sum coins
    coins = quarters + dimes + nickels + pennies

    # Print total number of coins to give the customer
    print(f"{coins}")

main()