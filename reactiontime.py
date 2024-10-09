import pyautogui
from PIL import ImageGrab
import keyboard
import time


color1 = (208, 36, 52)
color2 = (80, 220, 108) 

pixel_x = 1596
pixel_y = 276

tolerance = 10

def detect_color_change():
    screenshot = ImageGrab.grab()

    pixel_color = screenshot.getpixel((pixel_x, pixel_y))

    if all(abs(pixel_color[i] - color1[i]) <= tolerance for i in range(3)):
        return 1
    elif all(abs(pixel_color[i] - color2[i]) <= tolerance for i in range(3)):
        return 2
    else:
        return 0

def click_screen():
    screen_width, screen_height = pyautogui.size()

    pyautogui.click(screen_width / 2, screen_height / 2)

print("Press 'P' to start color detection and click functionality.")
keyboard.wait('p')

print("Color detection and click functionality started.")
while True:
    change_detected = detect_color_change()
    if change_detected == 1:
        print("Color changed to #d02434 detected.")
    elif change_detected == 2:
        print("Color changed to #50dc6c detected.")
        click_screen()
    else:
        print("No color change detected. Pixel color:", pyautogui.screenshot().getpixel((pixel_x, pixel_y)))
    time.sleep(0.01) # adjust as you need 
