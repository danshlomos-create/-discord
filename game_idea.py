import random

def generate_game():
    print("--- 🎮 Welcome to PlayForge AI Idea Generator 🎮 ---")
    mood = input("How are you feeling today? (bored / energetic / creative): ").lower()

    themes = {
        "bored": ["Space Adventure", "Deep Sea Mystery", "Lost in a Deserted Island"],
        "energetic": ["Fast-paced Racing", "Ninja Battle", "Neon Parkour"],
        "creative": ["World Builder", "Magic Potion Shop", "Dinosaur Zoo"]
    }

    mechanics = ["Gravity Flip", "Time Freeze", "Shape Shifting", "Double Jump"]

    if mood in themes:
        selected_theme = random.choice(themes[mood])
        selected_mech = random.choice(mechanics)
        
        print(f"\n🚀 Your unique game idea for today:")
        print(f"Theme: {selected_theme}")
        print(f"Special Power: {selected_mech}")
        print(f"\nGo build it in Lovable or Roblox! 🛠️")
    else:
        print("That mood isn't in my database yet, but I'm sure it's a great day for a new game!")

if __name__ == "__main__":
    generate_game()
