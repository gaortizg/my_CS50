def main():
    # Create list with months
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"  
    ]

    while True:
        try:
            # Prompt user for date in month-day-year format
            date = input("Date: ").strip()

            # Replace any instance of '/' or ',' with a whitespace
            date = date.replace("/", " ").replace(",", " ")

            # Split 'date' into ['month', 'day', 'year']
            month, day, year = date.split()

            # Cast 'day' and 'year' to integers
            day = int(day)
            year = int(year)

        # If 'day' or 'year' are not integers
        except ValueError:       
            pass

        else:
            # Validate month
            if month.isalpha():
                if month not in months:
                    continue
            else:
                if int(month) > 12:
                    continue
            
            # Validate day
            if day > 31:
                continue
            else:
                break

    # Format 'month'. Print date accordingly
    if month.isalpha():
        month_for = months.index(month.capitalize()) + 1
        print(f"{year}-{month_for:02}-{day:02}")
    else:
        month_for = int(month)
        print(f"{year}-{month_for:02}-{day:02}")

# Run 'main' function
if __name__ == "__main__":
    main()
