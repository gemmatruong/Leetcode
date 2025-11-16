import random

def play_round(round_number):
    print(f"\n====== ROUND {round_number} ======\n")

    # --- 10 UNIQUE PUZZLES ---
    puzzles = [
        {
            "killer": "Mr. Black",
            "suspects": ["Mr. Black", "Ms. Rose", "Dr. Gray", "Mrs. White"],
            "clues": [
                "The killer always wears dark clothing.",
                "He was seen near the library around 9 PM.",
                "He is the tallest among the suspects."
            ]
        },
        {
            "killer": "Ms. Rose",
            "suspects": ["Mr. Steel", "Ms. Rose", "Chef Brown", "Lady Gold"],
            "clues": [
                "A rose petal was found at the crime scene.",
                "The killer has long hair.",
                "She was missing during the time of the murder."
            ]
        },
        {
            "killer": "Chef Brown",
            "suspects": ["Chef Brown", "Captain Blue", "Nurse Pink", "Mr. Silver"],
            "clues": [
                "Flour footprints were found.",
                "Someone smelled bread near the scene.",
                "The killer works in the kitchen."
            ]
        },
        {
            "killer": "Dr. Gray",
            "suspects": ["Dr. Gray", "Sergeant Jade", "Professor Mint", "Mr. Copper"],
            "clues": [
                "The killer knew anatomy extremely well.",
                "There were precise surgical cuts on the body.",
                "He was the last person to see the victim alive."
            ]
        },
        {
            "killer": "Professor Mint",
            "suspects": ["Professor Mint", "Mr. Bronze", "Captain Blue", "Sister Pearl"],
            "clues": [
                "The killer is highly educated.",
                "A piece of chalk was found near the victim.",
                "He teaches at the university."
            ]
        },
        {
            "killer": "Lady Gold",
            "suspects": ["Lady Gold", "Mr. Steel", "Dr. Gray", "Ms. Violet"],
            "clues": [
                "Witnesses say the killer wore expensive jewelry.",
                "She was upset about a stolen necklace.",
                "She comes from a wealthy family."
            ]
        },
        {
            "killer": "Mr. Bronze",
            "suspects": ["Mr. Bronze", "Chef Brown", "Dr. Gray", "Ms. Rose"],
            "clues": [
                "The killer had traces of metal on their hands.",
                "He works with heavy tools.",
                "He was repairing something earlier that day."
            ]
        },
        {
            "killer": "Captain Blue",
            "suspects": ["Captain Blue", "Mr. Black", "Nurse Pink", "Lady Gold"],
            "clues": [
                "Blue fabric was found torn at the scene.",
                "The killer has military training.",
                "He was seen running at high speed afterward."
            ]
        },
        {
            "killer": "Nurse Pink",
            "suspects": ["Nurse Pink", "Dr. Gray", "Mr. Silver", "Ms. Rose"],
            "clues": [
                "A medical glove was found near the victim.",
                "The killer knows basic medical care.",
                "She seemed nervous the entire evening."
            ]
        },
        {
            "killer": "Mr. Silver",
            "suspects": ["Mr. Silver", "Captain Blue", "Sister Pearl", "Professor Mint"],
            "clues": [
                "Silver dust was found nearby.",
                "He works in a jewelry shop.",
                "He owed the victim money."
            ]
        }
    ]

    case = random.choice(puzzles)
    killer = case["killer"]
    suspects = case["suspects"]

    print("Suspects:")
    for s in suspects:
        print(" -", s)

    print("\nClues:")
    for i, clue in enumerate(case["clues"], 1):
        print(f"Clue {i}: {clue}")

    guess = input("\nWho is the killer? ").strip()

    if guess.lower() == killer.lower():
        print("🔍 Correct! You solved the case!")
    else:
        print(f"❌ Wrong! The killer was: {killer}")

def play_game():
    print("🕵️ DETECTIVE GAME — FIND THE KILLER!")
    print("Up to 3 rounds per game.\n")

    round_number = 1

    while round_number <= 3:
        play_round(round_number)

        if round_number == 3:
            print("\n🎉 You reached Round 3 — Game Over!")
            break

        choice = input("\nDo you want to continue to the next round? (yes/no): ").strip().lower()
        if choice not in ["yes", "y"]:
            print("\n👋 You ended the game early. Goodbye Detective!")
            break

        round_number += 1

if __name__ == "__main__":
    play_game()
