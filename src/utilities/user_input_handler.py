from colorama import Fore, init

init(autoreset=True)

def user_input_handler():
    user_input = input(f"Enter a command: {Fore.LIGHTCYAN_EX}")
    print(Fore.RESET, end="")
    return user_input

if __name__ == "__main__":
    pass
