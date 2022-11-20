from cs50 import get_int

def main():
    # Prompt user for height and validate integer
    while True:
        n = get_int("Height: ")
        if (n > 0) and (n <= 8):
            break
    
    # Print result on screen
    for i in range(n):
        print((n - i - 1) * " ", end="")
        print((i + 1) * "#", end="")
        print(2*" ",end="")
        print((i + 1) * "#")

main()