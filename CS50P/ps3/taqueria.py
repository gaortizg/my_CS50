def main():
    # Create dictionary
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # Initialize variable
    total = 0

    while True:
        try:
            # Prompt user for input
            item = input("Item: ")
            
            # If 'item' is in 'menu', add price to 'total'
            if item.title() in menu:
                total += menu[item.title()]

                # Print result on screen
                print(f"Total: ${total:.2f}")

        # If user presses 'ctrl + d' in keyboard, end routine
        except EOFError:
            print()
            break

# Run 'main' function
if __name__ == "__main__":
    main()
