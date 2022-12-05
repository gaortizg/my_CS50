import csv
import sys
from tabulate import tabulate

def main():
    # validate command-line arguments
    check_argv = validate_sys_argv(sys.argv)

    # Print table on screen using 'tabulate' package
    if check_argv:
        print_table(sys.argv[1])


def validate_sys_argv(my_argv):
    # Validate number of command-line arguments
    num_com = len(my_argv)
    if num_com < 2:
        sys.exit("Too few command-line arguments")
    elif num_com > 2:
        sys.exit("Too many command-line arguments")
    else:
        # Check file extension
        if not(my_argv[1].lower().endswith('.csv')):
            sys.exit("Not a CSV file")
    
    # If we reach this line, everything OK!
    return True


def print_table(path):
    # Initialize list
    pizzas = []

    # Open file
    try:
        with open(path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                pizzas.append(row)

    # If CSV file does not exist, inform user
    except FileNotFoundError:
        sys.exit("File does not exist")
    
    # If everything goes OK!
    else:
        print(tabulate(pizzas, headers="firstrow", tablefmt="grid"))

# Run 'main' function
if __name__ == "__main__":
    main()