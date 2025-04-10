from utility.colorize import colorize_message

def show_help(commands):
        print("This is available commands:")
        for name, info in commands.items():
            print(f"  {name:<15} - {info['description']}")
    
if __name__ == "__main__":
    pass
