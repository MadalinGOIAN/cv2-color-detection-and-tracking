import threading

from user_interface import UI
from color_tracker import track_color

thread = threading.Thread(target=track_color)
thread.start()
UI.start()

thread.join()
