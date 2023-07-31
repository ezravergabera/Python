import pyautogui as py
import keyboard as key
import random
import time as t

times = 33

t.sleep(1)

for i in range(1, times + 1):
    if(key.is_pressed("q")):
        break
    search = ""
    number_of_letter = random.randint(6, 15)
    for j in range(1, number_of_letter + 1):
        search = search + chr(random.randint(65, 122))
        if random.randint(1, 2) == 1:
            search = search + " "
    py.typewrite(search)
    py.press("enter")
    with py.hold("ctrl"):
        py.press("e")
    py.press("backspace")