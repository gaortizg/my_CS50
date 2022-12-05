import inflect

p = inflect.engine()

def main():
    # Initialize list
    names = []
    total = 0

    # Keep prompting user for names
    while True:
        try:
            # Append name to list
            names.append(input("Name: "))
            total += 1

        # If user presses 'ctrl+d' in keyboard, end loop
        except EOFError:
            print()
            break

    # Print names on screen
    print(f"Adieu, adieu, to {p.join(names, final_sep="")}")

# Run 'main' function
if __name__ == "__main__":
    main()
