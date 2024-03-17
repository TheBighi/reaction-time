import pyautogui
from PIL import ImageGrab
import keyboard
import time

# Define the colors to detect
color1 = (208, 36, 52)  # RGB value of color #d02434
color2 = (80, 220, 108)  # RGB value of color #50dc6c

# Coordinates of the pixel you want to monitor
pixel_x = 1596
pixel_y = 276

# Define a tolerance for color matching
tolerance = 10

def detect_color_change():
    # Grab a screenshot
    screenshot = ImageGrab.grab()

    # Get the color of the specified pixel
    pixel_color = screenshot.getpixel((pixel_x, pixel_y))

    # Check if the color is within the tolerance range of color1 or color2
    if all(abs(pixel_color[i] - color1[i]) <= tolerance for i in range(3)):
        return 1
    elif all(abs(pixel_color[i] - color2[i]) <= tolerance for i in range(3)):
        return 2
    else:
        return 0

def click_screen():
    # Get the screen resolution
    screen_width, screen_height = pyautogui.size()

    # Perform a click at the center of the screen
    pyautogui.click(screen_width / 2, screen_height / 2)

# Main loop
print("Press 'P' to start color detection and click functionality.")
keyboard.wait('p')  # Wait for the 'P' key to be pressed

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
    time.sleep(0.01)  # Adjust the delay as per your need
