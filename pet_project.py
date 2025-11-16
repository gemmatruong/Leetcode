import random

def play_game():
    print("🕵️ DETECTIVE GAME: Find the Killer!")
    print("-------------------------------------")
    print("You will receive 3 clues. Use them to identify the killer.\n")

    puzzles = [
        {
            "killer": "Mr. Black",
            "suspects": ["Mr. Black", "Ms. Rose", "Dr. Gray", "Mrs. White"],
            "clues": [
                "The killer always wears dark colors.",
                "He was seen near the library at 9 PM.",
                "He is the tallest among all suspects."
            ]
        },
        {
            "killer": "Ms. Rose",
            "suspects": ["Mr. Steel", "Ms. Rose", "Chef Brown", "Lady Gold"],
            "clues": [
                "The killer left behind a rose petal.",
                "Witnesses say the killer has long hair.",
                "She was the only one without an alibi."
            ]
        },
        {
            "killer": "Chef Brown",
            "suspects": ["Chef Brown", "Captain Blue", "Nurse Pink", "Mr. Silver"],
            "clues": [
                "Flour footprints were found at the crime scene.",
                "The killer is someone who works in the kitchen.",
                "He is known for having a bad temper."
            ]
        },
        {
            "killer": "Dr. Gray",
            "suspects": ["Dr. Gray", "Sergeant Jade", "Professor Mint", "Mr. Copper"],
            "clues": [
                "The killer knows anatomy very well.",
                "The body showed very precise cuts.",
                "He was the last person to see the victim alive."
            ]
        }
    ]

    # pick a random case
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
        print("🔍 Correct! You solved the murder!")
    else:
        print(f"❌ Wrong! The killer was: {killer}")

    print("\nThanks for playing, Detective!")

if __name__ == "__main__":
    play_game()
