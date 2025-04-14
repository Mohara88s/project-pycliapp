from colorama import Fore, init
"""  
    Provides colored console output using ANSI color codes.  
    Includes predefined color palette and safe fallback for invalid colors.  
    """  

init(autoreset=True)
COLORS_SET={
        'BLUE'        :Fore.BLUE,
        'GREEN'       :Fore.GREEN,
        'YELLOW'      :Fore.YELLOW,
        'RED'         :Fore.RED,
        'MAGENTA'     :Fore.MAGENTA,
        'CYAN'        :Fore.CYAN,
        'LIGHTCYAN_EX':Fore.LIGHTCYAN_EX,
        'WHITE'       :Fore.WHITE,
    }

def colorize_message(message, color):
    """  
    Applies colored formatting to text message for console output.  
    """
    color=color.upper()
    if color in COLORS_SET.keys():
        return f"{COLORS_SET[color]}{message}{Fore.RESET}"
    else:
        return f"{Fore.WHITE}{message}{Fore.RESET}"


if __name__ == "__main__":
    pass
