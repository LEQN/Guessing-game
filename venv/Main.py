import random
import tkinter as tk
from tkinter import messagebox

class GameGUI:

    def __init__(self):
        # set window and size
        self.root = tk.Tk()
        self.root.geometry("500x700")
        self.root.title("Num Guess")
        self.root.configure(background='DodgerBlue')

        # create upperbound and attempts variables
        self.upper = 0
        self.attempts = 0
        # load all the pages and store them
        self.pages = []
        self.current_page_index = 0

        self.start_page()
        self.guess_page()
        self.display_current()

        self.root.mainloop()

    # load the frame for the start page and add to the list
    def start_page(self):
        self.start_frame = tk.Frame(self.root, bg='DodgerBlue')
        self.label = tk.Label(self.start_frame, text="Guess the Number", font=('Arial', 24, 'underline', 'bold'),
                              bg='DodgerBlue', fg='white')
        self.label.pack(padx=25, pady=80)
        # input frame
        self.inputFrame = tk.Frame(self.start_frame, bg='DodgerBlue')
        self.inputFrame.columnconfigure(0, weight=1)
        self.inputFrame.columnconfigure(1, weight=1)
        # range input
        self.rangeLabel = tk.Label(self.inputFrame, text="Range upperbound: ", font=('Arial', 16), bg='DodgerBlue',
                                   fg='white')
        self.rangeLabel.grid(row=0, column=0, pady=20)
        self.rangeEntry = tk.Entry(self.inputFrame)
        self.rangeEntry.bind("<KeyPress>", self.shortcut)
        self.rangeEntry.grid(row=0, column=1, pady=20)
        # attempts input
        self.attemptLabel = tk.Label(self.inputFrame, text="Attempts: ", font=('Arial', 16), bg='DodgerBlue',
                                     fg='white')
        self.attemptLabel.grid(row=1, column=0, pady=20)
        self.attemptEntry = tk.Entry(self.inputFrame)
        self.attemptEntry.bind("<KeyPress>", self.shortcut)
        self.attemptEntry.grid(row=1, column=1, pady=20)

        self.inputFrame.pack(padx=25, pady=25)
        # start button
        self.buttonBorder = tk.Frame(self.start_frame, highlightbackground='white', highlightthickness=2, bd=0)
        self.startButton = tk.Button(self.buttonBorder, text="Start!", font=('Arial', 18), height=2, width=10,
                                     bg='DodgerBlue', fg='white', command=self.check_start_input)
        self.startButton.pack()
        self.buttonBorder.pack(padx=15, pady=80)

        self.pages.append(self.start_frame)

    # retrieve the input in the entry boxes and check the type and values are valid before loading next scene and
    # starting the game.
    def check_start_input(self):
        try:
            self.upper = int(self.rangeEntry.get())
            self.attempts = int(self.attemptEntry.get())

            if self.upper <= 0 or self.attempts <= 0:
                messagebox.showerror(title="Error", message="Input must be greater than 0.")
            else:
                self.goal = random.randint(0, self.upper)
                self.current_page_index += 1
                self.display_current()
        except ValueError:
            messagebox.showerror(title="Error", message="Invalid input. Please enter a valid Integer.")

    # load the frame for the guessing page. The game begins before this page loads.
    def guess_page(self):
        self.guess_frame = tk.Frame(self.root, bg='DodgerBlue')

        self.titleLabel = tk.Label(self.guess_frame, text="Guess the Number", font=('Arial', 18, 'underline', 'bold'),
                              bg='DodgerBlue', fg='white')
        self.titleLabel.pack(padx=25, pady=80)
        self.guessEntry = tk.Entry(self.guess_frame)
        self.guessEntry.bind("<KeyPress>", self.shortcut)
        self.guessEntry.pack(padx=25, pady=80)

        self.buttonBorder = tk.Frame(self.guess_frame, highlightbackground='white', highlightthickness=2, bd=0)
        self.startButton = tk.Button(self.buttonBorder, text="Enter Guess!", font=('Arial', 18), height=2, width=10,
                                     bg='DodgerBlue', fg='white', command=self.guess_check)
        self.startButton.pack()
        self.buttonBorder.pack(padx=15, pady=80)
        self.guess_frame.pack()

        self.pages.append(self.guess_frame)

    # display the current page
    def display_current(self):
        for page in self.pages:
            page.pack_forget()

        current_page = self.pages[self.current_page_index]
        current_page.pack()

    def shortcut(self, event):
        if self.current_page_index == 0:
            if (event.state == 8 and event.keysym == "Return") or (event.state == 262152 and event.keysym == "Return"):
                if len(self.attemptEntry.get()) == 0:
                    self.attemptEntry.focus_set()
                else:
                    self.check_start_input()
        elif self.current_page_index == 1:
            if (event.state == 8 and event.keysym == "Return") or (event.state == 262152 and event.keysym == "Return"):
                self.guess_check()

    # check guess is valid
    def guess_check(self):
        try:
            guess = int(self.guessEntry.get())
            if guess >= self.upper or guess < 0:
                messagebox.showerror(title="Error",
                                     message="Guess must be a positive value and less than or equal to the upperbound.")
            else:
                self.game_logic(guess)
        except ValueError:
            messagebox.showerror(title="Error", message="Input a valid guess integer.")

    # do all main game logic
    def game_logic(self, guess):
        self.attempts -= 1
        if self.attempts > 0:
            if guess != self.goal:
                if guess > self.goal:
                    print("Too high")
                else:
                    print("Too low")
            else:
                print("You win! Guesses left over: ", self.attempts)
        else:
            print("you lose")
            exit()

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
#
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