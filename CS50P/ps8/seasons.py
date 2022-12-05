from datetime import date
import inflect
import sys

def main():
    # Prompt user for birthdate and check whether
    # date of birth is in valid format (YYYY-MM-DD)
    try:
        birth_date = date.fromisoformat(input("Date of Birth: "))
    # If inavlid date format, catch error
    except ValueError:
        sys.exit("Invalid date")
    # If everything OK!
    else:
        # The following line is neccesary so 'inflect' module can be used
        p = inflect.engine()

        # Convert days to minutes, and store result as words
        # remove unnecessary 'and'
        minutes = p.number_to_words(convert(birth_date)*24*60, andword = '')
        
        # Print result on screen
        print(f"{minutes.capitalize()} minutes")


def convert(d):
    # Get today's date
    today = date.today()
    # Return the difference between today and date 'd'
    # Only return number of days
    return (today - d).days


# Run 'main' function
if __name__ == "__main__":
    main()