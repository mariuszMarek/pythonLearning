import subprocess, sys
import pyautogui
import pyperclip
import time
import pynput

import win32gui

from ManagaSettings import ManageSettings
from MakeScreenshot import MakeScreenshot
from cmdInterface import prep_cmd
from passcodeFinder import ParsEmail

SCREENSHOT_SIZE = 300
NUM_OF_INSTACE = 1
prep_cmd() # jak to dzialalo ? xD do przypomnienia na później
RecordStep     = False  # to powinno byc brane z parametrów ale na razie będzie tak na sztywno
# RecordStep     = True  # to powinno byc brane z parametrów ale na razie będzie tak na sztywno


ListOfSteps     = ManageSettings(RecordStep) # need to update this with method to record steps
MEMUC_EXE       = 'F:\\Program Files\\memu\\MEmu\\memuc.exe'
QUINDAN_APP     = "F:\\memu\\base.apk"
INVITE_CODE     = "il6MzssI"
GENERIC_PASS    = "Test123456"
LIST_OF_EMAILS  = "F:\\memu\\listOfMyEmails.txt"
EMAIL_FROM      = "Webnovel <noreply@webnovel.com>"
WINDOW_NAME     = "Memu"
SUBJECT_TO_FIND = "Activate your Webnovel account"
# jednak potrzebuję mieć możliwość posiadania więcej niż jednej instrukcji na raz
# potrzebuje miec maila z pliku tekstowego, kod po wyslaniu maila
sequence_num    = 0
lines_of_emails = open(LIST_OF_EMAILS, 'r').readlines()
email_parser    = ParsEmail()
for num in range(0, NUM_OF_INSTACE):
    email_to_use   = lines_of_emails[num].strip()
    passcode       = ""
    emulator_index = 0
    
    
    
    subprocess.Popen([MEMUC_EXE, "remove", "-i", "{}".format(emulator_index)]).wait()
    subprocess.Popen([MEMUC_EXE, "create", "51"]).wait()
    subprocess.Popen([MEMUC_EXE, "setconfig" , "-i", "{}".format(emulator_index),"cpus","2"]).wait()
    subprocess.Popen([MEMUC_EXE, "setconfig" , "-i", "{}".format(emulator_index),"memory","2048"]).wait()
    subprocess.Popen([MEMUC_EXE, "setconfig" , "-i", "{}".format(emulator_index),"turbo_mode","0"]).wait()
    subprocess.Popen([MEMUC_EXE, "start"     , "-i", "{}".format(emulator_index)]).wait() # to gowno sie cos psuje, trudno pozostaje sleep

    Whandle = win32gui.FindWindow(None, WINDOW_NAME)
    win32gui.SetForegroundWindow(Whandle)  # na wrazie czego    
    
    subprocess.Popen([MEMUC_EXE, "adb"       , "-i", "{}".format(emulator_index),"shell","input","keyevent","3"]).wait()
    # time.sleep(1)
    subprocess.Popen([MEMUC_EXE, "adb"       , "-i", "{}".format(emulator_index),"install", "{}".format(QUINDAN_APP)]).wait() # moze tutaj zmienic na adb install path_to_apk ?
    # subprocess.Popen([MEMUC_EXE, "installapp", "-i", "{}".format(emulator_index),"{}".format(QUINDAN_APP)]).wait()

    
    pyperclip.copy(email_to_use)
    if RecordStep : print('start recording steps') # dodac to do klasy manageSetings
    posXY = ListOfSteps.save_or_load(sequence_num)
    ScreenShots = MakeScreenshot(posXY, SCREENSHOT_SIZE)
    ScreenShots.make_screensots()
    # omijaj pierwsza instancje jako że nagrywają się kroki wczesniej. Generalnie zrobie to specjalna klasa ktora to ogarnie, bedzie wygladalo to lepiej
    if RecordStep and num > 0:
        for posX,posY in posXY:
            pass
            #move the coursor and do the click
    else: # dla kazdego innego przypadku
        for posX, posY in posXY:
            #make the clicks
            pass
    sequence_num += 1
    print("will wait for email")
    while not passcode:
        passcode = email_parser.find_passcode(EMAIL_FROM, email_to_use,SUBJECT_TO_FIND) #this needs to be in a loop as i don't know how long it will take to recive the email
        print ("wating for email with passcode")
        #cos kurwa tutaj nie działa
        # po 3-5 razy bedzie musialo sie wylaczac bo prawdopodobnie mail przyszedł po chińsku, lel
        time.sleep(5)
    print ("recived passcode {}, start recording new instruction".format(passcode))
    #z hadrkodować wklepanie kodu zapraszającego jako input z klawiatury ?
    pyperclip.copy(passcode) # copy the passcode from email to the clippboard
    posXY = ListOfSteps.save_or_load(sequence_num) #another steps to do
    ScreenShots = MakeScreenshot(posXY, SCREENSHOT_SIZE)
    ScreenShots.make_screensots()

    if RecordStep and num > 0:
        for posX, posY in posXY:
            pass
            #move the coursor and do the click
    else:  # dla kazdego innego przypadku
        for posX, posY in posXY:
            #make the clicks
            pass
    time.sleep((60*60))
    #tutaj wylaczamy emulator by moc go zabic

with open(LIST_OF_EMAILS, 'w') as exit_file:
    for index, lines in enumerate(lines_of_emails):
         if index >= NUM_OF_INSTACE: exit_file.write(lines)


# pyautogui.moveTo(450, 450, duration=1.0)

# pyautogui.click()
# pyautogui.moveRel(None, 10)  # move mouse 10 pixels down
# pyautogui.doubleClick()
# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.
# pyautogui.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
# pyautogui.press('esc')
# pyautogui.keyDown('shift')
# pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
# pyautogui.keyUp('shift')
# pyautogui.hotkey('ctrl', 'c')
