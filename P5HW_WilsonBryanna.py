#Bryanna Wilson
#5/7/2025
#P5HW – Cooking Chaos Game
#A memory based cooking game where the player collects ingredients in the correct order to make a meal. 
#Wrong order or delays cause the pot to explode in true cartoon fashion! 💥🍲

import random
import time

# Value-returning function: returns shuffled list of ingredients
def get_ingredients():
    correct_ingredients = [
        {"name": "carrots", "order": 1},
        {"name": "potatoes", "order": 2},
        {"name": "onions", "order": 3},
        {"name": "spices", "order": 4},
        {"name": "broth", "order": 5}
    ]
    
    wrong_ingredients = [
        {"name": "banana", "order": 0},
        {"name": "ice cream", "order": 0},
        {"name": "chocolate", "order": 0},
        {"name": "cheese", "order": 0},
        {"name": "apple", "order": 0}
    ]

    all_ingredients = correct_ingredients + wrong_ingredients
    random.shuffle(all_ingredients)
    return all_ingredients, correct_ingredients

# Function to display the explosion scene
def explosion_scene():
    print("\n💥 KA-BOOM!!")
    print("You added the wrong ingredient! The pot exploded!")
    print("You're now a soot-covered cartoon character 😵‍💫🧨\n")

# Function to display success scene
def success_scene():
    print("\n🎉 Congratulations!")
    print("You made the perfect stew! The kitchen smells amazing 😋🍲")
    print("You’ve earned your Golden Chef Hat! 👨‍🍳👑\n")

# Function to show a 10-second countdown
def show_countdown():
    print()
    for i in range(10, 0, -1):
        print(f"{i}...")
        time.sleep(0.7)  # Short enough to keep things moving
    print()

# Function to play the game
def cook(ingredients, correct_ingredients):
    print("👨‍🍳 Welcome to Cooking Chaos! 🍲")
    print("Your goal: Add the ingredients in the correct order to make a perfect stew.")
    print("Add one wrong ingredient or make a mistake, and... 💥 KA-BOOM!\n")

    print("📝 Here's the correct order — memorize it!")
    for item in correct_ingredients:
        print(f" ➤ {item['name'].capitalize()}")
    print()
    print()
    print()
    print()

    show_countdown()

    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("🧠 Time's up! Let's see if you remember it...\n")
    time.sleep(0.5)
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("Start cooking!\n🔥 Time to cook! Add the ingredients in the correct order.")

    correct_order = [item['name'] for item in correct_ingredients]
    collected = []

    for i in range(5):
        print(f"\nStep {i + 1}: Choose the correct ingredient to add.")
        print("Available ingredients:")

        for idx, item in enumerate(ingredients):
            print(f"{idx + 1}. {item['name'].capitalize()}")

        try:
            choice = int(input("Enter the NUMBER of the ingredient: "))
            chosen = ingredients.pop(choice - 1)
            collected.append(chosen['name'])

            if chosen['order'] == 0 or collected[-1] != correct_order[len(collected) - 1]:
                explosion_scene()
                return

            print(f"✅ {chosen['name'].capitalize()} added successfully!")

        except (ValueError, IndexError):
            print("\n❌ Invalid input! That messes up the recipe!")
            explosion_scene()
            return

        time.sleep(0.8)

    success_scene()

# Main function that controls the game
def main():
    play_again = "yes"
    while play_again.lower() in ["yes", "y"]:
        ingredients, correct_ingredients = get_ingredients()
        cook(ingredients, correct_ingredients)
        play_again = input("Would you like to play again? (yes/no): ")
        print()
          # Exit note when the player chooses 'no'
    if play_again.lower() in ["no", "n"]:
        print("\n🧹 The kitchen is clean and the chef is taking a well-deserved nap. 🍵😴")
        print("Thanks for playing Cooking Chaos! Come back soon for another culinary adventure! 👩‍🍳🍲✨")
    
if __name__ == "__main__":
    main()
