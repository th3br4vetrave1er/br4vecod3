import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    


player_choice = input("Enter ... \n1 for Rock \n2 for Paper or \n3 for Scissors \nVVVVVVVVVVVVVVV \n\n")

player = int(player_choice)
computer_choice = random.choice("123")
computer = int(computer_choice)


if player < 1 | player > 3:
    sys.exit("Enter 1, 2 or 3.")
    
    
print("")
print("You chose " + str(RPS(player)).replace("RPS.", "") + ".")
print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".")

if player == computer:
    print("😒 Its a tie!")
elif player == 2 and computer == 1:
    print("👌 You win!")
elif player == 3 and computer == 2:
    print("👌 You win!")
elif player == 1 and computer == 3:
    print("👌 You win!")
else:
    print("🐍 Python wins!")