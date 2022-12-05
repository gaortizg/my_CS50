import sys

def main():
    # validate command-line arguments
    check_argv = validate_sys_argv(sys.argv)

    # Count number of lines and print result on screen
    if check_argv:
        print(count_lines_file(sys.argv[1]))


def validate_sys_argv(my_argv):
    # Validate number of command-line arguments
    num_com = len(my_argv)
    if num_com < 2:
        sys.exit("Too few command-line arguments")
    elif num_com > 2:
        sys.exit("Too many command-line arguments")
    else:
        # Check file extension
        if not(my_argv[1].lower().endswith('.py')):
            sys.exit("Not a python file")
    
    # If we reach this line, everything OK!
    return True


def count_lines_file(path):
    # Initialize variable
    total_lines = 0

    # Open file
    try:
        with open(path, "r") as file:
            for line in file:
                line = line.strip()

                # Do not count comment lines or empty lines
                if line and not(line.startswith("#")):
                    total_lines += 1

    # If python file does not exist, inform user
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        return total_lines

# Run 'main' function
if __name__ == "__main__":
    main()