# Define global variable
COINS = [5, 10, 25]

def main():
    # Print info on screen
    print("Amount Due: 50")

    # Initialize variable
    total = 0

    # Keep asking for input until a certain condition is met
    while True:
        # Prompt user for input. Validate whether coin
        # is in list of accepeted coins by machine
        coin = get_coin(total)

        # Add value of coin to total
        total += coin
        
        # If total amount < 50, print info on screen
        if total < 50:
            print(f"Amount Due: {50 - total}")
        else:
            break

    # Check for total value and report change owed
    print(f"Change owed: {total - 50}")

def get_coin(total):
    # Keep prompting user for input until valid data is entered
    while True:
        try:
            coin = int(input("Insert coin: "))
            if coin in COINS:
                return coin
            else:
                print(f"Amount Due: {50 - total}")
        except ValueError:
            print(f"Amount Due: {50 - total}")

# Run 'main' function
if __name__ == "__main__":
    main()
