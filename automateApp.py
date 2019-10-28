import subprocess, sys
import pyautogui
import pyperclip
import time

# powershellVirtualAndroidScript = "F:\\memu\\runemucMultipleTimes.ps1"
# subprocess.Popen(["powershell", powershellVirtualAndroidScript])
#will run pythong from ps1 script

screenWidth, screenHeight    = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
# pyautogui.moveTo(450, 450, duration=1.0)
num = 0
while ( num < 100 ):
    print ("To jest pozycja kursora {0}".format(pyautogui.position))
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
