# By Leo-MathGuy
# You can copy this code if you don't sell it, attribute it to me, and share it with this same licence.

"""
Code order:

Line function
Gamemode
Ask
Ask control
Banks
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

def ask(q, h,  help=True, **kwargs):  #Universal ask function. Provide quesiton, help, and kwargs as option:return
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

################################################################################################################################

whatDo = "What do you want to do?"

class askControl:
	def __init__():
		pass
	
	def mainLoop():
		opts = {"Invest": "I", "Banks": "B", "Wait":"W", "Stats":"S", "Settings":"X", "Exit":"E"}
		return ask(whatDo, "Option = Action. You do not need to capitaliaze", **opts)
	def bank():
		opts = {"Details": "D", "Change Bank": "C", "Exit": "E"}
		return ask(whatDo, "", False, **opts)
	def bankTwo():
		opts = {"Join Bank": "J", "Next Bank": "N", "Exit": "E"}
		return ask(whatDo, "", False, **opts)


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
	bank("Meow Bank", "Meow meow meow! Meow meow. Mreaaaawww! Meow meow meoow? Meow!", 15, 1000, 5000)
]
cBank = 0
bankObj = bankList[cBank]


def banks():
	global money
	global bankObj
	global cBank
	
	print(f"Current bank: {bankList[cBank].name}")
	print(f"Balance: {money}")
	while True:
		option = askControl.bank()
		line(50)
		match option:
			case "E":
				return
			case "D":
				line(20)
				print(f"Bank: {bankObj.name}")
				print(f"Description: {bankObj.description}")
				print(f"Maximum credit: {bankObj.maxCredit}")
				print(f"Max balace: {bankObj.maxBalance}")
				line(20)
			case "C":
				if cBank+1 == len(bankList):
					print("Sorry, this is the final bank")
					line(69)
				else:
					skipped = False
					i = 0
					while True:
						i += 1
						nextBank = bankList[cBank+i]
						if not skipped:
							print("\nNext bank:")
							print(f"Name: {nextBank.name}")
							print(f"Description: {nextBank.description}")
							print(f"Joining Fee: {nextBank.joinFee}")
							print(f"Max Balance: {nextBank.maxBalance}")
							print(f"Max Credit: {nextBank.maxCredit}\n")
						option = askControl.bankTwo()
						skipped = False
						match option:
							case "N":
								if cBank+i+1 == len(bankList):
									line(50)
									print("Sorry, this is the final bank")
									line(50)
									i -= 1
									skipped = True
								else:
									continue
							case "J":
								if nextBank.joinFee <= money:
									cBank += i
									bankObj = nextBank
									money -= nextBank.joinFee
									line(15)
									print("\nBank joined!\n")
									line(15)
									break
							case "E":
								break

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
		print(f"Day {day}\nMoney: {money}")
		option = askControl.mainLoop()
		
		if option == "E":
			exit = True
		elif option == "B":
			line(69)
			banks()

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

ginit_dict = {"Name: ":gname, "Starting Money: $":gstart, "Goal: $":goal, "Advanced Mode: ":var}

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