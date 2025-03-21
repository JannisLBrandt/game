# class for creating an entity in the game
class Entity:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    # get the name of the entity
    def get_name(self):
        return self.name
    
    # get thr health of the entity
    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack
    
    # set the name of the entity
    def set_name(self, name):
        self.name = name
    
    # set the health of the entity
    def set_health(self, health):
        self.health = health

    def set_attack(self, attack):
        self.attack = attack
