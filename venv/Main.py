import random

# take input of range upperbound and number of attempts
while True:
    try:
        upper_bound = int(input("Input an upperbound for the number generated: "))
        attempts = int(input("Input the maximum number of attempts: "))
        if upper_bound < 0 or attempts < 0:
            print("Input needs to be greater than 0.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter valid integers.")
# generate a random number within ranges
goal = random.randint(0, upper_bound)

def game_run(goal, attempts, upper):
    while (attempts > 0):
        # take user input guess
        while True:
            try:
                guess = int(input("Enter Guess: "))
                if guess > upper or guess < 0:
                    print("Enter a guess lower than the upperbound")
                else:
                    break
            except ValueError:
                print("Input an Integer guess.")
        # check the players guess against generated num
        # if not ==,  attempt -1 and tell user whether guess is too high or too low
        if (guess != goal):
            if (guess > goal):
                print("Too high")
            else:
                print("Too low")
            attempts = attempts - 1
            print(attempts)
        else:
            # if guess is correct end game
            return "You win!! Remaining attempts: " + str(attempts)
    return "You lost!! The number was " + str(goal)


# attempts = 0 end game
print(game_run(goal, attempts, upper_bound))