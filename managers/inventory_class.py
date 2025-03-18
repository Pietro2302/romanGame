class Item:
    def __init__(self, name, item_type, description, effects):
        self.name = name
        self.item_type = item_type
        self.description = description
        self.effects = effects

    def __str__(self):
        return f"{self.name} ({self.item_type}): {self.description}"

class InventoryManager:
    def __init__(self):
        self.items = {}
