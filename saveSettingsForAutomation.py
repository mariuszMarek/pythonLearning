import winsound
import subprocess, sys
import pyautogui
import pyperclip
import time
import pynput

import win32gui
from MakeScreenshot import MakeScreenshot
from ManagaSettings import ManageSettings
from cmdInterface import prep_cmd
from passcodeFinder import ParsEmail
prep_cmd() # jak to dzialalo ? xD do przypomnienia na później
RecordStep     = False  # to powinno byc brane z parametrów ale na razie będzie tak na sztywno
RecordStep     = True   # to powinno byc brane z parametrów ale na razie będzie tak na sztywno

#most of those should be taken from the parser
NUM_OF_INSTACE   = 1
MEMUC_EXE        = 'F:\\Program Files\\memu\\MEmu\\memuc.exe'
QUINDAN_APP      = "F:\\memu\\base.apk"
INVITE_CODE      = "il6MzssI"
GENERIC_PASS     = "Test123456"
LIST_OF_EMAILS   = "F:\\memu\\listOfMyEmails.txt"
EMAIL_FROM       = "Webnovel <noreply@webnovel.com>"
WINDOW_NAME      = "Memu"
SUBJECT_TO_FIND  = "Activate your Webnovel account"
MAX_NUM_OF_TRIES = 5
HARDCODED_PASS   = "PythonAutomate12#" # bedzie brane z parametru
PROGRAM_NAME     = "Webnovel"

ListOfSteps      = ManageSettings() # need to update this with method to record steps
sequence_num     = 0
lines_of_emails  = open(LIST_OF_EMAILS, 'r').readlines()
email_parser     = ParsEmail()
for_instances    = list(range(0, NUM_OF_INSTACE))
frequency        = 3500  # Set Frequency To 2500 Hertz
duration         = 500  # Set Duration To 1000 ms == 1 second
stop_button      = "alt_l"

for num in for_instances:
    print("star the memuc emulator")
    successfull_email = True
    email_to_use      = lines_of_emails[num].strip()
    passcode          = ""
    emulator_index    = 0
    num_of_tries      = 0
    
    subprocess.Popen([MEMUC_EXE, "remove", "-i", "{}".format(emulator_index)]).wait()
    subprocess.Popen([MEMUC_EXE, "create", "51"]).wait()

    subprocess.Popen([MEMUC_EXE, "setconfig", "-i", "{}".format(emulator_index),"cpus","4"]).wait()
    subprocess.Popen([MEMUC_EXE, "setconfig", "-i", "{}".format(emulator_index),"memory","2048"]).wait()
    subprocess.Popen([MEMUC_EXE, "setconfig", "-i", "{}".format(emulator_index),"turbo_mode","1"]).wait()
    subprocess.Popen([MEMUC_EXE, "setconfig", "-i", "{}".format(emulator_index),"is_customed_resolution", "1"]).wait()
    subprocess.Popen([MEMUC_EXE, "setconfig", "-i", "{}".format(emulator_index),"resolution_width", "720"]).wait()
    subprocess.Popen([MEMUC_EXE, "setconfig", "-i", "{}".format(emulator_index),"resolution_height", "1280"]).wait()

    subprocess.Popen([MEMUC_EXE, "start"    , "-i", "{}".format(emulator_index)]).wait() # to gowno sie cos psuje, trudno pozostaje sleep    
    Whandle = win32gui.FindWindow(None, WINDOW_NAME)
    try:
        win32gui.SetForegroundWindow(Whandle)  # na wrazie czego, tutaj chyba trzeba try: catch jak chińskie gówno się włączy
    except :
        pass    
    # print("Wait 50 s for program to start") 
    # time.sleep(50)
    winsound.Beep(frequency, duration)
    print("wczyta teraz emaila do uzycia {}".format(email_to_use))
    pyperclip.copy(email_to_use)
    if RecordStep : print('start recording steps') # dodac to do klasy manageSetings
    ListOfSteps.record_settings(sequence_num,stop_button)
    

    print("zapisalo pierwszy krok, teraz wczyta haslo do googla do schowka")
    pyperclip.copy(HARDCODED_PASS)
    sequence_num += 1
    ListOfSteps.record_settings(sequence_num,stop_button)
    
    # omijaj pierwsza instancje jako że nagrywają się kroki wczesniej. Generalnie zrobie to specjalna klasa ktora to ogarnie, bedzie wygladalo to lepiej bo aktualnie to chujowo    

    print("zapisalo kolejny krok, teraz skopiuje webnowel do schowka")
    pyperclip.copy(PROGRAM_NAME)
    sequence_num += 1
    ListOfSteps.record_settings(sequence_num,stop_button)
    
    print("zapisalo kojeny krok, teraz wklei emaila do schowka")
    pyperclip.copy(email_to_use)
    sequence_num += 1
    ListOfSteps.record_settings(sequence_num,stop_button)
    

    print ("wating for email with passcode")           
    while not passcode:
        try:
            passcode = email_parser.find_passcode(EMAIL_FROM, email_to_use,SUBJECT_TO_FIND) #this needs to be in a loop as i don't know how long it will take to recive the email
        except ConnectionAbortedError: #reestablish the connecton
            email_parser = ParsEmail()            
            passcode     = email_parser.find_passcode(EMAIL_FROM, email_to_use, SUBJECT_TO_FIND)
        # for now i'll trun this off
        # if(num_of_tries > MAX_NUM_OF_TRIES): 
        #     successfull_email = False         
        #     NUM_OF_INSTACE += 1
        #     for_instances.append(NUM_OF_INSTACE)
        num_of_tries += 1
        time.sleep(5)
        if not passcode :print("wating for email with passcode")

    print ("recived passcode {}, start recording new instruction".format(passcode))
    pyperclip.copy(passcode) # copy the passcode from email to the clippboard            
    sequence_num += 1
    ListOfSteps.record_settings(sequence_num,stop_button) # po wklejonym kodzie zapraszajacym jeszcze trzeba ogarnac wklejenie zaproszenai
    
    pyperclip.copy(INVITE_CODE)
    print("teraz kod zaprosenia do wklejenie")
    sequence_num += 1
    ListOfSteps.record_settings(sequence_num,stop_button) # po wklejonym kodzie zapraszajacym jeszcze trzeba ogarnac wklejenie zaproszenai
    


subprocess.Popen([MEMUC_EXE, "stop", "-i", "{}".format(emulator_index)]).wait()
try:
    subprocess.Popen([MEMUC_EXE, "remove", "-i", "{}".format(emulator_index)]).wait()
finally:
    subprocess.Popen([MEMUC_EXE, "remove", "-i", "{}".format(emulator_index)]).wait()

with open(LIST_OF_EMAILS, 'w') as exit_file:
    for index, lines in enumerate(lines_of_emails):
         if index >= NUM_OF_INSTACE: exit_file.write(lines)
