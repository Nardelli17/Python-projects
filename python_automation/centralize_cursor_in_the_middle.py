# Created by Nardelli17 
# Date 31-08-2024.

import pyautogui
import keyboard
import time

def centralize_cursor():
    # Get the screen width and height
    screen_width, screen_height = pyautogui.size()
    
    # Calculate the center of the screen
    center_x = screen_width // 2
    center_y = screen_height // 2
    
    # Move the mouse to the center
    pyautogui.moveTo(center_x, center_y)

if __name__ == "__main__":
    print("Press Enter to centralize the cursor. Press Ctrl+C to exit.")
    
    try:
        while True:
            # Wait for the Enter key press
            if keyboard.is_pressed('enter'):
                centralize_cursor()
                # Adding a small delay to avoid multiple detections for a single press
                time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nExiting program.")
