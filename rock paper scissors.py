import random
moves = ["rock", "paper", "scissors"]
keep_playing = "true"
while keep_playing == "true":
    cmove = random.choice(moves)
    pmove = input("What is your move: rock, paper or scissors?")
    print ("the computer chose",cmove)
    if cmove == pmove:
        print ("tie")
    elif pmove == "rock" and cmove == "scissors":
        print ("player wins")
    elif pmove == "rock" and cmove == "paper":
        print ("computer wins")
    elif pmove == "paper" and cmove == "rock":
        print ("player wins")
    elif pmove == "paper" and cmove == "scissors":
        print ("computer wins")
    elif pmove == "scissors" and cmove == "paper":
        print ("player wins")
    elif pmove == "scissors" and cmove == "rock":
        print ("computer wins")
        
