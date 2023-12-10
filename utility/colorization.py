"""
Console colors utilities
"""


def foreground_color(r, g, b):
    return f'\033[38;2;{r};{g};{b}m'

def background_color(r, g, b):
    return f'\033[48;2;{r};{g};{b}m'\
        
        
COLOR_RESET='\033[0m'
COLOR_INT=foreground_color(201, 18, 162)
COLOR_FLOAT=foreground_color(232, 48, 7)
COLOR_STRING=foreground_color(30, 18, 201)

COLOR_OK=foreground_color(218, 22, 224)
COLOR_BAD=foreground_color(5, 222, 255)
COLOR_ALERT=foreground_color(101, 255, 5)

import os
import ctypes
import platform

def enable_virtual_terminal_processing(turnOn: bool):
    if not turnOn:
        COLOR_RESET=''
        COLOR_INT=''
        COLOR_FLOAT=''
        COLOR_STRING=''

        COLOR_OK=''
        COLOR_BAD=''
        COLOR_ALERT=''
        return
    
    if platform.system() == "Windows":
        kernel32 = ctypes.WinDLL('kernel32')
        hStdOut = kernel32.GetStdHandle(-11)
        mode = ctypes.c_ulong()
        kernel32.GetConsoleMode(hStdOut, ctypes.byref(mode))
        mode.value |= 4  # ENABLE_VIRTUAL_TERMINAL_PROCESSING is 0x0004
        kernel32.SetConsoleMode(hStdOut, mode)
    
def colorize(arg: any) -> str:
    """
    Determines the type of the argument and returns a colorized string based on its type.

    Parameters:
    arg (any): The argument whose type needs to be determined.

    Returns:
    str: A colorized string representation of the argument.
    """
    if isinstance(arg, int):
        return f"{COLOR_INT}{arg}{COLOR_RESET}"
    elif isinstance(arg, float):
        return f"{COLOR_FLOAT}{arg}{COLOR_RESET}"
    elif isinstance(arg, str):
        return f"{COLOR_STRING}{arg}{COLOR_RESET}"
    elif isinstance(arg, bool):
        return f"{COLOR_OK if arg else COLOR_BAD}{arg}{COLOR_RESET}"
    else:
        return f"{arg}"
