import random
from colorama import Fore, Style, init


RULES = {
    "rock":     ["scissors", "lizard"],
    "paper":    ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard":   ["spock", "paper"],
    "spock":    ["scissors", "rock"],
}

OPTIONS = list(RULES.keys())


def play_round(user_choice: str, ai_choice: str) -> int:
    """Return 1 if user wins, -1 if AI wins, 0 for tie."""
    if user_choice == ai_choice:
        return 0
    if ai_choice in RULES[user_choice]:
        return 1
    return -1


def main():
    init(autoreset=True)
    print(Fore.CYAN + "Rock-Paper-Scissors-Lizard-Spock!")
    target = input("Play to how many wins? [3]: ")
    try:
        target_wins = int(target) if target else 3
    except ValueError:
        target_wins = 3
    user_score = 0
    ai_score = 0

    while user_score < target_wins and ai_score < target_wins:
        print(Fore.YELLOW + f"Score - You: {user_score}  AI: {ai_score}")
        user = input("Choose rock, paper, scissors, lizard, or spock (or quit): ").lower()
        if user == "quit":
            print("Thanks for playing!")
            return
        if user not in OPTIONS:
            print(Fore.RED + "Invalid choice.")
            continue
        ai_choice = random.choice(OPTIONS)
        print(f"AI chose {ai_choice}")
        result = play_round(user, ai_choice)
        if result == 0:
            print(Style.BRIGHT + "It's a tie!")
        elif result == 1:
            user_score += 1
            print(Fore.GREEN + "You win this round!")
        else:
            ai_score += 1
            print(Fore.MAGENTA + "AI wins this round!")
        print()

    if user_score > ai_score:
        print(Fore.GREEN + Style.BRIGHT + "Congratulations! You won the match.")
    else:
        print(Fore.MAGENTA + Style.BRIGHT + "AI won the match. Better luck next time!")


if __name__ == "__main__":
    main()
