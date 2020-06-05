# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.desc = description
    def __str__(self):
        return f'****ROOM***** \n NAME: "{self.name}" \n DESC: "{self.desc}" \n----------------------------'
