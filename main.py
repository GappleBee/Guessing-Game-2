# Started 17/10/22
from tkinter import *
import random

# Checks if the leaderboard file has been created
try:
	leaderboard = open("leaderboard.txt", "r")
	leaderboard.close()
except:
	leaderboard = open("leaderboard.txt", "w")
	leaderboard.close()

points = 0
lives = 10


def loginToGame():
	global fullName
	fullName = name.get()
	frameLogin.grid_forget()
	frameGame.grid(column=0, row=0)


def game():
	frameLead.grid_forget()
	frameGame.grid(column=0, row=0)


def leader():
	pointsList = []
	leaderboard = open("leaderboard.txt", "r")
	for row in leaderboard:
		field = row.split(", ")
		pointsList.append(str(field[1]))
	pointsList = sorted(pointsList, reverse=True)
	leaderboard.close()

	entriesList = []
	for i in range(len(pointsList)):
		leaderboard.close()
		leaderboard = open("leaderboard.txt", "r")
		for row in leaderboard:
			field = row.split(", ")
			if pointsList[i] == field[1]:
				entriesList.append(row)

	if len(entriesList) < 10:
		names = ""
		nums = ""
		for i in range(len(entriesList)):
			entry = entriesList[i].split(", ")
			name = entry[0] + "\n"
			num = entry[1]
			names += name
			nums += num
		for i in range(10 - len(entriesList)):
			names += "\n"
			nums += "\n"
		Label(frameLead, text=names, background="lightblue").grid(column=1, row=2)
		Label(frameLead, text=nums, background="lightblue").grid(column=2, row=2)
	else:
		names = ""
		nums = ""
		for i in range(10):
			entry = entriesList[i].split(", ")
			name = entry[0] + "\n"
			num = entry[1] + "\n"
			names += name
			nums += num
			Label(frameLead, text=names, background="lightblue").grid(column=1, row=2)
			Label(frameLead, text=nums, background="lightblue").grid(column=2, row=2)

	leaderboard.close()
	frameGame.grid_forget()
	frameLead.grid(column=0, row=0)


def submit():
	global points
	global lives
	randNum = random.randint(1, 10)
	num = int(guess.get())
	if 1 <= num <= 10:
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
			entry = fullName + ", " + str(points) + "\n"
			leaderboard = open("leaderboard.txt", "r")
			inList = 0
			for row in leaderboard:
				if entry == row:
					inList = 1
			if inList != 1:
				leaderboard.close()
				leaderboard = open("leaderboard.txt", "a")
				leaderboard.write(entry)
			leaderboard.close()
			points = 0
			pointsDis.config(text="Point(s): " + str(points))
			lives = 10
			livesDis.config(text="Live(s): " + str(lives))
	else:
		result.config(text="Invalid input! Enter a number between 1 and 10!")


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
name = Entry(frameLogin)
name.grid(column=1, row=1, padx=5, pady=5)

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
	ranks += rank
	Label(frameLead, text=ranks, background="lightblue").grid(column=0, row=2)

Button(frameLead, text="Back To Game", command=game).grid(column=1,
                                                          row=3,
                                                          pady=10)

root.mainloop()
