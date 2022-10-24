# Started 17/10/22
from tkinter import *
import random

# Checks if the leaderboard file has been created
try:
	leaderboard = open("leaderboard.txt", "r")
except:
	leaderboard = open("leaderboard.txt", "w")

points = 0
lives = 10


def loginToGame():
	frameLogin.grid_forget()
	frameGame.grid(column=0, row=0)


def game():
	frameLead.grid_forget()
	frameGame.grid(column=0, row=0)


def leader():
	frameGame.grid_forget()
	frameLead.grid(column=0, row=0)


def submit():
	global points
	global lives
	randNum = random.randint(1, 10)
	num = int(guess.get())
	if lives > 1:
		if num == randNum:
			result.config(text="Correct!")
			points += 1
			pointsDis.config(text="Point(s): " + str(points))
		else:
			result.config(text="Incorrect!")
			lives -= 1
			livesDis.config(text="Live(s): " + str(lives))
	else:
		result.config(text="Out of lives! Points and lives have been reset!")
		points = 0
		pointsDis.config(text="Point(s): " + str(points))
		lives = 10
		livesDis.config(text="Live(s): " + str(lives))


root = Tk()
root.title("Guessing Game")
root.config(background="lightblue")
root.resizable(False, False)

# Login page
frameLogin = Frame(root)
frameLogin.config(background="lightblue")
frameLogin.grid(column=0, row=0)

Label(frameLogin, text="Login", font=("Arial", 24),
      background="lightblue").grid(column=0, row=0, columnspan=2, pady=5)

Label(frameLogin, text="Full Name:", background="lightblue").grid(column=0,
                                                                  row=1,
                                                                  padx=5,
                                                                  pady=5)
fullname = Entry(frameLogin)
fullname.grid(column=1, row=1, padx=5, pady=5)

Button(frameLogin, text="Submit", command=loginToGame).grid(column=0,
                                                            row=2,
                                                            columnspan=2,
                                                            pady=50)

# Main game page
frameGame = Frame(root)
frameGame.config(background="lightblue")

Label(frameGame,
      text="Guessing Game",
      font=("Arial", 24),
      background="lightblue").grid(column=0,
                                   row=0,
                                   columnspan=2,
                                   padx=30,
                                   pady=5)

Label(frameGame,
      text="Enter a number between 1 and 10:",
      background="lightblue").grid(column=0, row=1, columnspan=2, pady=3)

guess = Entry(frameGame, justify=CENTER)
guess.grid(column=0, row=2, columnspan=2)

livesDis = Label(frameGame,
                 text="Live(s): " + str(lives),
                 background="lightblue")
livesDis.grid(column=0, row=3, columnspan=2)

pointsDis = Label(frameGame,
                  text="Point(s): " + str(points),
                  background="lightblue")
pointsDis.grid(column=0, row=4, columnspan=2)

result = Label(frameGame, background="lightblue")
result.grid(column=0, row=5, columnspan=2)

Button(frameGame, text="View Leaderboard", command=leader).grid(column=0,
                                                                row=6,
                                                                pady=30)

Button(frameGame, text="Submit Guess", command=submit).grid(column=1,
                                                            row=6,
                                                            pady=30)

# Leaderboard page
frameLead = Frame(root)
frameLead.config(background="lightblue")

Label(frameLead,
      text="The Leaderboard",
      font=("Arial", 24),
      background="lightblue").grid(column=1, row=0, pady=5)

Label(frameLead, text="Rank", font=("Arial", 16),
      background="lightblue").grid(column=0, row=1, padx=15)
Label(frameLead, text="Name", font=("Arial", 16),
      background="lightblue").grid(column=1, row=1, padx=15)
Label(frameLead, text="Points", font=("Arial", 16),
      background="lightblue").grid(column=2, row=1, padx=15)

ranks = ""
for i in range(1, 11):
	rank = "#" + str(i) + "\n"
	ranks = ranks + rank
	Label(frameLead, text=ranks, background="lightblue").grid(column=0, row=2)

Button(frameLead, text="Back To Game", command=game).grid(column=1,
                                                          row=3,
                                                          pady=10)

root.mainloop()
