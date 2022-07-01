import pyautogui, time
def commentAfterDelay():
   time.sleep(2)
   pyautogui.click(100, 100)
   pyautogui.typewrite('In IDLE, Alt-3 comments out a line.')
   time.sleep(2)
   pyautogui.hotkey('alt', '3')

commentAfterDelay()














##n IDLE, Alt-3 comments out a line.











