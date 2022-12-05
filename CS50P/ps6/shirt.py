import os
from PIL import Image, ImageOps
import sys

def main():
    # validate command-line arguments
    check_argv = validate_sys_argv(sys.argv)

    if check_argv:
        # Retrieve filenames of images
        img_read = sys.argv[1]
        img_write = sys.argv[2]

        # Overlay images
        overlay_png(img_read, img_write)


def validate_sys_argv(my_argv):
    # Validate number of command-line arguments
    num_com = len(my_argv)
    if num_com < 3:
        sys.exit("Too few command-line arguments")
    elif num_com > 3:
        sys.exit("Too many command-line arguments")
    else:
        # List with valid file extensions
        valid_ext = [".jpg", ".jpeg", ".png"]
        
        # Check file extension (make sure is lowercase)
        ext1 = os.path.splitext(sys.argv[1].lower())
        ext2 = os.path.splitext(sys.argv[2].lower())
        if (ext1[1] not in valid_ext) or (ext2[1] not in valid_ext):
            sys.exit("This program only works with .jpg, .jpeg, .png files")
        elif not(ext1[1] == ext2[1]):
            sys.exit("Input and output have different extensions")
    
    # If we reach this line, everything OK!
    return True


def overlay_png(before, after):
    # Open file with 'shirt'
    try:
        shirt = Image.open("img/shirt.png")

    # If image does not exist, inform user
    except FileNotFoundError:
        sys.exit("Input does not exist")
    
    # Compute size of shirt image
    size_shirt = shirt.size

    # Open image to overlay with 'shirt'
    try:
        with Image.open(before) as im:
            # Resize input
            im_resized = ImageOps.fit(im, size_shirt)

    # If image does not exist, inform user
    except FileNotFoundError:
        sys.exit("Input does not exist")
    
    # If everything OK!
    else:
        # Overlay the shirt on im_resized
        im_resized.paste(shirt, shirt)

        # Save new image
        im_resized.save(after)

# Run 'main' function
if __name__ == "__main__":
    main()