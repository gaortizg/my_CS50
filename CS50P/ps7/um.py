import re

def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"\bum\W?\b", s, flags=re.IGNORECASE)
    return len(matches)


# Run 'main' function
if __name__ == "__main__":
    main()