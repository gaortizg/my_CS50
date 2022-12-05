def main():
    # Prompt user for input
    time = input("What time is it? ")

    # Convert time from string to float
    time_float = convert(time)

    # Check which time it is and print result on screen accordingly
    if (7 <= time_float) and (time_float <= 8):
        print("Breakfast time")
    elif (12 <= time_float) and (time_float <= 13):
        print("Lunch time")
    elif (18 <= time_float) and (time_float <= 19):
        print("Dinner time")

def convert(time):
    """
    Converts time from a 24-hour format string, to the corresponding
    number of hours as a float
    Ex:
    >>> convert("7:30")
    >>> 7.5
    """
    # Split string at character ':'
    time = time.split(":")

    # Cast hours and minutes to float. Then add hours + (min / 60)
    time_float = float(time[0]) + float(time[1]) / 60

    # Return time as a float
    return time_float

# Run 'main' function
if __name__ == "__main__":
    main()
