import pyautogui
import time
import sys
from vendas import moduloCadCliente


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


def vendas():
    pyautogui.hotkey('Alt', 'v')
    time.sleep(5)


def contareceber():
    pyautogui.hotkey('Alt', 'r')
    time.sleep(5)


def contapagar():
    pyautogui.hotkey('Alt', 'p')
    time.sleep(5)


def livrofiscal():
    pyautogui.hotkey('Alt', 'l')
    time.sleep(5)


def contabilidade():
    pyautogui.hotkey('Alt', 'c')
    time.sleep(5)


def ativo():
    pyautogui.hotkey('Alt', 'a')
    time.sleep(5)

if __name__ == "__main__":
    pyautogui.doubleClick(65, 321)
    pyautogui.moveTo(158, 808, duration=1)
    pyautogui.typewrite("G", interval=0.2)
    pyautogui.press('enter', interval=0.2)
    time.sleep(2)
    login()
    time.sleep(2)
    # if sys.argv.__getitem__(1) == "1":
    vendas()
    moduloCadCliente()
    # elif sys.argv.__getitem__(1) == "2":
    #     modulolivrofiscal()