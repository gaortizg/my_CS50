def main():
    # Prompt user for name of a file
    file = input("File name: ")

    # Create tuples with suffixes
    suffix_app = (".pdf", ".zip")
    suffix_img = (".gif", ".jpg", ".jpeg", ".png")

    # Remove any leading and trailing whitespaces, and
    # make sure file name is lowercase
    file = file.strip().lower()

    # Split file name at '.', so we can retrieve file extension
    # from the resulting list (last element of the list)
    get_ext = file.split(".")[-1]

    # Check file extension. Print result on screen
    if file.endswith(suffix_app):
        print("application/" + get_ext)
    elif file.endswith(suffix_img):
        print("image/" + get_ext)
    elif file.endswith(".txt"):
        print("text/plain")
    else:
        print("application/octet-stream")

# Run 'main' function
if __name__ == "__main__":
    main()
