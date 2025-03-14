import time

class Skill:
    def __init__(self, name, skill_type, is_active=True, combat_only=False,
                 cooldown=0, stamina_cost=0, requirements=None, scaling_factors=None, effect=None):
        self.name = name
        self.skill_type = skill_type
        self.is_active = is_active
        self.combat_only = combat_only
        self.cooldown = cooldown
        self.stamina_cost = stamina_cost
        self.requirements = requirements if requirements is not None else {}
        self.scaling_factors = scaling_factors if scaling_factors is not None else {}
        self.effect = effect  
        self.last_used_time = 0  

    def is_ready(self):
        """Check if the skill is off cooldown."""
        current_time = time.time()
        return (current_time - self.last_used_time) >= self.cooldown

    def use(self, user, **kwargs):
        if self.is_active:
            if not self.is_ready():
                return f"{self.name} is on cooldown."
            if user.stamina < self.stamina_cost:
                return f"Not enough stamina to use {self.name}."
            self.last_used_time = time.time()
            if self.combat_only:
                user.stamina -= self.stamina_cost
        if self.effect is not None:
            return self.effect(user, **kwargs)
        
        return f"{self.name} used."

    def __repr__(self):
        return f"Skill(name='{self.name}', type='{self.skill_type}', active={self.is_active})"

class SkillsManager:
    def __init__(self, max_combat_skills=4):
        self.learned_skills = {}           
        self.equipped_combat_skills = {}      
        self.max_combat_skills = max_combat_skills

    def learn_skill(self, skill):
        self.learned_skills[skill.name] = skill

    def equip_skill(self, skill_name):
        if skill_name not in self.learned_skills:
            return f"Skill {skill_name} not learned."
        skill = self.learned_skills[skill_name]
        if not skill.is_active:
            return f"{skill_name} is passive and always active."
        if len(self.equipped_combat_skills) >= self.max_combat_skills:
            return "Maximum combat skills already equipped."
        self.equipped_combat_skills[skill_name] = skill
        return f"{skill_name} equipped for combat."

    def unequip_skill(self, skill_name):
        if skill_name in self.equipped_combat_skills:
            del self.equipped_combat_skills[skill_name]
            return f"{skill_name} unequipped."
        return f"{skill_name} is not equipped."

    def use_skill(self, skill_name, user, **kwargs):
        if skill_name not in self.learned_skills:
            return f"Skill {skill_name} not learned."
        skill = self.learned_skills[skill_name]
        if skill.is_active and skill.combat_only:
            if skill_name not in self.equipped_combat_skills:
                return f"{skill_name} is not equipped for combat."
        return skill.use(user, **kwargs)

    def list_skills(self):
        return list(self.learned_skills.keys())

    def list_equipped_skills(self):
        return list(self.equipped_combat_skills.keys())

    def __repr__(self):
        return (f"SkillsManager(learned_skills={list(self.learned_skills.keys())}, "
                f"equipped_combat_skills={list(self.equipped_combat_skills.keys())})")

