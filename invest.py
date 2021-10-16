# By Leo-MathGuy
# You can copy this code if you don't sell it, attribute it to me, and share it with this same licence.

from math import *
from time import sleep

# Beggining message
print("By Leo-MathGuy \n")
print("Welcome to the investment game! \n\n")

day = 1
money = 0

# Game Modes
class gamemode:
	def __init__(self, name, advanced, startmoney, goal):
		self.name = name
		self.advanced = False #Disabled for now
		self.start = startmoney
		self.goal = goal * 10000 #To avoid unnecessary 0s

# Things that start with a g before a word are linked to the gamemode
gveasy = gamemode("Very Easy", False, 250, 50)
geasy = gamemode("Easy", False, 150, 100)
gmed = gamemode("Medium", False, 100, 100)
ghard = gamemode("Hard", False, 75, 150)
gvhard = gamemode("Very Hard", True, 50, 200)
gbrut = gamemode("Brutal", True, 30, 500)

def ask(q, h,  help="True", **kwargs):  #Universal ask function. Provide quesiton, help, and kwargs as option:return
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
			if inpt in optionl:
				sleep(0.2)
				return kwargs[inpt]
			sleep(0.35)
			print("Error: Unknown Input. Please enter valid option\n")

whatDo = "What do you want to do?"

class askControl:
	def __init__():
		pass
	
	def mainLoop():
		opts = {"Invest": "I", "Banks": "B", "Wait":"W", "Stats":"S", "Settings":"X", "Exit":"E"}
		return ask(whatDo, "Option = Action", **opts)
	def bank():
		opts = {"Details": "D", "Change Bank": "C", "Exit": "E"}
		return ask(whatDo, "", False, **opts)
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
	print(f"Current bank: {bankList[cBank].name}")
	print(f"Balance: {money}")
	while True:
		option = askControl.bank()
		match option:
			case "E":
				return
			case "D":
				print("-" * 20)
				print(f"Bank: {bankObj.name}")
				print(f"Description: {bankObj.description}")
				print(f"Maximum credit: {bankObj.maxCredit}")
				print(f"Max balace: {bankObj.maxBalance}")
				print("-" * 20)
			case "C":
				print("Work In Progress")
#Tutorial
def tutorial():
	print("===Work=In=Progress===(tutorial)")

### Main Game Loop ###
def main_game():
	while True:
		print("-" * 69)
		print(f"Day {day}\nMoney: {money}")
		option = askControl.mainLoop()
		if option == "E":
			break
		elif option == "B":
			banks()

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
sleep(0.25)
print("\n")
for item in list(ginit_dict.keys()):
	sleep(0.25)
	print(item, end='')
	print(str(ginit_dict[item])+"\n")
sleep(0.25)

if ask("Do you want a tutorial?", "y = begin tutorial  n = skip tutorial", y=True, n=False):
	tutorial()
else:
	main_game()
