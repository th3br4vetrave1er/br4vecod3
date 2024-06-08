# import sys
# import random
# from enum import Enum

# class RPS(Enum):
#     ROCK = 1
#     PAPER = 2
#     SCISSORS = 3
    


# player_choice = input("Enter ... \n1 for Rock \n2 for Paper or \n3 for Scissors \nVVVVVVVVVVVVVVV \n\n")

# player = int(player_choice)
# computer_choice = random.choice("123")
# computer = int(computer_choice)


# if player < 1 or player > 3:
#     sys.exit("Enter 1, 2 or 3.")
    
    
# print("")
# print("You chose " + str(RPS(player)).replace("RPS.", "") + ".")
# print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".")

# if player == computer:
#     print("😒 Its a tie!")
# elif player == 2 and computer == 1:
#     print("👌 You win!")
# elif player == 3 and computer == 2:
#     print("👌 You win!")
# elif player == 1 and computer == 3:
#     print("👌 You win!")
# else:
#     print("🐍 Python wins!")


# test = input()
# test_list = []
# test_list += test   
# print(test_list)



users = ["Dave", "John", "Sara"]

data = ["Dave", 42, True]

emptylist = []

print("Dave" in emptylist)

print(users[0])
print(users[-2])

print(users.index("Sara"))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))


users.append("Elsa")
print(users)

users += ["Jason"]
print(users)


users.extend(["Robert", "Jimmy"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Bob")
print(users)

users[2:2] = ["Eddie", "Alex"]
print(users)

users[1:3] = ["Robert", "JPJ"]
print(users)    

users.remove("Bob")
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)


users[1:2] = ["dave"]
users.sort()
print(users)


users.sort(key=str.lower)
print(users)