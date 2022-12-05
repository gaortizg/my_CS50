from emoji import emojize

def main():
    # Prompt user for input
    my_str = input("Input: ")

    # Translate string to emoji
    emoji = emojize(my_str, language = "alias")

    # Print 'emoji' version of string
    print(f"Output: {emoji}")

# Run 'main' function
if __name__ == "__main__":
    main()
