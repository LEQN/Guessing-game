import random

# take input of range upperbound and number of attempts
while True:
    try:
        upper_bound = int(input("Input an upperbound for the number generated: "))
        attempts = int(input("Input the maximum number of attempts: "))
        break
    except ValueError:
        print("Invalid input. Please enter valid integers.")
# generate a random number within range
goal = random.randint(0, upper_bound)
gameover = False

while(attempts>0):
    # take user input guess
    while True:
        try:
            guess = int(input("Enter Guess: "))
            break
        except ValueError:
            print("Input an Integer guess.")
    # check the players guess against generated num
    # if not ==,  attempt -1 and tell user whether guess is too high or too low
    if(guess != goal):
        if(guess > goal):
            print("Too high")
        else:
            print("Too low")
        attempts= attempts-1
        print(attempts)
    else:
    # if guess is correct end game
        print("You win!! Remaining attempts: " , attempts)
        break

# attempts = 0 end game
# print("You lost! The number was ", goal)