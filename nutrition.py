fruits = [
    {"item": "apple", "calories": 130},
    {"item": "avocado", "calories": 50},
    {"item": "banana", "calories": 110},
    {"item": "cantaloupe", "calories": 50},
    {"item": "grapefruit", "calories": 60},
    {"item": "grapes", "calories": 90},
    {"item": "honeydew melon", "calories": 50},
    {"item": "kiwi", "calories": 90},
    {"item": "lemon", "calories": 15},
    {"item": "lime", "calories": 20},
    {"item": "nectarine", "calories": 60},
    {"item": "orange", "calories": 80},
    {"item": "peach", "calories": 60},
    {"item": "pear", "calories": 100},
    {"item": "pineapple", "calories": 50},
    {"item": "plum", "calories": 70},
    {"item": "strawberry", "calories": 50},
    {"item": "sweet cherry", "calories": 100},
    {"item": "tangerine", "calories": 50},
    {"item": "watermelon", "calories": 80}
]

def main():
    user_input = input("Item: ").lower()
    
    for fruit in fruits:
        if user_input == fruit["item"]:
            print(f"Calories: {fruit['calories']}")
            return
    
    print("Fruit not found in the list.")

if __name__ == "__main__":
    main()