# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, race, sex, role, bio, skills, stats, room, inventory=[]):
        self.name = name
        self.race = race
        self.sex = sex
        self.role = role
        self.bio = bio
        self.inv = inventory
        self.skil = skills
        self.stat = stats
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.room = room
        
    def __str__(self):
        return f'\n ♥♥♥♥♥PLAYER♥♥♥♥♥ \n NAME: "{self.name}" \n RACE: "{self.race}" \n SEX: "{self.sex}" \n ROLE: "{self.role}" \n BIO: "{self.bio}" \n INV: "{self.inv}" \n SKIL: "{self.skil}" \n STAT: "{self.stat} \n ROOM: "{self.room.name}" \n----------------------------'
    def inventory(self):
        i = ''
        for x in self.inv:
            i += f"†††††ITEM††††† \n NAME: {x.name} - ({x.desc}) \n"
        return i
