#! /usr/bin/python3

import pyautogui, time

time.sleep(5)
pyautogui.click()    # click to put drawing program in focus
distance = 200
while distance > 0:
	pyautogui.dragRel(distance, 0, duration=0.2)   # move right
	distance = distance - 5
	pyautogui.dragRel(0, distance, duration=0.2)   # move down
	pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
	distance = distance - 5
	pyautogui.dragRel(0, -distance, duration=0.2)  # move up
