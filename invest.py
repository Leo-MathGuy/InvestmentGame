# By Leo-MathGuy
# You can copy this code if you don't sell it, attribute it to me, and share it with this same licence.

"""
Code order:

Line function
Gamemode
Ask
Ask control
Money
Banks
Wait
Stats
Tutorial
Main game
Beginning
"""
from math import *
from time import sleep

# Beggining message
print("By Leo-MathGuy \n")
print("Welcome to the investment game! \n\n")

day = 1
hour = 8
money = 0

# Beatiful seperator

def line(x):
	print("-"*x)
# Game Modes
class gamemode:
	def __init__(self, name, advanced, startmoney, goal):
		self.name = name
		self.advanced = False #Disabled for now
		self.start = startmoney
		self.goal = goal * 10000 #To avoid unnecessary 0s

################################################################################################################################

# Things that start with a g before a word are linked to the gamemode
gveasy = gamemode("Very Easy", False, 250, 50)
geasy = gamemode("Easy", False, 150, 100)
gmed = gamemode("Medium", False, 100, 100)
ghard = gamemode("Hard", False, 75, 150)
gvhard = gamemode("Very Hard", True, 50, 200)
gbrut = gamemode("Brutal", True, 30, 500)

################################################################################################################################

def ask(q, h,  help=True, mega=False,  **kwargs):  #Universal ask function. Provide quesiton, help, and kwargs as option:return
	if not mega:
		optionl = list(kwargs.keys())
		options = ""
		for i in range(0, len(optionl)):
			options += str(optionl[i])
			options += "/"
	
		if help:
			options += "Help"
		else:
			options = options[:-1]
	
		while True:
			inpt = input("{} ({}): ".format(q, options))
			if inpt == "help" and help:
				print(h)
			else:
				for item in optionl:
					if inpt.title() == item:
						return kwargs[inpt.title()]
			
				print("Error: Unknown Input. Please enter valid option\n")
	
	else:
		keys = list(kwargs.keys())

		print(q + "\n")
		while True:
			for key in keys:
				print(key + f" [{kwargs[key]}]")
			
			inpt = input("\nChoose an option: ")
			
			if inpt.title() in list(kwargs.values()):
				return inpt.title()
			elif inpt.title() in keys:
				return kwargs[inpt.title()]
			else:
				print("\nPlease enter a valid option.\n")
			
################################################################################################################################

whatDo = "What do you want to do?"

class askControl:

	def __init__():
		pass
	
	def mainLoop():
		opts = {"Invest": "I", "Banks": "B", "Wait":"W", "Stats":"S", "Settings":"X", "Exit":"E"}
		return ask(whatDo, "Option = Action.", True, True, **opts)

	def bank():
		opts = {"Details": "D", "Change Bank": "C", "Exit": "E"}
		return ask(whatDo, "", False, True, **opts)

	def bankTwo():
		opts = {"Join Bank": "J", "Next Bank": "N", "Exit": "E"}
		return ask(whatDo, "", False, True, **opts)

	def wait():
		opts = {"Sleep till 8:00": "S"}
		return ask(whatDo, "", False, True, **opts)


################################################################################################################################

# Money

added = 0;
used = 0;

class moneyControl:

	def add(x):
		global money
		money += x
		added += x

	def subtract(x):
		global money
		money -= x
		used += x

################################################################################################################################

# Wait

def wait():
	global day
	global hour
	
	option = askControl.wait()
	
	match option:
		case "S":
			print("Sleeping", end="", flush=True)
			sleep(0.3)
			print(".", end="", flush=True)
			sleep(0.3)
			print(".", end="", flush=True)
			sleep(0.3)
			print(".")
			
			day += 1
			hour = 8
			
################################################################################################################################

# Banks

class bank:
	def __init__(self, name, desc, joinFee, maxCredit, maxMoney):
		self.name = name
		self.joinFee = joinFee
		self.maxCredit = maxCredit
		self.maxBalance = maxMoney
		self.description = desc

