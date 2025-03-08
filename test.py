from rich.console import Console
from rich.text import Text
from rich.panel import Panel
import questionary  # Replaces PyInquirer

# Initialize Rich console
console = Console()

# Function to display a styled message
def show_message(title, message, style="bold green"):
    text = Text(f"\n{title}\n", style="bold underline")
    text.append(message, style=style)
    console.print(Panel(text, expand=False))


# Function to display interactive choices
def ask_question(question, choices):
    return questionary.select(question, choices=choices).ask()


# Example Game Flow
console.print("[bold cyan]Welcome to Ancient Rome, traveler![/bold cyan]")
show_message("Narrator:", "A hooded figure approaches you in the market...")

# Interaction example
choice = ask_question("What do you do?", ["Greet them", "Draw your weapon", "Ignore them"])
if choice == "Greet them":
    show_message("Stranger:", "Ah, a friendly soul. You seem like a person of great potential.")
elif choice == "Draw your weapon":
    show_message(
        "Stranger:",
        "Bold... but foolish. You feel a hidden blade press against your back.",
        "bold red"
    )
elif choice == "Ignore them":
    show_message(
        "Stranger:",
        "Silent type, huh? You might survive here after all.",
        "bold yellow"
    )

# Combat example
show_message("A gladiator challenges you!", "Prepare for battle!", "bold red")
combat_choice = ask_question("What will you do?", ["Attack", "Defend", "Try to talk"])
if combat_choice == "Attack":
    show_message("You swing your sword!", "The crowd roars!", "bold magenta")
elif combat_choice == "Defend":
    show_message("You raise your shield!", "The gladiator tests your defenses.", "bold blue")
elif combat_choice == "Try to talk":
    show_message("You attempt diplomacy!", "The gladiator smirks but lowers his guard.", "bold green")

console.print("[bold cyan]Your adventure continues...[/bold cyan]")