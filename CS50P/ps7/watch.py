import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        matches = re.search(r"^<iframe.*src=\"https?://(?:www\.)?(youtube.com/embed/\w+)\"(?:.*)?></iframe>$", s.strip())
    
        # retrieve link from RE search
        my_link = matches.group(1)
    
    # If no match (i.e., no valid YouTube link), catch error
    except AttributeError:
        return None
    
    # If everything OK!
    else:
        # Split link
        my_link = my_link.split("/")
        
        # Return shorter, shareable YouTube link
        return "https://youtu.be/" + my_link[2]


# Run 'main' function
if __name__ == "__main__":
    main()