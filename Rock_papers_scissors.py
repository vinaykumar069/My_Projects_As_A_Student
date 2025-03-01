import random
print("-----------Welcome to the game--------------")
print("       __ROCK___PAPER___SCISSORS__")
moves = ["rock","paper","scissors"]
i=1
while i==1:
    sys_move= random.choice(moves)
    user_move = input("Enter:- ").lower()
    if sys_move=="rock":
        if user_move=="rock":
            print("mine is rock\nYay! it's a tie.")
        elif user_move=="paper":
            print("mine is rock\nI lose,you Win...may be next time.")
        elif user_move=="scissors":
            print("mine is rock\nBetter luck next time")
        else:
            print("wrong option/spelling")
    elif sys_move=="paper":
        if user_move=="rock":
            print("mine is paper\nYou lose.")
        elif user_move=="paper":
            print("mine is paper\nYou are lucky, it's a tie.")
        elif user_move=="scissors":
            print("mine is paper\nI lose.")
        else:
            print("wrong option/spelling")
    elif sys_move=="scissors":
        if user_move=="rock":
            print("mine is scissors\nLooks like I lost to you.")
        elif user_move=="paper":
            print("mine is scissors\nI win")
        elif user_move=="scissors":
            print("mine is scissors\nIt's a tie.")
        else:
            print("wrong option/spelling")
    sel = input("Wanna play again?(y/n)").lower()
    if sel=="y":
        i=1
    else:
        i=0
        print("Play again soon...")