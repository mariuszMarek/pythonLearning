import subprocess, sys
import pyautogui
import pyperclip
import time
import pynput

from ManagaSettings import ManageSettings
from MakeScreenshot import MakeScreenshot
from cmdInterface import prep_cmd
prep_cmd() # check for commands

# powershellVirtualAndroidScript = "F:\\memu\\runemucMultipleTimes.ps1"
# subprocess.Popen(["powershell", powershellVirtualAndroidScript])
# bede uruchamial proces po procesie

prep_cmd()

# pyautogui.moveTo(450, 450, duration=1.0)
num = 0
# mogę sobie nagrać pozycje gdzie klikałem a potem te liczby wykorzystać przy programowaniu, czyli plik ini ?
while ( num < 100 ):
    
    # print ("To jest pozycja kursora x->{} i y-> {}".format(*pyautogui.position())) # nie aktualne 
    time.sleep(2)
    num = num + 1

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
