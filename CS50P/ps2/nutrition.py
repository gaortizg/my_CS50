def main():
    # Prompt user for input
    item = input("Item: ")

    # Create dictionary
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "necatrine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    # Search for user's input in dictionary. Print result on screen
    if item.lower() in fruits:
        print(f"Calories: {fruits[item.lower()]}")

# Run 'main' function
if __name__ == "__main__":
    main()
