import json
from enum import Enum

class MessageType(Enum):
    INFO = "INFO"             # General information
    WARNING = "WARNING"       # Non-critical issue
    ERROR = "ERROR"           # Critical issue or failure
    COMBAT = "COMBAT"         # Combat-related messages
    DIALOGUE = "DIALOGUE"     # NPC conversations
    QUEST = "QUEST"           # Quest-related updates
    SKILL = "SKILL"           # Skill usage or unlock notifications
    INVENTORY = "INVENTORY"   # Item usage, acquisition, or loss
    SYSTEM = "SYSTEM"  

def load_characters(filename):
    try:
        with open(filename, "r") as json_file:
            type(json_file)
            return json.load(json_file)
    except FileNotFoundError:
        return []


def save_characters(filename, characters_dict):
    with open(filename, "w") as json_file:
        json.dump(characters_dict, json_file, indent=4)

class GameMessage:
    def __init__(self, message_type, content, sender=None, recipient=None):
        """
        Rappresenta un messaggio interno tra i moduli del gioco.

        :param message_type: Tipo di messaggio (es. "INFO", "WARNING", "ERROR", "COMBAT", "DIALOGUE", etc.)
        :param content: Testo del messaggio
        :param sender: Modulo o entità che invia il messaggio (opzionale)
        :param recipient: Modulo o entità che riceve il messaggio (opzionale)
        """
        self.message_type = MessageType
        self.content = content
        self.sender = sender
        self.recipient = recipient

    def __repr__(self):
        sender = f"[{self.sender}]" if self.sender else "[SYSTEM]"
        return f"{sender} [{self.message_type}] -> {self.content}"


class GameResult:
    def __init__(self, success, message, data=None):
        """
        Rappresenta il risultato di un'azione nel gioco.

        :param success: Booleano, indica se l'operazione è riuscita
        :param message: Messaggio associato al risultato (es. errore, conferma, ecc.)
        :param data: Dati opzionali (es. danno inflitto, oggetti ottenuti, ecc.)
        """
        self.success = success
        self.message = GameMessage
        self.data = data  # Può contenere informazioni extra utili

    def __repr__(self):
        return f"GameResult(success={self.success}, message='{self.message}', data={self.data})"