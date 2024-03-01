import keyboard
import time
import random
import pyautogui
from mss import mss

# Function to take a screenshot per frame to classify later
def take_screenshot():
    """
    Captures screenshots
    """
	monitor = mss().monitors[1]  # Capture the first monitor of system
	mss().grab(monitor) # Takes screenshot
	timestamp = time.time()
	filename = f"screenshot_{timestamp:.3f}.png"
	mss().shot(mon=1, output=filename) # Saves screenshot
	print(f"Screenshot saved as {filename}")

# Function that performs action randomly (for now, later will perform action
#  based on classification of image)
def perform_random_action():
    """
    Performs a random action from actions array.
    """
    actions = ['up', 'down', 'left', 'right', 'stay']
    action = random.choice(actions)
	if action != 'stay':
    	keyboard.press_and_release(action)
    print(f"Performed action: {action}")  # print the action performed

# Main loop
def main():
    try:
        while True:
            take_screenshot()
            perform_random_action()
    except KeyboardInterrupt:
        print("Program exited.")

if __name__ == "__main__":
    main()