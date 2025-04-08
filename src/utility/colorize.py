from colorama import Fore, init

init(autoreset=True)
COLORS_SET={
        'BLUE'        :Fore.BLUE,
        'GREEN'       :Fore.GREEN,
        'YELLOW'      :Fore.YELLOW,
        'RED'         :Fore.RED,
        'MAGENTA'     :Fore.MAGENTA,
        'CYAN'        :Fore.CYAN,
        'LIGHTCYAN_EX':Fore.LIGHTCYAN_EX,
    }


def colorize_message(message, color):
    color=color.upper()
    if color in COLORS_SET.keys():
        return f"{COLORS_SET[color]}{message}{Fore.RESET}"
    else:
        return f"{Fore.WHITE}{message}{Fore.RESET}"


if __name__ == "__main__":
    pass
