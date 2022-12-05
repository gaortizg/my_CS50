def main():
    # Initialize dictionary
    groceries = {}

    while True:
        try:
            # Prompt user for input. Make sure is uppercase
            item = input().upper()
            
            # Add 'item' to dictionary
            if item not in groceries:
                groceries[item] = 1
            else:
                groceries[item] += 1

        # If user presses 'ctrl + d' in keyboard, end routine
        except EOFError:
            print()
            break

    # Print dictionary in alphabetical order
    for key, value in sorted(groceries.items()):
        print(value, key)

# Run 'main' function
if __name__ == "__main__":
    main()
