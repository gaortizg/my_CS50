def main():
    # Prompt user for input
    my_str = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    # Make sure 'my_str' is lowercase
    my_str = my_str.lower()

    # Remove any whitespaces on the string
    my_str = my_str.replace(" ", "")

    # Check whether answer is 42 and print answer on screen
    if my_str in ["42", "fortytwo", "forty-two"]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
