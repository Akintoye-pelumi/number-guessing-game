import random

def welcome():
	guess_level = input("Select level, Enter EASY, MEDIUM, or HARD: ").upper()
	return guess_level

def mode(guess_level):
	if (guess_level == "EASY"):
		guess_range = random.randint(1, 10)
		chances = 6
		count = 1
		guess = 0 
		chance_count = 0
		if guess == guess_range:
			print ("You got it right!")
		elif:
			print ("That was wrong!")
			print (f"you have {chances - count} guesses left")
		else:
			print ("Game Over")
	break

	elif (guess_level == "MEDIUM"):
		guess_range = random.randint(1, 20)
		chances = 4
		count = 1
		guess = 0 
		chance_count = 0
		if guess == guess_range:
			print ("You got it right!")
		elif:
			print ("That was wrong!")
			print (f"you have {chances - count} guesses left")
		else:
			print ("Game Over")
	break

	elif (guess_level == "HARD"):
		guess_range = random.randint(1, 50)
		chances = 3
		count = 1
		guess = 0 
		chance_count = 0
		if guess == guess_range:
			print ("You got it right!")
		elif:
			print ("That was wrong!")
			print (f"you have {chances - count} guesses left")
		else:
			print ("Game Over")
	break
	else:
		print("Enter a valid level")
break



