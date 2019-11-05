import subprocess, sys
import pyautogui
import pyperclip
import time
import pynput

import win32gui

from ManagaSettings import ManageSettings
from MakeScreenshot import MakeScreenshot
from cmdInterface import prep_cmd

SCREENSHOT_SIZE = 300
NUM_OF_INSTACE = 1
prep_cmd() # jak to dzialalo ? xD do przypomnienia na później
RecordStep  = False 


ListOfSteps = ManageSettings(RecordStep)

memuc_exe   = 'F:\\Program Files\\memu\\MEmu\\memuc.exe'
QUINDAN_APP = "F:\\memu\\base.apk"

for num in range(0, NUM_OF_INSTACE):
    print (num)
    subprocess.Popen([memuc_exe, "remove"    ,"-i","{}".format(num)]).wait()
    subprocess.Popen([memuc_exe, "create"    , "51"]).wait()
    subprocess.Popen([memuc_exe, "setconfig" , "-i", "{}".format(num),"cpus","2"]).wait()
    subprocess.Popen([memuc_exe, "setconfig" , "-i", "{}".format(num),"memory","2048"]).wait()
    subprocess.Popen([memuc_exe, "setconfig" , "-i", "{}".format(num),"turbo_mode","0"]).wait()
    subprocess.Popen([memuc_exe, "start"     , "-i", "{}".format(num)]).wait()
    subprocess.Popen([memuc_exe, "adb"       , "-i", "{}".format(num),"shell","input","keyevent","3"]).wait()
    subprocess.Popen([memuc_exe, "installapp", "-i", "{}".format(num),"{}".format(QUINDAN_APP)]).wait()

    WindowName = "Memu" if num == 0 else "Memu" + str(num)
    handle = win32gui.FindWindow(None,WindowName)
    win32gui.SetForegroundWindow(handle)
    time.sleep((60*2))
    print("powinno sie zainstalowac")
    ListOfSteps.save_or_load()
    if RecordStep and num > 0:
        for steps in ListOfSteps.position_list:
            pass
            #move the coursor and do the click
    time.sleep((60*60))
    # jednak potrzebuje dwoch roznych instancji krokow, jedno do wyslania maila, drugie po odebraniu maila
    # potrebuje jeszcze odczyl z pliku TXT wartosci maila i usuniecia go z tego pliku
    # memuc adb - i $index  "shell input keyevent 3"
    # memuc installapp - i $index "F:\memu\base.apk"
    # subprocess.Popen([memuc_exe, "remove","-i","{}".format(num)]).wait()

    pass

ListOfSteps.save_or_load()
ScreenShots = MakeScreenshot(ListOfSteps.position_list, SCREENSHOT_SIZE)
ScreenShots.make_screensots()
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
