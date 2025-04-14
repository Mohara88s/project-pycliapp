from colorama import Fore, init
"""
Handles user input with colored prompt and automatic color reset.
"""

init(autoreset=True)

def user_input_handler(input_text):
    user_input = input(f"{input_text}{Fore.LIGHTCYAN_EX}")
    print(Fore.RESET, end="")
    return user_input

if __name__ == "__main__":
    pass
