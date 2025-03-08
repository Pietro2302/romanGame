class Item:
    def __init__(self, name, item_type, description):
        self.name = name
        self.item_type = item_type  # Example: 'weapon', 'potion', 'armor', etc.
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.item_type}): {self.description}"