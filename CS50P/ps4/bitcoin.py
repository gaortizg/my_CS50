import json
import requests
import sys

def main():
    # Check command-line arguments
    if not(len(sys.argv) == 2):
        sys.exit("Missing command-line argument")
    else:
        while True:
            # Validate command-line argument
            try:
                n = float(sys.argv[1])
                if n <= 0:
                    sys.exit("Command-line argument has to be a positive non-zero number")
                else:
                    break
            except ValueError:
                sys.exit("Command-line argument is not a number")

    # Collect data from API
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("There was an ambiguous exception that occurred while handling your request.")

    # Print 'response' to check where bitcoin price is in dictionary
    # print(json.dumps(response.json(), indent=2))

    # Retrieve price of bitcoin in USD from object 'response'
    o = response.json()
    bitcoin_price = float(o["bpi"]["USD"]["rate"].replace(",", ""))

    # Compute price for the number of bitcoins input by user
    total = n * bitcoin_price

    # Print result on scren
    print(f"${total:,.4f}")

# Run 'main' function
if __name__ == "__main__":
    main()
