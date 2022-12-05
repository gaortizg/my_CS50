def main():
    # Prompt user for input
    time = input("What time is it? ")

    # Convert time from string to float
    time_float = convert(time)

    # Check which time it is and print result on screen accordingly
    # If a.m.
    if time.endswith("a.m."):
        if (7 <= time_float) and (time_float <= 8):
            print("Breakfast time")

    # If p.m.
    else:
        if ((12 <= time_float) and (time_float < 13)) or (time_float == 1.0):
            print("Lunch time")
        elif (6 <= time_float) and (time_float <= 7):
            print("Dinner time")

def convert(time):
    """
    Converts time from a format string, to the corresponding
    number of hours as a float
    Ex:
    >>> convert("7:30 a.m.")
    >>> 7.5
    >>> convert("6:45 p.m.")
    >>> 6.75
    """
    # Remove suffix 'a.m.' or 'p.m.'
    if time.endswith("a.m."):
        time = time.removesuffix("a.m.")
    else:
        time = time.removesuffix("p.m.")

    # Split string at character ':'
    time = time.split(":")

    # Cast hours and minutes to float. Then add hours + (min / 60)
    time_float = float(time[0]) + float(time[1]) / 60

    # Return time as a float
    return time_float

# Run 'main' function
if __name__ == "__main__":
    main()
