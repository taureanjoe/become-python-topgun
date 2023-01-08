'''
This program uses the pyautogui library to open the calculator program, type the expression "2 + 2" into the calculator, and press Enter to evaluate the result. It then takes a screenshot of the calculator window and saves it to a file called "result.png".

To use this program, you will need to have the "pyautogui" library installed. You can install it using pip install pyautogui. Then, simply run the program and it will automate the tasks on your computer. Note that this program is designed to work on a Windows computer with the calculator program installed. If you are using a different operating system or a different program, you may need to adjust the commands accordingly.

'''

import pyautogui

# Open the calculator program
pyautogui.hotkey('win', 'r')
pyautogui.typewrite('calc')
pyautogui.hotkey('enter')

# Perform a calculation
pyautogui.typewrite('2 + 2')
pyautogui.hotkey('enter')

# Take a screenshot of the result
image = pyautogui.screenshot()
image.save('result.png')
