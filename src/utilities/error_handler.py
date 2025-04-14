from utilities.colorize import colorize_message
"""
Error Handling Utilities

Provides standardized colored output for error messages with two severity levels.
"""

def error_handler(e):
    print(colorize_message(f"{e}", "RED"))

def error_handler_yellow(e):
    print(colorize_message(f"{e}", "YELLOW"))
    
if __name__ == "__main__":
    pass
