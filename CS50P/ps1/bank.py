def main():
    # Prompt user for greeting
    greeting = input("Greeting: ")

    # Check greeting and print result accordingly
    total = value(greeting)
    print(total)

def value(greeting):
    # Remove leading and trailing whitespaces, and make
    # sure greeting is lowercase
    greeting = greeting.strip().lower()

    # If greeting starts with 'hello', print $0
    if greeting.startswith("hello"):
        return "$0"
    # If greet starts with 'h', but not hello, print $20
    elif greeting.startswith("h"):
        return "$20"
    # Otherwise, print $100
    else:
        return "$100"

# Run 'main' function
if __name__ == "__main__":
    main()
