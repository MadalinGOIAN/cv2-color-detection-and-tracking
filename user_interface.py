import tkinter as tk
from constants import *

class UI:
    window = tk.Tk()
    lower_limit = blue.lower
    upper_limit = blue.upper
    
    def start():
        UI.window.title('Choose Color')
        
        button_frame = tk.Frame(UI.window)
        button_frame.pack(padx=10, pady=10)
        
        UI.create_button('blue', UI.set_blue)
        UI.create_button('red', UI.set_red)
        UI.create_button('yellow', UI.set_yellow)
        
        UI.window.mainloop()

    def create_button(color, command):
        button = tk.Button(UI.window, bg=color,
                           width=10, height=5, command=command)
        button.pack(side=tk.LEFT, padx=10, pady=10)

    def set_blue():
        UI.lower_limit = blue.lower
        UI.upper_limit = blue.upper

    def set_red():
        UI.lower_limit = red.lower
        UI.upper_limit = red.upper

    def set_yellow():
        UI.lower_limit = yellow.lower
        UI.upper_limit = yellow.upper
