from pyfiglet import Figlet
from random import choice
import sys

def main():
    # this line is to be able to use 'Figlet' module
    figlet = Figlet()

    # Compute number of command-line arguments
    len_sys = len(sys.argv)

    # Get available fonts from 'figlet' module
    # If no command-line arguments are provided
    if len_sys == 1:
        # Choose random font from list
        my_font = choice(figlet.getFonts())

    # In case of command-line arguments
    elif not (len_sys == 3):
        # Too few/many arguments
        sys.exit("Invalid usage")
    else:
        # Check first command line argument
        if sys.argv[1] not in ['-f', '--font']:
            sys.exit("Invalid usage")
        
        # Check whether font is valid or not
        my_font = sys.argv[2]
        if my_font not in figlet.getFonts():
            sys.exit("Invalid usage")

    # Prompt user for input
    my_str = input("Input: ")

    # Set font to be used with 'figlet' module
    figlet.setFont(font=my_font)

    # Print result on screen
    print(figlet.renderText(my_str))

# Run 'main' function
if __name__ == "__main__":
    main()
