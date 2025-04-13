from utilities.colorize import colorize_message

def error_handler(e):
    print(colorize_message(f"{e}", "RED"))

def error_handler_yellow(e):
    print(colorize_message(f"{e}", "YELLOW"))
    
if __name__ == "__main__":
    pass
