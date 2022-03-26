import string    
import random 
import pyautogui
import time

S = 20
shongkha = int(input("How Much messege: "))

time.sleep(5)
for i in range(shongkha):  
	if i < shongkha:
		time.sleep(1.7)
		ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
		pyautogui.typewrite(ran)
		pyautogui.press("enter")

	else:	
		break
 