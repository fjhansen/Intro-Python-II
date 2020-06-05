# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, race, sex, role, bio, inventory, skills, stats):
        self.name = name
        self.race = race
        self.sex = sex
        self.role = role
        self.bio = bio
        self.inv = inventory
        self.skil = skills
        self.stat = stats
    def __str__(self):
        return f'♥♥♥♥♥PLAYER♥♥♥♥♥ \n NAME: "{self.name}" \n RACE: "{self.race}" \n SEX: "{self.sex}" \n ROLE: "{self.role}" \n BIO: "{self.bio}" \n INV: "{self.inv}" \n SKIL: "{self.skil}" \n STAT: "{self.stat}" \n----------------------------'
