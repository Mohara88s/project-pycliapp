from utilities.colorize import colorize_message

def error_handler(e):
    print(colorize_message(f"{e}", "RED"))
    
if __name__ == "__main__":
    pass
