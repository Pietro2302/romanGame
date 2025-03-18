from inventory_class import InventoryManager
from quest_class import QuestsManager
from relationship_class import RelationshipsManager
from reputation_class import ReputationsManager
from skills_class import SkillsManager
from title_class import TitlesManager


class CharacterManager:
    def __init__(self):
        self.inventoryManager = InventoryManager()
        self.questManager = QuestsManager()
        self.relationshipManager = RelationshipsManager()
        self.reputationManager = ReputationsManager()
        self.skillManager = SkillsManager()
        self.titleManager = TitlesManager()
        