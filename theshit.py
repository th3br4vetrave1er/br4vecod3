from random import randint
win_num = randint(0, 100)
print("GUESSING GAME!!!")
print(win_num)
guess = int(input("ENTER THE NUM IN DIGITS: "))

while guess != win_num:
    if guess < win_num:
        print("A little higher, mate!")
    elif guess > win_num:
        print("Too much, mate!")
    guess = int(input("GUESS AGAIN: "))
    
if guess == win_num:
    print(f"YOU GUESSED IT! {guess} IS THE WIN NUM!!!")