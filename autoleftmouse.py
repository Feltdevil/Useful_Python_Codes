import time
import threading
import os
from pynput.mouse import Button, Controller, Listener
from pynput.keyboard import Key, Listener as KeyboardListener

# Initialize the mouse controller
mouse = Controller()
clicking = False
self_clicking = False  # Flag to prevent self-clicking registration

def click_mouse():
    global self_clicking
    while True:
        if clicking:
            self_clicking = True  # Indicate that the click is from the auto-clicker
            mouse.click(Button.left)
            self_clicking = False   # Reset the flag after clicking
            time.sleep(0.01)  # Adjust the delay for click speed (0.01 seconds between clicks)

def on_click(x, y, button, pressed):
    global clicking
    if button == Button.left and pressed:
        if not self_clicking:  # Check if the click is not from the auto-clicker
            clicking = not clicking  # Toggle clicking state
            if clicking:
                print("Auto-clicking started.")
            else:
                print("Auto-clicking stopped.")

def on_press(key):
    if key == Key.f7:
        print("F7 pressed. Exiting...")
        os._exit(0)  # Exit the script completely

# Start the auto-clicking thread
click_thread = threading.Thread(target=click_mouse)
click_thread.daemon = True
click_thread.start()

# Start the mouse listener
with Listener(on_click=on_click) as mouse_listener:
    # Start the keyboard listener
    with KeyboardListener(on_press=on_press) as keyboard_listener:
        mouse_listener.join()  # Wait for mouse listener to finish
        keyboard_listener.join()  # Wait for keyboard listener to finish
