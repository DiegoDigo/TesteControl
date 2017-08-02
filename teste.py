import pyautogui
import time
import sys


def login():
    pyautogui.typewrite("1", interval=0.2)
    pyautogui.press('enter', interval=0.2)
    pyautogui.typewrite("ctr", interval=0.2)
    pyautogui.typewrite("043244", interval=0.2)
    pyautogui.press('enter', interval=0.2)
    i = 0
    while i < 3:
        pyautogui.press('enter', interval=0.2)
        i += 1


def modulovendas():
    pyautogui.hotkey('Alt', 'v')
    time.sleep(5)
    pyautogui.keyDown('Alt')
    pyautogui.press('s')
    pyautogui.press('r')
    pyautogui.keyUp('Alt')


def modulocontareceber():
    pyautogui.hotkey('Alt', 'r')


def modulocontapagar():
    pyautogui.hotkey('Alt', 'p')


def modulolivrofiscal():
    pyautogui.hotkey('Alt', 'l')


def modulocontabilidade():
    pyautogui.hotkey('Alt', 'c')


def moduloativo():
    pyautogui.hotkey('Alt', 'a')

if __name__ == "__main__":
    pyautogui.doubleClick(65, 321)
    pyautogui.moveTo(158, 808, duration=1)
    pyautogui.typewrite("G", interval=0.2)
    pyautogui.press('enter', interval=0.2)
    time.sleep(2)
    login()
    time.sleep(2)
    if sys.argv[1] == "1":
        modulovendas()
    elif sys.argv[1] == "2":
        modulolivrofiscal()
    else:
        print(u"opcão invalida")