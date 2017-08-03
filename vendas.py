import pyautogui
import time

def moduloEspecial():
    pyautogui.keyDown('Alt')
    pyautogui.press('s')
    pyautogui.press('r')
    pyautogui.keyUp('Alt')


def moduloCadCliente():
    pyautogui.keyDown('Alt')
    pyautogui.press('d')
    pyautogui.press('c')
    pyautogui.press('c')
    pyautogui.press('right')
    pyautogui.press('c')
    pyautogui.press('enter')
    pyautogui.keyUp('Alt')
    time.sleep(1)
    # incluir("1", True, "21687684", "0001", "11")
    mostar(517, 258)

def mostar(positionx, positiony):
    pyautogui.hotkey('Alt', 'o')
    pyautogui.moveTo(positionx, positiony, duration=0.2)
    pyautogui.click()
    pyautogui.press('enter')


def incluir(regiao=None, matriz=False, cnpj_1=None, cnpj_2=None, cnpj_3=None ):
    pyautogui.press("f5")
    time.sleep(1)
    pyautogui.typewrite(regiao, interval=0.2)
    pyautogui.press("enter")
    if matriz:
        pyautogui.press("space")
    pyautogui.press("enter")
    pyautogui.press("del")
    if len(cnpj_1) < 9:
        pyautogui.typewrite(cnpj_1, interval=0.2)
        pyautogui.press("enter")
    else:
        pyautogui.typewrite(cnpj_1, interval=0.2)
    pyautogui.typewrite(cnpj_2, interval=0.2)
    pyautogui.typewrite(cnpj_3, interval=0.2)
    pyautogui.press("enter")
    pyautogui.typewrite("Teste Atomatizado", interval=0.2)
    pyautogui.press("enter")
    pyautogui.hotkey('Alt', 'o')