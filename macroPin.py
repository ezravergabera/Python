import pyautogui as py
import time as t

times = 10 # number of pins

t.sleep(1)

for i in range(1, times + 1):
    message = "PIN "
    py.typewrite(message)
    py.press("down")
    with py.hold("ctrl"):
        py.press("left")