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
        self.oka_ddossed = False
player = player() #this calls the class player to init player with these values

#### unused TITLE SCREEN content ####
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
    cls()
    print("welcome")
    print("- play- ")
    print("- Help -")
    print("- Quit -")

####### unused ######

def game_intro():
    cls()
    question0 = ". . . . . .\n\n"
    delay_print_01(question0)
    
    question1 = "Mysterious guy : Hello there, what is your name?\n"
    delay_print_3(question1)
	#This occurs throughout the entire game.  
    #It allows the string to be typed gradually - bearing a typerwriter effect. refer to def delay_print_3().

    player_name = input("> ")
    player.name = player_name

    question2 = "Mysterious guy : " + player_name + ", I have heard of your l33t h4ck3r sk1llz and I am in need of your services.\n"
    question25= "Mysterious guy : Please, call me Keith. "
    question3 = "\nKeith : And Please. . .\n"
    question4 = "Keith : Please help me hack into the school's wifi network and change my DW grades to an 'A'.\n"
    question5 = "Keith : I promise you . . . a large sum of money.\n\n"

    delay_print_3(question2)
    delay_print_3(question25)
    delay_print_01(question3)
    delay_print_3(question4)

    for character in question5:
    	sys.stdout.write(character)
    	sys.stdout.flush() #flushes buffer(memory of qn1) to terminal
    	time.sleep(0.1) #delay btwn each character 

    os.system('pause')
    cls()
    answer = input("Type 'terminal' to begin\n> ")
    if answer.lower().strip() == "terminal":
        terminal_boot()
    while answer != "terminal":#goes into infinite loop
        print("unknown command.")
        answer = input("> ")

        if answer == "terminal":
            terminal_boot() #calls the main game
#game intro is done

def terminal_boot():
    s1 = ("loading. . .\n\n")
    s2 = ("Starting NVIDIA Persistence Daemon...\nStarting LSB...\nStarting Disk Manager...\nStarting WPA Supplicant\nStarted NVIDIA Persistence Daemon...\nStarting OpenSSH...\nStarted LSB...\nStarted Disk Manager...\nStarted WPA Supplicant\nStarted OpenSSH...\n\n")
    s3 = ("downloading updates. . .\n")
    s4 = (". . . . . . . . . .\n")
    s5 = ("installing updates. . .\n")
    loadbar = ("■■■■■■■■■■■■■■■■■■■\n")

    delay_print_5(s1)
    for character in s2:
    	sys.stdout.write(character)
    	sys.stdout.flush() #flushes buffer(memory of qn1) to terminal
    	time.sleep(0.01) #delay btwn each character
    delay_print_3(s3)
    delay_print_02(s4)
    delay_print_02(loadbar)
    delay_print_3(loadbar)
    delay_print_3(s5)
    delay_print_3(loadbar)

    print("\n©Copyright @BruttherJOE 2020")
    print("Terminal Loaded\n")
    os.system('pause')
    cls()
    print("type 'help' to access basic help functions. \n'help' will be accessible almost everywhere.")
    terminal_function()
#terminal boot sequence complete

def terminal_function(): #undone : help functions. refer to help()

    #player.name = "vegeta" #placeholder for debugging
    player.location = ("C:\ " + player.name + "\ ")

    answer = input(player.location + "> ")
    if answer.lower().strip() == "ls":#primary loop
        print("desktop\npictures")
        terminal_function()
    if answer.lower() == "cd desktop":
        desktop()
    if answer.lower() == "cd pictures":
        pictures()
    if answer.lower() == "help":
        help()
        terminal_function()

    if answer.lower() == "ssh oka@192.168.1.1": #nested loop
        if player.oka_ddossed == False:
            print("\nYou should not attempt to ssh without ddos! It will be easy for authorities to catch you!\n")
            terminal_function()
        elif player.oka_ddossed == True:
            ssh_intro()
   
    while answer not in ["ls","cd desktop","cd pictures","help","ssh"]:#secondary loop
        print(answer + " is not recognised as an internal or external command, operable program, or batch file")
        answer = input(player.location + "> ")
        if answer.lower().strip() == "ls":#primary loop
            print("desktop\npictures")
            terminal_function()
        if answer.lower() == "cd desktop":
            desktop()
        if answer.lower() == "cd pictures":
            pictures()
        if answer.lower() == "help":
            help()
            terminal_function()
        if answer.lower() == "ssh": #nested loop
            if player.oka_ddossed == False:
                print("\nYou should not attempt to ssh without ddos! It will be easy for authorities to catch you!")
                terminal_function()
            elif player.oka_ddossed == True:
                ssh_intro()


