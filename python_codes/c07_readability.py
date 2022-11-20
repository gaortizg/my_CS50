from cs50 import get_string
import string

def main():
    # Prompt user for a string
    my_string = get_string("Text: ")

    # Initialize variable to count number of letters, and sentences
    n_letters = 0
    n_sentences = 0

    # Split sentence into words
    words = my_string.split()

    # Compute number of words
    n_words = len(words)

    # Loop through each word
    for word in words:
        # Loop through letters in each word
        for letter in word:
            # Check if we have a letter/number or a symbol
            if letter.isalnum():
                n_letters += 1
            elif letter in [".", "!", "?"]:
                n_sentences += 1

    # Use Coleman-Liau index formula to compute grade of the sentence
    L = (n_letters * 100) / n_words
    S = (n_sentences * 100) / n_words
    grade = round(0.0588 * L - 0.296 * S - 15.8)

    # Print result
    if grade < 1:
        print("Before Grade 1")
    elif grade >= 16:
        print("Grade: 16+")
    else:
        print(f"Grade: {grade}")

main()