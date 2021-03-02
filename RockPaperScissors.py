import random as rndm
computer_score = 0
player_score = 0
while True:
    player = input("Enter your choice (Rock, Paper, Scissors): ")
    moves = ["Rock", "Paper", "Scissors"]
    computer = rndm.choice(moves)
    print(f"\nYou choose {player}, Computer choose {computer}.\n")

    if player == computer:
        print(f"Both players selected {player}. It's a tie!")
    elif player == "Rock":
        if computer == "Scissors":
            print("Rock smashes Scissors! You win!")
            player_score+=1
        else:
            print("Paper covers rock! You lose.")
            computer_score+=1
    elif player == "Paper":
        if computer == "Rock":
            print("Paper covers rock! You win!")
            player_score+=1
        else:
            print("Scissors cuts paper! You lose.")
            computer_score+=1
    elif player == "Scissors":
        if computer == "Paper":
            print("Scissors cuts paper! You win!")
            player_score+=1
        else:
            print("Rock smashes scissors! You lose.")
            computer_score+=1

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
print("PLAYER SCORE : ",player_score)
print("COMPUTER SCORE :",computer_score)
if player_score == computer_score:
    print("TIE!!!")
elif player_score > computer_score:
    print("YEAH!!!YOU WON")
else:
    print("OHH!!!YOU LOST")
