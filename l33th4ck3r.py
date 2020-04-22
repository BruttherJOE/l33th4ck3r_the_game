import cmd
import sys
import time
import os

###########
# imports #
###########

cls = lambda: os.system('cls') 
#The “lambda” keyword in Python is used to define anonymous functions. 
#These functions are also called as lambda functions.

###############
# globalfuncs #
###############

#### player init ####
class player:
    def __init__(self):
        self.name = ''
        self.location = ''
player = player() #this calls the class player to init player with these values

#### unused TITLE SCREEN ####
def title_screen_options():
    option = input("> ")
    if option.lower() == ("play"):
        game_setup()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ["play", "quit"]:
        # if input isnt in options presented in the list then remind them
        print("Please enter a valid command")
def title_screen():
    os.system(cls)
    print("welcome to my rpg")
    print("- play- ")
    print("- Help -")
    print("- Quit -")
    title_screen_options()
####### unused ######




def game_intro():
    cls()
    question0 = ". . . . . .\n"
    for character in question0:
    	sys.stdout.write(character)
    	sys.stdout.flush() #flushes buffer(memory of qn1) to terminal
    	time.sleep(0.08) #delay btwn each character
    question1 = "Mysterious guy : Hello there, what is your name?\n"
    for character in question1:
		#This will occur throughout the intro code.  
        #It allows the string to be typed gradually - like a typerwriter effect.
    	sys.stdout.write(character)
    	sys.stdout.flush() #flushes buffer(memory of qn1) to terminal
    	time.sleep(0.03) #delay btwn each character
    player_name = input("> ")
    player.name = player_name

    question2 = "Mysterious guy : " + player_name + ", I have heard of your l33t h4ck3r sk1llz and I am in need of your services.\n"
    question3 = "Mysterious guy : Please. . .\n"
    question4 = "Mysterious guy : Please help me hack into the school's wifi network and change my DW grades.\n"
    question5 = "Mysterious guy : I promise you . . . a large sum of money.\n"
    for character in question2:
    	sys.stdout.write(character)
    	sys.stdout.flush() #flushes buffer(memory of qn1) to terminal
    	time.sleep(0.03) #delay btwn each character
    for character in question3:
    	sys.stdout.write(character)
    	sys.stdout.flush() #flushes buffer(memory of qn1) to terminal
    	time.sleep(0.1) #delay btwn each character
    for character in question4:
    	sys.stdout.write(character)
    	sys.stdout.flush() #flushes buffer(memory of qn1) to terminal
    	time.sleep(0.03) #delay btwn each character 
    for character in question5:
    	sys.stdout.write(character)
    	sys.stdout.flush() #flushes buffer(memory of qn1) to terminal
    	time.sleep(0.08) #delay btwn each character 

    time.sleep(2)
    cls()
    answer = input("Type 'terminal' to begin\n> ")
    if answer.lower().strip() == "terminal":
        maingame()
    while answer != "terminal":#goes into infinite loop
        print("unknown command")
        answer = input("> ")

        if answer == "terminal":
            maingame() #calls the main game
#game intro is done

def maingame():
    print("type help to access basic help functions")
    answer = input("Type 'terminal' to begin\n> ")
    if answer.lower().strip() == "terminal":
        terminal_boot() #def terminal boot here
    while answer != "terminal":#goes into infinite loop
        print("unknown command")
        answer = input("> ")
        if answer == "terminal":
            terminal_boot() 
#maingame could be not done yet, but probably done


