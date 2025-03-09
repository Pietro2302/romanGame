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

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'family_name': self.family_name,
            'gender': self.gender,
            'level': self.level,
            'xp': self.xp,
            'attributes': self.attributes,
            'skills': self.skills.to_dict(),
            'relationships': self.relationships.to_dict(),
            'inventory': self.inventory.to_dict(),
            'quests': self.quests.to_dict(),
            'reputation': self.reputation.to_dict(),
            'titles': self.titles.to_dict()
        }
    
    def __str__(self):
        return str(self.to_dict())
