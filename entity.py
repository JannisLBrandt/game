# for regular expressions
import re

# class for creating an entity in the game
class Entity:
    def __init__(self,
                 name,
                 health,
                 attack,
                 physical_resistance,
                 magic_resistance):
        self.name = name
        self.health = health
        self.attack = attack
        self.physical_resistance = physical_resistance
        self.magic_resistance = magic_resistance

    # get the name of the entity
    def get_name(self):
        return self.name
    
    # get thr health of the entity
    def get_health(self):
        return self.health
    # get the attack of the entity
    def get_attack(self):
        return self.attack
    # get the physical_resistance of the entity
    def get_physical_resistance(self):
        return self.physical_resistance

    # get the magica_resistance of the entity
    def get_magic_resistance(self):
        return self.magic_resistance
    
    # set the name of the entity
    def set_name(self, amount):
        self.name = amount
    
    # set the health of the entity
    def set_health(self, amount):
        self.health = amount
    
    # set the attack of the entity
    def set_attack(self, amount):
        self.attack = amount
    
    # set the physical_resistance of the entity
    def set_physical_resistance(self, amount):
        self.physical_resistance = amount

    # set the magic_resistance of the entity
    def set_magic_resistance(self, amount):
        self.magic_resistance = amount

def input_reader():
    name = input("Enter your entities' name: ")
    health = input("Enter your entities' health: ")
    attack = input("Enter your entities' attack: ")
    physical_resistance = input("Enter your entities' physical resistance: ")
    magic_resistance = input("Enter your entities' magic resistance: ")
    return name, health, attack, physical_resistance, magic_resistance

# function to check for valid input
def validate_input(name, health, attack, physical_resistance, magic_resistance):
    # validate name is of type string
    if type(name) != str:
        print(f"Error: name attribute is of type: {type(name)}")
        return
    # validate health is of type float
    if type(health) != float:
        print(f"Error: attribute health is of type: {type(health)}")
        return
    # validate attack is of type float
    if type(attack) != float:
        print(f"Error: attribute attack is of type: {type(health)}")
        return
    # validate physical resistance is of type float 
    if type(physical_resistance) != float:
        print(f"Error: attribute physical_resistance is og type: {type(physical_resistance)}")
        return
    # validate magical resistance is of type float
    if type(magic_resistance) != float:
        print(f"Error: attribute magic resistance is of type: {type(magic_resistance)}")
        return

# function to check for number in string
def is_numeric(a):
    pattern = r"-?\d+(\.\d+)?"
    return re.match(pattern, a)
        
def parse_input(name, health, attack, physical_resistance, magic_resistance):
    # check attribute name
    if not isinstance(name, str):
        name = str(name)
    # numerical attributes need to be checked that if the string is a number convert it else display error
    # check attribute health
    if is_numeric(health):
        health = float(health)
    else:
        raise ValueError("Health must be a numeric value")
    if is_numeric(attack):
        attack = float(attack)
    else:
        raise ValueError("Attack must be a numeric value")
    if is_numeric(physical_resistance):
        physical_resistance = float(physical_resistance)
    else:
        raise ValueError("Physical resistance must be a numerical value")
    if is_numeric(magic_resistance):
        magic_resistance = float(magic_resistance)
    else:
        raise ValueError("Magic resistance must be a numerical value")
    return name, health, attack, physical_resistance, magic_resistance

def create_entity(name, health, attack, physical_resistance, magic_resistance):
    entity = Entity(name,
                    health,
                    attack,
                    physical_resistance,
                    magic_resistance)
    return entity
