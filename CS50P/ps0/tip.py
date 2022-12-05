def main():
    """
    Compute amount to tip
    """
    # Prompt user for price of meal
    dollars = dollars_to_float(input("How much was the meal? "))

    # Prompt user for percentage to tip
    percent = percent_to_float(input("What percentage would you like to tip? "))
    
    # Compute tip
    tip = dollars * percent

    # Print result on screen
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # Remove leading $ symbol (if any)
    d = d.replace("$", "")

    # Cast string to float and return the value
    return float(d)

def percent_to_float(p):
    # Remove trailing % symbol (if any)
    p = p.replace("%", "")

    # Cast string to float, convert to decimal and
    # return the value
    return float(p) / 100

# Run 'main' function
if __name__ == "__main__":
    main()
