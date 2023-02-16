import pyautogui as py
import time as t


def Spam(message, times):
    for i in range(1, times + 1):
        py.typewrite(message)
        # t.sleep(1)
        py.press("enter")


words = input("Your message: \n")
count = int(input("How many times: \n"))
t.sleep(2)
Spam(words, count)
