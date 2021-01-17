import pyautogui
import time

print('Press Ctrl-C to quit.')
print('Start in 10 Seconds. Be ready.')
time.sleep(5)

sleep_time = 0.25 
interval_time = 0.25

try:
	while True:
		# copy cell and press down key one
		pyautogui.hotkey('command', 'c', interval=interval_time)
		time.sleep(sleep_time)
		pyautogui.press('down')
		time.sleep(sleep_time)
	
		# move to youtube music
		pyautogui.hotkey('command', '2', interval=interval_time)

		# move to search box and paste text then hit enter
		pyautogui.click(2050, 137, clicks=2, interval=interval_time)
		time.sleep(sleep_time)
		pyautogui.hotkey('command', 'a', interval=interval_time)

		# Search the query
		time.sleep(sleep_time)
		pyautogui.hotkey('command', 'v', interval=interval_time)
		time.sleep(sleep_time)
		pyautogui.press('enter')
		time.sleep(3)

		# move to first music and hit 3 dots
		# select save to playlist, and select the first one
		pyautogui.click(2433, 407)
		time.sleep(sleep_time)
		pyautogui.click(2800, 440)
		time.sleep(sleep_time)
		pyautogui.click(2890, 478)
		time.sleep(sleep_time)

		# If twitter was opend, close tab and the popup
		pyautogui.hotkey('command', '3', interval=interval_time)
		time.sleep(sleep_time)
		pyautogui.hotkey('command', 'w', interval=interval_time)
		time.sleep(sleep_time)
		pyautogui.press('esc')
		time.sleep(sleep_time)

		# If it is another type to select playlist, try again
		pyautogui.click(2433, 407)
		time.sleep(sleep_time)
		pyautogui.click(2800, 440)
		time.sleep(sleep_time)
		pyautogui.click(2890, 542)
		time.sleep(sleep_time)

		# press esc 3 times before move to another tap 
		pyautogui.press('esc', presses=3)
		time.sleep(sleep_time)

		# go back to spreedsheet
		pyautogui.hotkey('command', '1', interval=interval_time)
		
except KeyboardInterrupt:
	print('\nDone!')

# Sleep for 3 seconds
time.sleep(3)


