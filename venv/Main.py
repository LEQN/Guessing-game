import random
import tkinter as tk

class GameGUI:

    def __init__(self):
        # set window and size
        self.root = tk.Tk()
        self.root.geometry("500x700")
        self.root.title("Num Guess")

        self.label = tk.Label(self.root, text="Guess the Number", font=('Arial', 24, 'underline'))
        self.label.pack(padx=25, pady=100)

        # input frame
        self.inputFrame = tk.Frame(self.root)
        self.inputFrame.columnconfigure(0, weight=1)
        self.inputFrame.columnconfigure(1, weight=1)
        # range input
        self.rangeLabel = tk.Label(self.inputFrame, text="Range upperbound: ", font=('Arial', 12))
        self.rangeLabel.grid(row=0, column=0, pady=20)
        self.rangeEntry = tk.Entry(self.inputFrame)
        self.rangeEntry.grid(row=0, column=1, pady=20)
        # attempts input
        self.attemptLabel = tk.Label(self.inputFrame, text="Attempts: ", font=('Arial', 12))
        self.attemptLabel.grid(row=1, column=0, pady=20)
        self.attemptEntry = tk.Entry(self.inputFrame)
        self.attemptEntry.grid(row=1, column=1, pady=20)

        self.inputFrame.pack()
        # start button
        self.startButton = tk.Button(self.root, text="Start!", font=('Arial', 18))
        self.startButton.pack(padx=15, pady=15)

        self.root.mainloop()
GameGUI()


# -----game logic-----
# take input of range upperbound and number of attempts
# while True:
#     try:
#         upper_bound = int(input("Input an upperbound for the number generated: "))
#         attempts = int(input("Input the maximum number of attempts: "))
#         if upper_bound < 0 or attempts < 0:
#             print("Input needs to be greater than 0.")
#         else:
#             break
#     except ValueError:
#         print("Invalid input. Please enter valid integers.")
# # generate a random number within ranges
# goal = random.randint(0, upper_bound)
#
# def game_run(goal, attempts, upper):
#     while (attempts > 0):
#         # take user input guess
#         while True:
#             try:
#                 guess = int(input("Enter Guess: "))
#                 if guess > upper or guess < 0:
#                     print("Enter a guess lower than the upperbound")
#                 else:
#                     break
#             except ValueError:
#                 print("Input an Integer guess.")
#         # check the players guess against generated num
#         # if not ==,  attempt -1 and tell user whether guess is too high or too low
#         if (guess != goal):
#             if (guess > goal):
#                 print("Too high")
#             else:
#                 print("Too low")
#             attempts = attempts - 1
#             print(attempts)
#         else:
#             # if guess is correct end game
#             return "You win!! Remaining attempts: " + str(attempts)
#     return "You lost!! The number was " + str(goal)
#
#
# # attempts = 0 end game
# print(game_run(goal, attempts, upper_bound))