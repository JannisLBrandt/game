# class for creating an entity in the game
class Entity:
    def __init__(self,
                 name,
                 health,
                 attack,
                 physical_resistance):
        self.name = name
        self.health = health
        self.attack = attack
        self.physical_resistance = physical_resistance

    # get the name of the entity
    def get_name(self):
        return self.name
    
    # get thr health of the entity
    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_physical_resistance(self):
        return self.physical_resistance
    
    # set the name of the entity
    def set_name(self, amount):
        self.name = amount
    
    # set the health of the entity
    def set_health(self, amount):
        self.health = amount

    def set_attack(self, amount):
        self.attack = amount

    def set_physical_resistance(self, amount):
        self.physical_resistance = amount
