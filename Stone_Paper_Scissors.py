import random

list = ['st','p','sc']

chance = 5
no_of_chance = 0
computer_point = 0
human_point = 0

print("\t\t\t Stone, Paper,Scissor \n\n")
print("'st' for stone\n 'p' for Paper\n 'sc' for Scissor")

while no_of_chance < chance :
    _input = input("Choose 'st , 'p' , sc'\n")
    _random = random.choice(list)

    if _input == _random :
        print("TIE,BOTH HAVE SAME ANSWER,0 POINTS\n")

    #If user enter st

    elif _input == "st" and _random =="p":
        computer_point = computer_point + 1
        print(f"Your Guess {_input} and computer Guess is {_random}\n")
        print("Computer gets +1 Points")
        print(f"Computer points is {computer_point} and Your points is {human_point}\n")

    elif _input == "st" and _random =="sc":
        human_point = human_point + 1
        print(f"Your Guess {_input} and computer Guess is {_random}\n")
        print("Human wins +1 Points")
        print(f"Computer points is {computer_point} and Your points is {human_point}\n")

    #if user enter p
    elif _input == "p" and _random =="sc":
        computer_point = computer_point + 1
        print(f"Your Guess {_input} and computer Guess is {_random}\n")
        print("Computer wins +1 Points")
        print(f"Computer points is {computer_point} and Your points is {human_point}\n")

    elif _input == "p" and _random =="st":
        human_point = human_point + 1
        print(f"Your Guess {_input} and computer Guess is {_random}\n")
        print("Human wins +1 Points")
        print(f"Computer points is {computer_point} and Your points is {human_point}\n")

    #if user enter sc
    elif _input == "sc" and _random =="st":
        computer_point = computer_point + 1
        print(f"Your Guess {_input} and computer Guess is {_random}\n")
        print("Computer wins +1 Points")
        print(f"Computer points is {computer_point} and Your points is {human_point}\n")

    elif _input == "sc" and _random =="p":
        human_point = human_point + 1
        print(f"Your Guess {_input} and computer Guess is {_random}\n")
        print("Human wins +1 Points")
        print(f"Computer points is {computer_point} and Your points is {human_point}\n")

    else:
        print("Wrong Input, Try again\n")

    no_of_chance = no_of_chance+1
    print(f"{chance-no_of_chance} chances are left out of {chance} \n")

print("GAMEOVER\n")

if computer_point>human_point:
    print("COMPUTER WINS\n")

elif computer_point ==human_point:
    print("GAME TIED\n")

else:
    print("YOU WON\n")

print(f"YOUR FINAL POINTS ARE {human_point} AND COMPUTER POINTS ARE {computer_point} ")










