import random

choices = ["rock", "paper", "scissors"]


def RockPaperScissors(player):
    computer = random.choice(choices)
    print(f"Computer: {computer.title()}")
    if player == computer:
        return 0
    elif player == "rock":
        if computer == "scissors":
            return 1
        else:
            return -1
    elif player == "paper":
        if computer == "rock":
            return 1
        else:
            return -1
    elif player == "scissors":
        if computer == "paper":
            return 1
        else:
            return -1


def main():
    player_score = 0
    computer_score = 0
    while True:
        player = input("Enter Rock, Paper, or Scissors: ").lower()
        if player not in choices:
            print("Invalid input. Please try again.")
            continue
        print(f"Player:{player.title()}")
        res = RockPaperScissors(player)
        if res == 0:
            print("It's a tie!")
        elif res == 1:
            print("Player wins!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        print(f"Player: {player_score}, Computer: {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"""\nFinal Score: \nPlayer: {
                  player_score}, Computer: {computer_score}""")
            if player_score > computer_score:
                print("Player wins!")
            elif player_score < computer_score:
                print("Computer wins!")
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
