class Title:
    def __init__(self, name, effects=None, description=None):
        self.name = name
        self.effects = effects if effects is not None else {}
        self.description = description if description else "No description provided."

    def __str__(self):
        return self.name

    def get_effects(self):
        return self.effects

    def get_description(self):
        return self.description


class Titles:
    def __init__(self):
        self.titles = {}  # { Title.SENATOR: {"influence": +10, "gold": +100}, ... }

    def to_dict(self):
        return {title.name: effects for title, effects in self.titles.items()}