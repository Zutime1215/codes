import pyautogui
import time

msg = input("Write your messege: ")
shongkha = int(input("How Much messege: "))

time.sleep(3)

for i in range(shongkha):  
	if i < shongkha:
		time.sleep(1)
		pyautogui.typewrite(msg)
		pyautogui.press("enter")

	else:	
		break
	
