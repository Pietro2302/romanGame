class Reputation:
    def __init__(self):
        # Different categories of reputation
        self.reputations = {
            "military": 0,  # Military reputation
            "noble": 0,     # Noble reputation
            "religious": 0, # Religious reputation
            "popular": 0,   # General public opinion
            "feared": 0     # Reputation for fear among enemies
        }
     
    def to_dict(self):
        return self.reputations