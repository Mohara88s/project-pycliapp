from utilities.colorize import colorize_message

def show_help(commands):
        i=0
        print("This is available commands:")
        for name, info in commands.items():
            print(colorize_message(f"  {name:<15} - {info['description']}", f"{"CYAN" if i%2==0 else "BLUE"}"))
            i+=1

if __name__ == "__main__":
    pass
