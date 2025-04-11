import difflib

def suggest_command(user_command, commands):
        matches = difflib.get_close_matches(user_command, commands.keys(), n=5, cutoff=0.2)
        return matches if matches else None
    
if __name__ == "__main__":
    pass
