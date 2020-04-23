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
        self.location = '' #location of a player
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
    player.name = "vegeta" #placeholder for debugging
    player.location = ("C:\ " + player.name + "\ ")

    answer = input(player.location + "> ")
    if answer.lower().strip() == "ls":#primary loop
        print("desktop\npictures")
        terminal_function()
    if answer.lower() == "cd desktop":
        desktop()
    if answer.lower() == "cd pictures":
        pictures()

        
    while answer not in ["ls","cd desktop","cd pictures"]:#secondary loop
        print(answer + " is not recognised as an internal or external command, operable program, or batch file")
        answer = input(player.location + "> ")
        if answer.lower().strip() == "ls":
            print("desktop\npictures")
            terminal_function()
        if answer.lower() == "cd desktop":
            player.location += "desktop"
            terminal_function()
        if answer.lower() == "cd pictures":
            player.location += "pictures"
            pictures()        

def desktop():
    #print("i am the desktop")
    #print (player.location + "> ")
    player.location = ("C:\ " + player.name + "\desktop\ ")
    answer = input(player.location + "> ")
    if answer.lower().strip() == "ls":#primary loop
        print("moic.exe\nDw game project.py")
        desktop()##to prevent prog from exit
    if answer.lower() == "cd ~":
        terminal_function()
    if answer.lower() == "moic.exe":
        moic()
        
    while answer not in ["ls","cd ~","moic.exe"]:#secondary loop
        print(answer + " is not recognised as an internal or external command, operable program, or batch file")
        answer = input(player.location + "> ")
        if answer.lower().strip() == "ls":
            print("moic.exe\nDw game project.py")
            desktop()
        if answer.lower() == "cd ~":
            terminal_function()
        if answer.lower() == "moic.exe":
            moic()

def pictures():
    player.location = ("C:\ " + player.name + "\pictures\ ")
    answer = input(player.location + "> ")
    if answer.lower().strip() == "ls":#primary loop
        print("naked.jpg")
        pictures() ## this loop is to prevent the program from exiting
    if answer.lower() == "cd ~":
        terminal_function()

    while answer not in ["ls","cd ~"]:#secondary loop
        print(answer + " is not recognised as an internal or external command, operable program, or batch file")
        answer = input(player.location + "> ")
        if answer.lower().strip() == "ls":
            print("naked.jpg")
            pictures()
        if answer.lower() == "cd ~":
            terminal_function()

def moic():
    cls()
    player.location = ("// MOIC > ")
    loadbar = ("■■■■■■■■■■■■■■■■■■■\nMOIC Loaded. \n2020 all rights reserved.\n")
    disclaimer = ("\nThere are inherent dangers in the use of any software, and you are solely responsible for your own actions.")
    moichelp = ("type 'help' to access MOIC commands.\ntype 'z' to exit program.")
    delay_print_5(loadbar)
    print(disclaimer)
    print (moichelp)
    #
    answer = input(player.location)
    if answer.lower().strip() == "help":#primary loop
        print("this is a help file placeholder")
    
    if answer.lower() == "ddos oka@192.168.1.1":
        DDOSoka()

    if answer.lower().strip() == "z":#primary loop
        desktop()

    while answer not in ["help","ddos oka@192.168.1.1"]:#secondary loop
        print(answer + " is not recognised as an internal or external command, operable program, or batch file")
        answer = input(player.location)
        if answer.lower().strip() == "help":#primary loop
            print("this is a help file placeholder")
    
        if answer.lower() == "ddos oka@192.168.1.1":
            DDOSoka()

        if answer.lower().strip() == "z":#primary loop
            desktop()

def DDOSoka():
    print("ahhh oka is ddossed")
    #this is where u code the show of ddossing oka




def ssh():
    pass






def help():
    print("")
    #these will be console commands before virtual terminal is launch

def notes(): #nano in to view
    cls()
    print("MOIC - 'Medium Orbit Ion Cannon'. The purpose of this program is to DDOS an individual.")
    print("MOIC is a denial-of-service attack application designed to attack as many as 256 URLs at the same time.\n")
    print("To successfully hack someone, FIRST deny service of their internet by DDOSing them,")
    print("THEN SSH into their computer and you can then change their files amidst the chaos.")
    #my personal hacking notes

def helpcmd():
    print("where x is location/directory/filename you want to open or go to,\n")
    print("cd x  -  change directory\n nano x  -  open text editor\n")

def helpmoic():
    #this is where you display the moic commands. it is invoked when help is typed
    pass



def delay_print_5(string): #this delays print such that dont have to keep writing same thing
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

















###################################################
answer = input("would u like to warp to moic? (yes/no)")

if answer.lower().strip() == "yes": 
    #this removes all the spaces at the end and also changes caps to lowercase
    #this also applies lower() and strip() to answer
    
    #terminal_function()
    #maingame() #use this to shortcut call maingame
    game_intro() #for the full game
    #moic()
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









