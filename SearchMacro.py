import pyautogui as py
import keyboard as key
import random
import time as t
import msvcrt as m

times = 33

print("Press any key to continue...")
m.getch()
t.sleep(1)

print("Press q to stop.")
for i in range(1, times + 1):
    t.sleep(10)
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

print("Press any key to exit...")
m.getch()