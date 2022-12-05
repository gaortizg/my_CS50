def main():
    # Prompt user for input
    camel_case = input("camelCase: ")

    # Split string into characters
    letters = [x for x in camel_case]

    # Loop through each letter in list
    for i in range(len(letters)):
        # If letter is uppercase
        if letters[i].isupper():
            # Replace letter by '_' + lowercase
            letters[i] = "_" + letters[i].lower()

    # Join list of characters into a single string
    tmp = ""
    snake_case = tmp.join(letters)

    # Print result on screen
    print(f"snake_case: {snake_case}")   

# Run 'main' function
if __name__ == "__main__":
    main()
