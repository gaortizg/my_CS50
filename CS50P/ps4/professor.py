import random

def main():
    # Validate entry
    while True:
        try:
            # Prompt user for a level
            level = int(input("Level: "))
        # Handle error
        except ValueError:
            pass
        # Check a valid level has been entered
        else:
            if level in [1, 2, 3]:
                break
    
    # Initialize variable
    total_right = 0

    # Generate 10 random problems
    for i in range(10):
        # Initialize number of attempts
        tries = 0

        # Generate random numbers based on level chosen
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        else:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        
        # Compute result
        res_sum = x + y

        # Prompt user for result
        while True and tries < 3:
            # Validate users input
            try:
                res_user = int(input(f"{x} + {y} = "))
            # Handle error
            except ValueError:
                print("EEE")
                tries += 1
                if tries == 3:
                    print(f"{x} + {y} = {res_sum}")
                pass
            else:
                # Check user's result
                if res_user == res_sum:
                    total_right += 1
                    break
                else:
                    tries += 1
                    print("EEE")
                    if tries == 3:
                        print(f"{x} + {y} = {res_sum}")

    # Print total score
    print(f"Score: {total_right}")

# Run 'main' function
if __name__ == "__main__":
    main()
