import time
import os
from pyfiglet import Figlet
from utilities.colorize import colorize_message
"""
Console Animation Utilities

Provides functions for creating animated console banners and text effects.
Includes console clearing capabilities and timed text animations.
"""

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def animate_text(lines, delay=0.05):
    for line in lines:
        print(colorize_message(line.center(os.get_terminal_size().columns), "GREEN"))
        time.sleep(delay)

def show_banner():
    clear_console()

    big_font = Figlet(font='slant')
    mid_font = Figlet(font='standard')

    assistant_text = big_font.renderText("ASSISTANT BOT").split('\n')
    made_by_text = mid_font.renderText("made by").split('\n')
    pythonway_text = mid_font.renderText("ThePythonWay").split('\n')

    animate_text(assistant_text, delay=0.05)
    time.sleep(0.5)
    animate_text(made_by_text, delay=0.05)
    time.sleep(0.5)
    animate_text(pythonway_text, delay=0.05)
    time.sleep(2)
    clear_console()


if __name__ == "__main__":
    show_banner()