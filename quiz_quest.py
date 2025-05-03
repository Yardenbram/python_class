import random

# 2. Define the question bank
questions = {
    "science": [
        {"q": "What planet is known as the Red Planet?", "a": "mars"},
        {"q": "What gas do plants absorb from the atmosphere?", "a": "carbon dioxide"},
    ],
    "history": [
        {"q": "Who was the first president of the United States?", "a": "george washington"},
        {"q": "In which year did World War II end?", "a": "1945"},
    ],
    "pop culture": [
        {"q": "Who sang 'Thriller'?", "a": "michael jackson"},
        {"q": "What movie features the quote 'I'll be back'?", "a": "the terminator"},
    ]
}

# 3. Initialize game variables
players = []
scores = {}
rounds = 3

# 4. Write helper functions
def ask_question(player):
    print(f"\n{player}, it's your turn.")
    category = input("Choose a category (science, history, pop culture): ").strip().lower()
    if category not in questions:
        print("Invalid category. Turn skipped.")
        return

    question = random.choice(questions[category])
    print("Question:", question["q"])
    answer = input("Your answer: ").strip().lower()

    if answer == question["a"]:
        print("Correct!")
        scores[player] += 1
    else:
        print(f"Wrong. The correct answer was: {question['a']}")

def show_scores():
    print("\nCurrent Scores:")
    for player in players:
        print(f"{player}: {scores[player]}")

def declare_winner():
    print("\nFinal Results:")
    show_scores()
    max_score = max(scores.values())
    winners = [p for p, s in scores.items() if s == max_score]

    if len(winners) == 1:
        print(f"Congratulations {winners[0]}! You won with {max_score} points.")
    else:
        print("It's a tie between:", ", ".join(winners), f"with {max_score} points each!")

# 5. Build the main game flow
def main():
    print("Welcome to Quiz Quest!")
    try:
        num_players = int(input("How many players? "))
        if num_players < 1:
            raise ValueError
    except ValueError:
        print("Invalid number of players. Exiting.")
        return

    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ").strip()
        players.append(name)
        scores[name] = 0

    for r in range(1, rounds + 1):
        print(f"\n--- Round {r} ---")
        for player in players:
            ask_question(player)
        show_scores()

    declare_winner()

if __name__ == "__main__":
    main()
