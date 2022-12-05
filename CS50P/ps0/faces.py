def main():
    # Prompt user for input
    my_str = input()

    # Feed my_str to function convert
    convert(my_str)

def convert(text):
    """
    Convert all occurrences of :) to 🙂, and
    all occurrences of :( to 🙁
    """
    # Replace all instances of :) and :(
    # by the respective emoticon
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    
    # Print modified string on screen
    print(f"{text}")

# Run 'main' function
if __name__ == "__main__":
    main()