def desktop():
    #print("i am the desktop")
    #print (player.location + "> ")
    player.location = ("C:\ " + player.name + "\desktop\ ")
    answer = input(player.location + "> ")
    if answer.lower().strip() == "ls":#primary loop
        print("moic.exe\nDW homework.ipynb\nhacknotes.txt")
        desktop()##to prevent prog from exit
    if answer.lower() == "cd ~":
        terminal_function()
    if answer.lower() == "moic.exe":
        moicload()
    if answer.lower() in ["nano hacknotes.txt","sudo nano hacknotes.txt"]:
        notes()
        
    while answer not in ["ls","cd ~","moic.exe","nano hacknotes.txt","sudo nano hacknotes.txt"]: #secondary loop
        print(answer + " is not recognised as an internal or external command, operable program, or batch file")
        answer = input(player.location + "> ")
        if answer.lower().strip() == "ls":#primary loop
            print("moic.exe\nDw game project.py")
            desktop()##to prevent prog from exit
        if answer.lower() == "cd ~":
            terminal_function()
        if answer.lower() == "moic.exe":
            moicload()
        if answer.lower() in ["nano hacknotes.txt","sudo nano hacknotes.txt"]:
            notes()

def pictures():
    player.location = ("C:\ " + player.name + "\pictures\ ")
    answer = input(player.location + "> ")
    if answer.lower().strip() == "ls":#primary loop
        print("naked.jpg")
        pictures() ## this loop is to prevent the program from exiting
    if answer.lower() == "cd ~":
        terminal_function()
    if answer.lower() == "naked.jpg":
        print("Congratulations! you have found the easter egg.")
        print("But you are a pervert, so let that sink in.")
        pictures()
    if answer.lower().strip() == "help":
        help()
        pictures()

    while answer not in ["ls","cd ~","naked.jpg"]:#secondary loop
        print(answer + " is not recognised as an internal or external command, operable program, or batch file")
        answer = input(player.location + "> ")
        if answer.lower().strip() == "ls":#primary loop
            print("naked.jpg")
            pictures() ## this loop is to prevent the program from exiting
        if answer.lower() == "cd ~":
            terminal_function()
        if answer.lower() == "naked.jpg":
            print("Congratulations! you have found the easter egg.")
            print("But you are a pervert, so let that sink in.")
            pictures()
        if answer.lower().strip() == "help":
            help()
            pictures()
#pictures are complete

def moicload():
    cls()
    loadbar = ("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\nMOIC Loaded. \n© 2020 all rights reserved.\n")
    disclaimer = ("\nThere are inherent dangers in the use of any software, and you are solely responsible for your own actions.")
    delay_print_5(loadbar)
    print(disclaimer)
    moic()

def moic():
    player.location = ("// MOIC > ")
    moichelp = ("\ntype 'help' to access MOIC commands.\ntype 'z' to exit program.\n")
    print (moichelp)
    #
    answer = input(player.location)
    if answer.lower().strip() == "help":#primary loop
        cls()
        print("input 'ddos [ip address]' to attack and deny a target's services")
        os.system('pause')
        moic()

    if answer.lower() == "ddos 192.168.1.1":
        DDOSoka()

    if answer.lower().strip() == "z":#primary loop
        desktop()

    while answer not in ["help","ddos 192.168.1.1"]:#secondary loop
        print(answer + " is not recognised as a MOIC internal or external command")
        answer = input(player.location)
        if answer.lower().strip() == "help":#primary loop
            print("input 'ddos [ip address]' to attack and deny a target's services")
            os.system('pause')
            moic()

        if answer.lower() == "ddos 192.168.1.1":
            DDOSoka()

        if answer.lower().strip() == "z":#primary loop
            desktop()

def DDOSoka():
    networkestablishing = ("establishing network link. . .\n")
    #this is where u code the show of ddossing oka
    loadbar = ("■■■■■■■■■■■■■■■■■■■")
    network_est = ("\nnetwork link established . . .\nlink strength : 98%")
    attack = ("\nattacking network protocols. . .\n")
    ddos_msg = ("\n192.168.1.1 is successfully hit.")

    delay_print_3(networkestablishing)
    delay_print_02(loadbar)
    delay_print_3(loadbar)
    delay_print_3(network_est)
    time.sleep(2)
    delay_print_3(attack)
    time.sleep(2)
    print(ddos_msg)
    time.sleep(3)
    player.oka_ddossed = True
    After_oka_ddos_msg = ("Keith : Congratulations! level 1 complete. I knew you could do it. \nKeith : But it's only half the battle. \nKeith : Now, SSH into Oka's terminal and edit my grades.\n")
    cls()
    delay_print_3(After_oka_ddos_msg)
    moic()

