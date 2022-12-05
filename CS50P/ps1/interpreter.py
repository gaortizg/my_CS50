def main():
    # Prompt user for input
    expression = input("Expression: ")

    # Split expression. Store each part of expression in
    # separate variables
    x, y, z = expression.split()

    # Cast numbers to float
    x = float(x)
    z = float(z)

    # Check value of second string in expression
    match y:
        case "+":
            print(x + z)
        case "-":
            print(x - z)
        case "*":
            print(x * z)
        case "/":
            print(f"{x / z:.1f}")

# Run 'main' function
if __name__ == "__main__":
    main()
