from enum import Enum


class ReputationType(Enum):
    HONORABLE = "Honorable"
    FEARED = "Feared"
    CORRUPT = "Corrupt"
    NEUTRAL = "Neutral"
    NOBLE = "Noble"
    INFAMOUS = "Infamous"
    TREACHEROUS = "Treacherous"
    DIGNIFIED = "Dignified"
    DECEITFUL = "Deceitful"
    BRAVE = "Brave"
    CUNNING = "Cunning"
    TYRANNICAL = "Tyrannical"


class Reputation:
    def __init__(self, reputation_type, reputation_value=0, history=None):
        self.reputation_type = reputation_type
        self.reputation_value = reputation_value
        self.history = history if history else []


class ReputationsManager:
    def __init__(self):
        self.reputations = {}
