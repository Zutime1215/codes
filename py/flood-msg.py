import pyautogui
import time

msg = input("Write your messege: ")
shongkha = int(input("How Much messege: "))

time.sleep(5)

# It's a loop.
for i in range(shongkha):  
	if i < shongkha:
		time.sleep(2)
		pyautogui.typewrite(msg)
		pyautogui.press("enter")

	else:	
		break		