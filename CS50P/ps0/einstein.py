# Declare global variable
SPEED_LIGHT = 300000000 # [m/s]

def main():
    """
    Compute Enegy using Einstein's formula E = m * c**2
    """
    # Prompt user for mass in kilograms. Cast input to int
    m = int(input("Mass [kg]: "))

    # Compute energy in Joules
    E = m * SPEED_LIGHT**2

    # Print result on screen
    print(f"Energy [J]: {E} ")

# Run 'main' function
if __name__ == "__main__":
    main()
