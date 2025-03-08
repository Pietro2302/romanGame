import uuid
from skills_class import Skills
from relationship_class import Relationships
from inventory_class import Inventory
from quest_class import QuestSystem
from reputation_class import Reputation
from title_class import Titles


class Character:
    def __init__(self, first_name, family_name, gender):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.family_name = family_name
        self.gender = gender
        self.level = 0
        self.xp = 0
        self.attributes = {
            "strength": 10, "dexterity": 10, "constitution": 10,
            "intelligence": 10, "wisdom": 10, "charisma": 10
        }

        self.skills = Skills()
        self.relationships = Relationships()
        self.inventory = Inventory()
        self.quests = QuestSystem()
        self.reputation = Reputation()
        self.titles = Titles()

    def __str__(self):
        # String representation of the character
        return (f"ID: {self.id} | Character: {self.first_name} {self.family_name}, "
                f"Gender: {self.gender}, Level: {self.level} | XP: {self.xp}\n"
                f"Attributes - STR: {self.attributes['strength']}, "
                f"DEX: {self.attributes['dexterity']}, CON: {self.attributes['constitution']}, "
                f"INT: {self.attributes['intelligence']}, WIS: {self.attributes['wisdom']}, "
                f"CHA: {self.attributes['charisma']}\n"
                f"Skills: {str(self.skills)} | Relationships: {str(self.relationships)}\n"
                f"Inventory: {str(self.inventory)} | Quests: {str(self.quests)} | "
                f"Reputation: {str(self.reputation)} | Titles: {str(self.titles)}")

    def to_dict(self):
        # Convert character to a dictionary representation
        return {
            'id': self.id,
            'first_name': self.first_name,
            'family_name': self.family_name,
            'gender': self.gender,
            'level': self.level,
            'xp': self.xp,
            'attributes': self.attributes,
            'skills': self.skills.to_dict(),  # Assuming Skills class has a to_dict method
            'relationships': self.relationships.to_dict(),  # Assuming Relationships class has a to_dict method
            'inventory': self.inventory.to_dict(),  # Assuming Inventory class has a to_dict method
            'quests': self.quests.to_dict(),  # Assuming QuestSystem class has a to_dict method
            'reputation': self.reputation.to_dict(),  # Assuming Reputation class has a to_dict method
            'titles': self.titles.to_dict()  # Assuming Titles class has a to_dict method
        }