def ssh_intro():
    print("login as: oka")
    answer = input("oka@192.168.1.1's password: ")
    if answer.lower().strip() == "iloveturtles":#primary loop
        time.sleep(2)
        oka_terminal()

    else:
        print("wrong password. connection refused.")
        terminal_function()

def oka_terminal():
    player.name = "oka" #you are now in oka terminal
    player.location = ("C:\ " + player.name + "\ ")

    answer = input(player.location + "> ")
    if answer.lower().strip() == "ls":#primary loop
        print("desktop\ndocuments")
        oka_terminal()
    if answer.lower() == "cd desktop":
        oka_desktop()
    if answer.lower() == "cd documents":
        oka_documents()
    if answer.lower() == "help":
        help()
        oka_terminal()
   
    while answer not in ["ls","cd desktop","cd documents","help",]:#secondary loop
        print(answer + " is not recognised as an internal or external command, operable program, or batch file")
        answer = input(player.location + "> ")
        if answer.lower().strip() == "ls":#primary loop
            print("desktop\ndocuments")
            oka_terminal()
        if answer.lower() == "cd desktop":
            oka_desktop()
        if answer.lower() == "cd documents":
            oka_documents()
        if answer.lower() == "help":
            help()
            oka_terminal()

def oka_desktop():
    player.location = ("C:\ " + player.name + "\desktop\ ")
    answer = input(player.location + "> ")
    if answer.lower().strip() == "ls":#primary loop
        print("minecraft.exe\ncyrille_password.txt")
        oka_desktop()##to prevent prog from exit
    if answer.lower() in ["nano cyrille_password.txt","sudo nano cyrille_password.txt"]:
        print("\nreserved for level 3. A work in progress. This is not where you beat level 2. Shoo!\n")
        oka_desktop()
    if answer.lower() == "cd ~":
        oka_terminal()
        
    while answer not in ["ls","cd ~","nano cyrille_password.txt","sudo nano cyrille_password.txt"]: #secondary loop
        print(answer + " is not recognised as an internal or external command, operable program, or batch file")
        answer = input(player.location + "> ")
        if answer.lower().strip() == "ls":#primary loop
            print("minecraft.exe\ncyrille_password.txt")
            oka_desktop()##to prevent prog from exit
        if answer.lower() in ["nano cyrille_password.txt","sudo nano cyrille_password.txt"]:
            print("\nreserved for level 3. A work in progress.\n")
            oka_desktop()
        if answer.lower() == "cd ~":
            oka_terminal()
#done

def oka_documents():
    player.location = ("C:\ " + player.name + "\documents\ ")
    answer = input(player.location + "> ")
    if answer.lower().strip() == "ls":#primary loop
        print("oka.jpg\ndw_grades.txt")
        oka_documents() ## this loop is to prevent the program from exiting
    if answer.lower() == "cd ~":
        oka_terminal()
    if answer.lower() == "sudo nano dw_grades.txt":
        dw_grades()
                    
    if answer.lower().strip() == "help":
        help()
        oka_documents()

    while answer not in ["ls","cd ~","sudo nano DW_grades.txt"]:#secondary loop
        print(answer + " is not recognised as an internal or external command, operable program, or batch file")
        answer = input(player.location + "> ")
        if answer.lower().strip() == "ls":#primary loop
            print("oka.jpg\ndw_grades.txt")
            oka_documents() ## this loop is to prevent the program from exiting
        if answer.lower() == "cd ~":
            oka_terminal()
        if answer.lower() == "sudo nano dw_grades.txt":
            dw_grades()

def dw_grades():
    cls()
    player.location = ("C:\ " + player.name + "\documents\dw_grades.txt\ ")
    print("Joe - C")
    print("Dino - B")
    print("Calvin - A")
    print("Jack - B")
    print("Keith - C")
    print("Overwrite : Keith - A ---------------(y/n?)")

    ans2 = input(player.location + "> ")
    if ans2.lower().strip() == "y":
        roll_credits()
    if ans2.lower().strip() == "n":
        oka_documents()
    while ans2 not in ["y","n"]:#secondary loop
        print(ans2 + " is not recognised as an internal or external command.")
        ans2 = input(player.location + "> ")
        if ans2.lower().strip() == "y":
            roll_credits()
        if ans2.lower().strip() == "n":
            oka_documents()






