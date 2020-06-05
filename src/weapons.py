class Weapons:
    def __init__(self, name, description, enchantment, effect, damage):
        self.name = name
        self.desc = description
        self.ench = enchantment
        self.efct = effect
        self.dmg = damage
    def __str__(self):
        return f'\n ⚔⚔⚔⚔⚔WEAPON⚔⚔⚔⚔⚔ \n NAME: "{self.name}" \n DESC: "{self.desc}" \n ENCH: "{self.ench}" \n EFCT: "{self.efct}" \n DAMG: {self.dmg} \n----------------------------'
    
