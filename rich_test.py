from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()

# Simple colored text output
console.print("[bold cyan]Welcome to Ancient Rome![/bold cyan]")

# Creating a panel for immersive storytelling
story_text = Text("A hooded figure stands before you. What do you do?", style="bold yellow")
console.print(Panel(story_text, title="A Mysterious Encounter"))

# Creating a fancy table (useful for inventory, stats, etc.)
table = Table(title="Character Stats")
table.add_column("Attribute", style="bold magenta")
table.add_column("Value", justify="right", style="bold green")

table.add_row("Strength", "10")
table.add_row("Charisma", "8")
table.add_row("Wisdom", "7")

console.print(table)
