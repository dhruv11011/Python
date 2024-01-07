import pyautogui
import time

def gui():
    pyautogui.moveTo(800, 300, duration=1)
    pyautogui. click ()
    screenWidth, screenHeight= pyautogui.size()
    print("The Screen Width is:", screenWidth)
    print("The Screen Height is:", screenHeight)
    pyautogui.alert(text= 'Python_A1ert', title='Advanced Python Programming By Dhruv Bhatt', button='OK')
    pyautogui.screenshot("screenshot.png")
    pyautogui.write("Hello, PyAutoGUI!", interval=0.2)
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('ctrl','v')

if __name__=="__main__":
    time.sleep(5)
    gui()
