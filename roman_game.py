from styles import narrator_print
from menu_functions import new_Game, displaySaveGames
from common_functions import load_characters
from rich.console import Console
import questionary
import os
import time
console = Console()
characters_filename = "character_player.json"
narrator_print("Hello and welcome to the Roman Imperium,fili mi! My name is Publius Vergilius Maro, and I will be your guide through this difficult world of mine. Firstly, choose what to do.",console)
menu_choice = questionary.select(
    "Menu",
    choices=["New Game", "Load Game", "Options", "Exit"]
).ask()

match menu_choice:
    case "New Game":
        os.system('cls')
        narrator_print("You chose to start a new game. Good luck, Roman!",console)
        time.sleep(2.5)
        new_Game(console)
    case "Load Game":
        os.system('cls')
        narrator_print("Choose one of the characters you have previously saved:", console)
        displaySaveGames(console)