def terminal_boot():
    s1 = ("loading. . .\n")
    s2 = ("Starting NVIDIA Persistence Daemon...\nStarting LSB...\nStarting Disk Manager...\nStarting WPA Supplicant\nStarted NVIDIA Persistence Daemon...\nStarting OpenSSH...\nStarted LSB...\nStarted Disk Manager...\nStarted WPA Supplicant\nStarted OpenSSH...\n\n")
    s3 = ("downloading updates. . .\n")
    s4 = (". . . . . . . . . .\n")
    s5 = ("installing updates. . .\n")
    loadbar = ("■■■■■■■■■■■■■■■■■■■\n")
    for character in s1:
    	sys.stdout.write(character)
    	sys.stdout.flush() #flushes buffer(memory of qn1) to terminal
    	time.sleep(0.05) #delay btwn each character
    
    for character in s2:
    	sys.stdout.write(character)
    	sys.stdout.flush() #flushes buffer(memory of qn1) to terminal
    	time.sleep(0.01) #delay btwn each character

    for character in s3:
    	sys.stdout.write(character)
    	sys.stdout.flush() #flushes buffer(memory of qn1) to terminal
    	time.sleep(0.03) #delay btwn each character

    for character in s4:
    	sys.stdout.write(character)
    	sys.stdout.flush() #flushes buffer(memory of qn1) to terminal
    	time.sleep(0.2) #delay btwn each character

    for character in loadbar:
    	sys.stdout.write(character)
    	sys.stdout.flush() #flushes buffer(memory of qn1) to terminal
    	time.sleep(0.2) #delay btwn each character

    for character in loadbar:
    	sys.stdout.write(character)
    	sys.stdout.flush() #flushes buffer(memory of qn1) to terminal
    	time.sleep(0.03) #delay btwn each character

    for character in s5:
    	sys.stdout.write(character)
    	sys.stdout.flush() #flushes buffer(memory of qn1) to terminal
    	time.sleep(0.03) #delay btwn each character

    for character in loadbar:
    	sys.stdout.write(character)
    	sys.stdout.flush() #flushes buffer(memory of qn1) to terminal
    	time.sleep(0.03) #delay btwn each character

    print("Copyright @BruttherJOE 2020")
    print("Terminal Loaded")
    time.sleep(4)
    cls()
    terminal_function()
#terminal boot sequence complete

def terminal_function(): 
    player.name = "vegeta"
    player.location = ("C:\ " + player.name + "\ ")

    answer = input(player.location + "> ")
    if answer.lower().strip() == "ls":#primary loop
        print("desktop\npictures")
        terminal_function()
    if answer.lower() == "cd desktop":
        player.location += "desktop"
        desktop()
        
    while answer not in ["ls","cd desktop"]:#secondary loop
        print(answer + " is not recognised as an internal or external command, operable program, or batch file")
        answer = input(player.location + "> ")
        if answer.lower().strip() == "ls":
            print("desktop\npictures")
            terminal_function()
        if answer.lower() == "cd desktop":
            player.location += "desktop"
            desktop()

def desktop():
    #print("i am the desktop")
    #print (player.location + "> ")
    answer = input(player.location + "> ")
    if answer.lower().strip() == "ls":#primary loop
        print("Medium Orbit Ion Cannon.exe\nDw game project.py")
        desktop()#### below undone
    if answer.lower() == "cd ~":
        player.location += "desktop"
        desktop()
        
    while answer not in ["ls","cd desktop"]:#secondary loop
        print(answer + " is not recognised as an internal or external command, operable program, or batch file")
        answer = input(player.location + "> ")
        if answer.lower().strip() == "ls":
            print("desktop\npictures")
            desktop()
        if answer.lower() == "cd desktop":
            player.location += "desktop"
            desktop()
    






def help():
    print("")
    #these will be console commands before virtual terminal is launch

def helpcmd():
    print("cd  -  change directory\n nano  -  open text editor")
    
    



















###################################################
answer = input("would u like to warp to terminal function? (yes/no)")

if answer.lower().strip() == "yes": 
    #this removes all the spaces at the end and also changes caps to lowercase
    #this also applies lower() and strip() to answer
    #maingame() #use this to shortcut call maingame
    game_intro()
    #terminal_function()
 #   answer = input("you reach a xroad left or right").lower().strip()
  #  if answer == "left":
    #    game_intro() #calls game fn

 #   elif answer == "right":
   #     pass

 #   while answer not in ["left","right"]:#goes into infinite loop
    #    print("please input either left or right")
    #    answer = input("> ")

    #    if answer == "left":
        #    game_intro() #calls game fn

    #    elif answer == "right":
    #        pass
###########################################
else:
    print("thats too bad")









