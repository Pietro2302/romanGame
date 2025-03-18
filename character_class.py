import uuid


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
        self.skills = {}
        self.relationships = {}
        self.inventory = {}
        self.quests = {}
        self.reputation = {}
        self.titles = {}

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'family_name': self.family_name,
            'gender': self.gender,
            'level': self.level,
            'xp': self.xp,
            'attributes': self.attributes,
            'skills': self.skills,
            'relationships': self.relationships,
            'inventory': self.inventory,
            'quests': self.quests,
            'reputation': self.reputation,
            'titles': self.titles
        }

    def __str__(self):
        return str(self.to_dict())
