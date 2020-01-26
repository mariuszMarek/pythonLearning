import subprocess
import sys
import pyautogui
import pyperclip
import time
import pynput

import win32gui
from MakeScreenshot import MakeScreenshot
from ManagaSettings import ManageSettings
from cmdInterface import prep_cmd
from passcodeFinder import ParsEmail
prep_cmd()  # to raczej potrzebne do glownego programu, ten plik bedzie podprogramem
RecordStep = False  # to powinno byc brane z parametrów ale na razie będzie tak na sztywno

#most of those should be taken from the parser
NUM_OF_INSTACE      = 1
MEMUC_EXE           = 'F:\\Program Files\\memu\\MEmu\\memuc.exe'
QUINDAN_APP         = "F:\\memu\\base.apk"
INVITE_CODE         = "il6MzssI"
GENERIC_PASS        = "Test123456"
LIST_OF_EMAILS      = "F:\\memu\\listOfMyEmails.txt"
EMAIL_FROM          = "Webnovel <noreply@webnovel.com>"
WINDOW_NAME         = "Memu"
SUBJECT_TO_FIND     = "Activate your Webnovel account"
MAX_NUM_OF_TRIES    = 5
HARDCODED_PASS      = "PythonAutomate12#"  # bedzie brane z parametru
PROGRAM_NAME        = "Webnovel"
LOAD_ALL            = True

# need to update this with method to record steps
ListOfSteps     = ManageSettings(RecordStep)
sequence_num    = 0
lines_of_emails = open(LIST_OF_EMAILS, 'r').readlines()
email_parser    = ParsEmail()
for_instances   = list(range(0, NUM_OF_INSTACE))
Steps_to_do     = ListOfSteps.save_or_load(LOAD_ALL, sequence_num)

for num in for_instances:
    successfull_email    = True
    email_to_use         = lines_of_emails[num].strip()
    passcode             = ""
    emulator_index       = 0
    num_of_tries         = 0

    subprocess.Popen([MEMUC_EXE, "remove", "-i",
                      "{}".format(emulator_index)]).wait()
    subprocess.Popen([MEMUC_EXE, "create", "51"]).wait()

    subprocess.Popen([MEMUC_EXE, "setconfig", "-i",
                      "{}".format(emulator_index), "cpus", "4"]).wait()
    subprocess.Popen([MEMUC_EXE, "setconfig", "-i",
                      "{}".format(emulator_index), "memory", "2048"]).wait()
    subprocess.Popen([MEMUC_EXE, "setconfig", "-i",
                      "{}".format(emulator_index), "turbo_mode", "1"]).wait()
    subprocess.Popen([MEMUC_EXE, "setconfig", "-i",
                      "{}".format(emulator_index), "is_customed_resolution", "1"]).wait()
    subprocess.Popen([MEMUC_EXE, "setconfig", "-i",
                      "{}".format(emulator_index), "resolution_width", "720"]).wait()
    subprocess.Popen([MEMUC_EXE, "setconfig", "-i",
                      "{}".format(emulator_index), "resolution_height", "1280"]).wait()
    subprocess.Popen(
        [MEMUC_EXE, "start", "-i", "{}".format(emulator_index)]).wait()
    Whandle = win32gui.FindWindow(None, WINDOW_NAME)
    # na wrazie czego, tutaj chyba trzeba try: catch jak chińskie gówno się włączy
    win32gui.SetForegroundWindow(Whandle)
    print("Wait 1 min for program to start")
    time.sleep(60)

    for sequences in Steps_to_do:        


        pyperclip.copy(email_to_use)   # for logi into google play        
        pyperclip.copy(HARDCODED_PASS) # for password into google play
        pyperclip.copy(PROGRAM_NAME)   # for looking the webnovel on google play        
        pyperclip.copy(email_to_use)   # for account creation in webnovel        
        print("wating for email with passcode")
        while not passcode:
            try:
                # this needs to be in a loop as i don't know how long it will take to recive the email
                passcode = email_parser.find_passcode(
                    EMAIL_FROM, email_to_use, SUBJECT_TO_FIND)
            except ConnectionAbortedError:  # reestablish the connecton
                email_parser = ParsEmail()
                passcode = email_parser.find_passcode(
                    EMAIL_FROM, email_to_use, SUBJECT_TO_FIND)
            # for now i'll trun this off
            # if(num_of_tries > MAX_NUM_OF_TRIES):
            #     successfull_email = False
            #     NUM_OF_INSTACE += 1
            #     for_instances.append(NUM_OF_INSTACE)
            num_of_tries += 1
            time.sleep(5)
            if not passcode:
                print("wating for email with passcode")
        
        pyperclip.copy(passcode)    # copy the passcode from email to the clippboard                
        pyperclip.copy(INVITE_CODE) # for submitting the invite        

subprocess.Popen([MEMUC_EXE, "stop", "-i", "{}".format(emulator_index)]).wait()
with open(LIST_OF_EMAILS, 'w') as exit_file:
    for index, lines in enumerate(lines_of_emails):
         if index >= NUM_OF_INSTACE:
             exit_file.write(lines)