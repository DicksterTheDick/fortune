import random
import json

def load_card_meanings(filename="card_meanings.json"):
    """Loads card meanings from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

def draw_cards(card_meanings, num_cards=1):
    """Randomly selects cards from the deck."""
    cards = random.sample(list(card_meanings.keys()), num_cards)
    return [(card, card_meanings[card]) for card in cards]

def display_card_and_meaning(cards_and_meanings, spread_type="Single Card"):
    """Displays the card(s) and their meaning(s) to the user."""

    gradient_border = "▓▒░░▒▓░▒░▒▓░▒░▒▓░▒░▒▓░▒░▒▓░▒░▒▓░▒░▒▓░▒░▒▓░▒░▒▓░▒░▒▓░▒░▒▓░▒░▒"

    if spread_type == "Single Card":
        print(f"    🔮  ▓▒░ Your Card ░▒▓  🔮\n")
        print(f"     {cards_and_meanings[0][0]}     ")
        print(f"  Meaning: {cards_and_meanings[0][1]}  \n")

    elif spread_type == "Three-Card Spread":
        print(f"    🔮  ▓▒░ Three-Card Spread ░▒▓  🔮\n")
        print(gradient_border)

        positions = ["Past", "Present", "Future"]
        general_interpretations = [
            "This card represents the events, influences, or factors that have led up to the current situation. It can provide context and help understand the roots of the issue.",
            "This card reflects the current situation, challenges, or opportunities. It gives a snapshot of where the querent (the person seeking guidance) stands at the moment.",
            "This card suggests the likely outcome or future development of the situation, based on the current trajectory. It's important to remember that the future isn't fixed, and this card often indicates potential outcomes or tendencies."
        ]

        for i in range(3):
            print(gradient_border)
            print(f"               ▓▒░ {positions[i]} Card: {cards_and_meanings[i][0]} ░▒▓")
            print(f"Meaning: {cards_and_meanings[i][1]}")
            print(f"\nGeneral Interpretation:\n{general_interpretations[i]}\n")

def main():
    """Main function to run the fortune-teller."""

    gradient_border = "▓▒░░▒▓░▒░▒▓░▒░▒▓░▒░▒▓░▒░▒▓░▒░▒▓░▒░▒▓░▒░▒▓░▒░▒▓░▒░▒▓░▒░▒▓░▒░▒"

    print(f"    🔮  ▓▒░ Welcome to the Python Fortune Teller! ░▒▓  🔮\n")
    print(gradient_border)

    card_meanings = load_card_meanings()

    while True:
        print("\nChoose an option:")
        print("1. Single Card Draw")
        print("2. Three-Card Spread (Past, Present, Future)")
        print("3. Leave")  # Added Leave option
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            cards = draw_cards(card_meanings, 1)
            display_card_and_meaning(cards, "Single Card")
        elif choice == '2':
            cards = draw_cards(card_meanings, 3)
            display_card_and_meaning(cards, "Three-Card Spread")
        elif choice == '3':
            leave_choice = input("Are you sure you want to leave? (y/n): ")
            if leave_choice.lower() == 'y':
                print("Goodbye!")
                break  # Exit the main loop
            else:
                continue  # Go back to the main menu
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        draw_again = input("\nDraw again? (y/n): ")
        if draw_again.lower() != 'y':
            continue  # Go back to the main menu

if __name__ == "__main__":
    main()