bankList = [
	bank("Pirate's Bank", "Hey matey? Have a bit o' gold ya want to keep safe? Well then you're in big luck! Pirate's Bank is open for ya matey! Arrrrrr!!", 0, 400, 1000),
	bank("Meow Bank", "Meow meow meow! Meow meow. Mreaaaawww! Meow meow meoow? Meow!", 500, 1000, 5000),
	bank("Bank of Trolls", "What did you say again? (x42)", 2050, 10000, 100000),
	bank("Bank Chicken", "n cfnfcv,mdkswedkmrejkwse,rjiw3ujrfkmesjndmke=snjwhemk", 5773, 2323, 8579),
	bank("Ultimatum", "For millionares!", 5000, 25000, 1000000000000000)
]
cBank = 0
bankObj = bankList[cBank]


def banks():
	
	global money
	global bankObj
	global cBank
	
	print(f"Current bank: {bankList[cBank].name}") # Print current bank stats
	print(f"Balance: ${money}")
	
	while True: # Menu
	
		option = askControl.bank() # Ask
		line(50)
		
		match option:
			
			case "E": # Exit
				return
			
			case "D": # Details
				line(20)
				print(f"Bank: {bankObj.name}")					# Details
				print(f"Description: ${bankObj.description}")
				print(f"Maximum credit: ${bankObj.maxCredit}")
				print(f"Max balace: ${bankObj.maxBalance}")
				line(20)
			
			case "C":	# Change Bank
	
				if cBank+1 == len(bankList): # If final bank
					print("Sorry, this is the final bank")
					line(69)
				else:
					skipped = False
					i = 0
					
					while True:
						i += 1
						nextBank = bankList[cBank+i]
					
						if not skipped: # To beatify
							print("\nNext bank:")
							print(f"Name: {nextBank.name}")
							print(f"Description: {nextBank.description}")
							print(f"Joining Fee: ${nextBank.joinFee}")
							print(f"Max Balance: ${nextBank.maxBalance}")
							print(f"Max Credit: ${nextBank.maxCredit}\n")
					
						option = askControl.bankTwo() # Ask as well
						skipped = False
						
						match option: # Menu
						
							case "N": # Next bank
								if cBank+i+1 == len(bankList):
									line(50)
									print("Sorry, this is the final bank")
									line(50)
									i -= 1
									skipped = True
								else:
									continue
								
							case "J": # Join
							
								if nextBank.joinFee <= money:
									cBank += i
									bankObj = nextBank
									money -= nextBank.joinFee
									line(15)
									print("\nBank joined!\n")
									line(15)
									break
								else:
									line(25)
									print("Not enough money!")
									line(25)
									break
								
							case "E": # Exit
								break
							
################################################################################################################################

# Stats

def stats():
	print(f"Day: {day}\nMoney: ${money}\nTotal money earned: ${added}\nTotal money used: ${used}")

################################################################################################################################

#Tutorial
def tutorial():
	print("===Work=In=Progress===(tutorial)")

################################################################################################################################

### Main Game Loop ###
exit = False
def main_game():
	global exit
	
	while True:
		if exit:
			break
		
		line(69)
		print(f"Day {day}\nHour {hour}\nMoney: ${money}")
		option = askControl.mainLoop()
		
		match option:
			case "E":
				exit = True
			case "B":
				line(69)
				banks()
			case "S":
				line(69)
				stats()
			case "W":
				line(69)
				wait()
			

################################################################################################################################

##Beginning##

# Game mode select
gamemode_obj = {"Very Easy":gveasy, "Easy":geasy, "Medium":gmed, "Hard":ghard, "Very Hard":gvhard, "Brutal":gbrut}
gamemode = ask("Pick gamemode: ", "Easier gamemodes have more starting money and less goals. Very easy is reccomended for first-timers.", **gamemode_obj)

#Game mode setup
gname = gamemode.name
goal = gamemode.goal
gstart = gamemode.start
gadv = gamemode.advanced

money = gstart
if gadv: var = "On"
else: var = "Off"

ginit_dict = {"\nName: ":gname, "Starting Money: $":gstart, "Goal: $":goal, "Advanced Mode: ":var}

for item in list(ginit_dict.keys()):
	sleep(0.25)
	print(item, end='')
	print(str(ginit_dict[item])+"\n")
sleep(0.25)

if ask("Do you want a tutorial?", False, Yes=True, No=False):
	tutorial()
else:
	main_game()
main_game()
