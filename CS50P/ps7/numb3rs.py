import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Capture matches in 'ip'
    matches = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip)

    # Convert matches to integers
    try:
        num1 = int(matches.group(1))
        num2 = int(matches.group(2))
        num3 = int(matches.group(3))
        num4 = int(matches.group(4))

    # Catch errors
    except AttributeError:
        return False
    
    # If everything OK!
    else:
        check_nums = [num1, num2, num3, num4]
        if all(x <= 255 for x in check_nums):
            return True
        else:
            return False


# Run 'main' function
if __name__ == "__main__":
    main()