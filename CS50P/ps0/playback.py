def main():
    # Prompt user for input
    my_str = input()

    # Replace whitespaces with ... (i.e., three periods)
    my_str = my_str.replace(" ", "...")

    # Print modified string on screen
    print(f"{my_str}")

# Run 'main' function
if __name__ == "__main__":
    main()