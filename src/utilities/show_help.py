from rich.console import Console
from rich.table import Table
"""
Displays a formatted help table of available commands using rich library styling.
"""
def show_help(commands):
    console = Console()

    table = Table(title="Available commands:", title_style="bold green", style="green", row_styles=["cyan", "blue"] )

    table.add_column("Command")
    table.add_column("Description")

    for name, info in commands.items():
        table.add_row(name, info["description"])

    console.print(table)

if __name__ == "__main__":
    pass
