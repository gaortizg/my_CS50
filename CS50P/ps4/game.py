import random

def main():
    # Validate user's input
    while True:
        try:
            # Prompt user for input
            n = int(input("Level: "))

            # Validate entry
            if n <= 0:
                continue
            else:
                break

        # Handle incorrect input
        except ValueError:
            pass

    # Generate random number between 1 and 'n'
    my_rand = random.randint(1, n)

    # Prompt user for a guess
    while True:
        try:
            guess = int(input("Guess: "))
            # Validate entry
            if guess <= 0:
                continue
            else:
                if guess > my_rand:
                    print("Too large!")
                elif guess < my_rand:
                    print("Too small!")
                else:
                    print("Just right!")
                    break

        # Handle incorrect input
        except ValueError:
            pass

# Run 'main' function
if __name__ == "__main__":
    main()
