# Define global variable
VOWELS = "aeiouAEIOU"

def main():
    # Prompt user for input:
    my_str = input("Input: ")

    # Call function 'shorten'
    str_mod = shorten(my_str)

    # Print resulting string
    print(f"Output: {str_mod}")

def shorten(word):
    # Loop through each vowel
    for vowel in VOWELS:
        # Delete vowel from 'word'
        word = word.replace(vowel, "")
    
    # Return 'word' without vowels
    return word

# Run 'main' function
if __name__ == "__main__":
    main()
