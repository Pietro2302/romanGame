class Skill:
    def __init__(self, name, skill_type, effects, is_active=True,
                 combat_only=False, cooldown=0, stamina_cost=0,
                 requirements=None):
        self.name = name
        self.skill_type = skill_type
        self.is_active = is_active
        self.combat_only = combat_only
        self.cooldown = cooldown
        self.stamina_cost = stamina_cost
        self.requirements = requirements if requirements is not None else {}
        self.effects = effects

    def __repr__(self):
        return (
            f"Skill(name='{self.name}',"
            f" type='{self.skill_type}',"
            f" active={self.is_active})"
        )


class SkillsManager:
    def __init__(self):
        self.skills = {}
        self.cooldowns = {}

    def load_skills(self, character):
        self.skills = character.skills
