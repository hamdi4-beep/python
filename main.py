import pyautogui

# opens up the search bar
pyautogui.hotkey('win', 's')

# types in Notepad
pyautogui.write('Notepad')

# launch the app
pyautogui.press('enter')

# delays a few seconds before it starts writing into the file
pyautogui.sleep(3)

# writes something into the app
pyautogui.typewrite('Whoa! I can launch and use apps without having to do that manually.')

# selects everything that was written
pyautogui.hotkey('ctrl', 'a')

# waits a few seconds before deleting selected text
pyautogui.sleep(4)
pyautogui.press('backspace')

# exists the notepad
pyautogui.hotkey('alt', 'f4')