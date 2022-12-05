def main():
    while True:
        # Prompt user for input
        fraction = input("Fraction: ")    

        # Convert 'fraction' to percentage
        per = convert(fraction)

        # If 'per' is an integer, break out of while loop
        if isinstance(per, int):
            break

    # Now check the value of 'per' and print result accordingly
    print(gauge(per))


def convert(my_str):
    try:
        # Split fraction at '/'
        str_mod = my_str.split("/", maxsplit = 1)
        
        # Cast both elements of 'str_mod' to 'int'
        num = int(str_mod[0])
        den = int(str_mod[1])
        
        # Make sure 'num' <= 'den'
        assert num <= den

        # Compute result
        result = num / den
    
    # Catch errors at this point
    except (ValueError, ZeroDivisionError, AssertionError):
        pass

    else:
        # Return fraction as a percentage
        return int(100 * result)


def gauge(n):
    if n >= 99:
        return "F"
    elif n <= 1:
        return "E"
    else:
        return f"{n}%"


# Run 'main' function
if __name__ == "__main__":
    main()
