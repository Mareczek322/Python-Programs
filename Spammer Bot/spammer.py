import pyautogui
import time

rec = input("Enter who to mention: ")
msg = input("Enter the message: ")
n = input("How many times ?: ")

print("t minus")

count = 5
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("Fire in the hole!!!")

for i in range(0,int(n)):
	pyautogui.typewrite(rec)
	pyautogui.press('enter')
	pyautogui.typewrite(msg)
	pyautogui.press('enter')
	time.sleep(1)

	