###############################################################################

def notes(): #nano in to view
    #player.name = "vegeta" #debug
    cls()
    print(player.name + "'s hacking notes")
    print("\nMOIC - 'Medium Orbit Ion Cannon'. The purpose of this program is to DDOS an individual.")
    print("MOIC is a denial-of-service attack application designed to attack as many as 256 URLs at the same time.\n")
    print("To successfully hack someone, FIRST deny service of their internet by DDOSing them,")
    print("THEN SSH into their computer and you can then change their files amidst the chaos.")
    print("\nOn actual terminals, ctrl+z to stop, and ctrl+x to save and exit. Here, it is x or z")
    print("\nI have observed Oka's actions for some time, \nand the ip address that Oka's computer is currently using is 192.168.1.1")
    print("His password is 'iloveturtles'")
    print("\n\nFor level 2: to SSH, type SSH [username]@[ip address] in the home directory.\n")

    player.location = ("C:\ " + player.name + "\desktop\hacknotes\ ")
    answer = input(player.location + "> ")
    if answer.lower().strip() in ["z","x"]:#primary loop
        cls()
        desktop()

    while answer not in ["z"]:#secondary loop
        print(answer + " is not recognised as a command. try exiting first?")
        answer = input(player.location + "> ")
        if answer.lower().strip() in ["z","x"]:
            cls()
            desktop()
#mypersonal hacking notes on desktop


def help():
    cls()
    print("ls: The ls command will show you aka 'list' the files in your current directory.\n")
    print("cd: The cd command will allow you to change directories.\n    When you open a terminal you will be in your home directory. \n    To move around the file system you will use cd. ")
    print("    For example, \n    To navigate into home directory, use 'cd ~'. \n    To navigate to desktop, use 'cd desktop'.")
    print("    To open .txt files, we use the command 'nano [filename]'. \n    For example, if there is a file called DW.txt, we do 'nano DW.txt' or 'sudo nano DW.txt'.")
    print("\napps: To open .exe or .jpg or any other misc files, you do [filename].[extension].\n      For example : if there is man.jpg, do man.jpg to open the picture.")
    print("\nSudo : Sudo stands for superuser do. it gives you admin priveleges such that you can edit text files.")
    print("\nDDOS - distributed denial of service. Floods target with unwanted traffic such that it cannot function.")
    print("\nFor level 2: to SSH, type SSH [username]@[ip address] in the home directory.\n")
    print("SSH - secure shell. Allows you to remotely and securely access computers over the wifi. Do not attempt to SSH without DDOS! ")
    os.system('pause') #press any key to continue. this is in the os package.
    cls()
    


#### DELAY PRINTERS ####
# delay printers delays print such that i dont have to keep writing same thing
def delay_print_5(string): 
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

def delay_print_3(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

def delay_print_02(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)

def delay_print_01(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

##############################
#### CREDITS #################
##############################

def roll_credits():
    cls()
    credit1 = ("\nCongratulations! \n\nYou have successfully beat the game and earned 50 gold from Keith.\n")
    credit3 = ("I have learnt a lot from writing this game.\n")
    credit2 = ("Thank you for playing my game. \n\nI took a really long time to make it, and things got really confusing sometimes.\n")
    credit4 = ("I hope that from this game, you will be more intrigued to learn linux shell.\n\n")

    delay_print_3(credit1)
    delay_print_3(credit2)
    delay_print_3(credit3)
    delay_print_3(credit4)
    sys.exit()
##############################





################### MAIN GAME LOOP#################
###################################################
answer = input("would you like to play my game? (yes/no)")

if answer.lower().strip() == "yes": 
    #this removes all the spaces at the end and also changes caps to lowercase
    #this also applies lower() and strip() to answer
    #all debugging shit below

    #dw_grades()
    
    #oka_terminal()
    #roll_credits()
    #ssh_intro()
    #help()
    #notes()
    #DDOSoka()

    #terminal_function()
    #maingame() #use this to shortcut call maingame
    game_intro() #for the full game
    #moicload()
 
else:
    print("another day, maybe?")

#####################################################







