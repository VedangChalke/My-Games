n=int(input("Select guess no\n"))
no_of_guesses = 1
print("No of guesses limited to 9 only\n")
while(no_of_guesses<=9):
    guess_number = int(input("Select number \n"))
    if guess_number<n:
        print("Your guess is too low \n")
    elif guess_number>n:
        print("Your guess is too high \n")
    else:
        print("You Won \n")
        print(no_of_guesses,"No of guesses u took to finish \n")
        break

    print(9-no_of_guesses,"no of guesses left\n")
    no_of_guesses=no_of_guesses+1

if(no_of_guesses>9):
     print("Game Over")

