def parse_input(user_input):
    """
    Parses raw user input into command and arguments.

    Splits the input string into tokens and separates the command (first word) 
    from its arguments (remaining words). Normalizes the command to lowercase.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
    

if __name__ == "__main__":
    pass
