# aim at last of first line
import pyautogui as py
import time as t
import math

times = 4  # number of pins

t.sleep(1)

for i in range(1, math.ceil(times/5)):
    py.press("down")
    py.press("down")
    py.press("down")
    py.press("down")
    py.press("enter")
    py.press("down")
    with py.hold("ctrl"):
        py.press("right")
        py.press("right")  # do this once if PIN is not included
