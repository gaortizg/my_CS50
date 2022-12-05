import csv
import sys

def main():
    # validate command-line arguments
    check_argv = validate_sys_argv(sys.argv)

    if check_argv:
        # Retrieve filenames of CSV files
        before_csv = sys.argv[1]
        after_csv = sys.argv[2]
        
        # Create new CSV file with updated info
        arrange_csv(before_csv, after_csv)


def validate_sys_argv(my_argv):
    # Validate number of command-line arguments
    num_com = len(my_argv)
    if num_com < 3:
        sys.exit("Too few command-line arguments")
    elif num_com > 3:
        sys.exit("Too many command-line arguments")
    else:
        return True


def arrange_csv(before, after):
    # Initialize list
    students = []

    # Open file
    try:
        with open(before, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name": row["name"], "house": row["house"]})

    # If CSV file does not exist, inform user
    except FileNotFoundError:
        sys.exit(f"Could not read {before}")
    
    # Create new CSV file where updated names will be stored
    with open(after, "a") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()

        # Loop through each student
        for student in students:
            # Split name of students into first name and last name.
            # Remove any leading whitespaces
            student_name = student["name"].split(",")
            first = student_name[1].rstrip()
            last = student_name[0].rstrip()
            house = student["house"]
            
            # Write new info to new CSV file
            writer.writerow({"first": first, "last": last, "house": house})

# Run 'main' function
if __name__ == "__main__":
    main()