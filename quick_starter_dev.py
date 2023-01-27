#Welcome to the source code of the quick_starter!
#Feel free to fork or modify this code!
#But please credit us :3

#MODULES
import os
import time

#Customization
os.system("title Quick Starter (PYTHON EDITION)")
os.system("color 9")


#OTHER VARIABLES (NOT RECOMMENDED TO MODIFY THEM)
USER = os.getlogin()

#The text that you can see at the start
print ("[SYSTEM] Welcome to the Quick Starter by Blue Amethyst!")
print ("[SYSTEM] This is the Python Edition, if you're searching for the default edition, \n[SYSTEM] Check out https://github.com/BLUEAMETHYST-Studios/winutils !")
print ('[SYSTEM] Type "help" to list all commands!')
command = input("Input > ")

#ALL PROGRAM VARIABLES/DEFINITIONS ARE HERE
#IF THE PATHS TO THOSE PROGRAMS ARE DIFFERENT, YOU CAN MODIFY THEM HERE!
#BUT PLEASE BE AWARE THAT, THE CODE COULD BREAK BY MODIFYING THEM!
    
def startDiscord():
        os.startfile ("C:/Users/" + USER + "/AppData/Local/Discord/app-1.0.9010/Discord.exe")
        print("[SYSTEM/WARN] If you close the application, which you used to open Discord, Discord will also close.")
        print("[SYSTEM] Due to some little issues, you'll need to wait 15 seconds before you can execute another command.")
        time.sleep(15)
        command = input("Input > ")
    
def startSteam():
        os.startfile ("C:\Program Files (x86)\Steam\steam.exe")
        command = input("Input > ")

def startGoogle():
    os.startfile ("https://www.google.com")
    command = input("Input > ")

def startChrome():
    os.startfile ("C:\Program Files\Google\Chrome\Application\chrome.exe")
    command = input("Input > ")


#IF STATEMENTS AND OUTPUTS
#IT'S NOT RECOMMENDED TO MODIFY THOSE, BECAUSE THEN THE PROGRAM COULD BREAK!
#ONLY DO IT IF YOU ARE EXPERIENCED!

if command == "discord":
    startDiscord()
if command == "steam":
    startSteam()
if command == "google":
    startGoogle()
if command == "chrome":
    startChrome()
    
