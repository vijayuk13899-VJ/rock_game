import random

# Rock-Paper-Scissors Game with Score Tracking

def play(scores):
    """Play one round and update scores."""
    choices = ["rock", "paper", "scissors"]

    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        return

    computer_choice = random.choice(choices)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")

    if user_choice == computer_choice:
        print("It's a tie!")
        scores["ties"] += 1
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("🎉 You win!")
        scores["wins"] += 1
    else:
        print("😢 You lose!")
        scores["losses"] += 1

def main():
    """Main function with replay and score tracking."""
    print("Welcome to Rock-Paper-Scissors with Scores! 🎮")
    scores = {"wins": 0, "losses": 0, "ties": 0}
