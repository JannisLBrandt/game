import unittest
import entity

class TestEntity(unittest.TestCase):
    # creates the same entity for every test, resets changes from previous ones
    def setUp(self):
        self.entity = entity.Entity("test", 0, 0, 0, 0)
    
    # test  attribute name
    def test_get_name(self):
        self.assertEqual(self.entity.get_name(), "test")

    def test_set_name(self):
        self.entity.set_name("test1")
        self.assertEqual(self.entity.get_name(), "test1")
    
    # test attribute health
    def test_get_health(self):
        self.assertEqual(self.entity.get_health(), 0)

    def test_set_health(self):
        self.entity.set_health(1)
        self.assertEqual(self.entity.get_health(), 1)
    
    # test attribute attack
    def test_get_attack(self):
        self.assertEqual(self.entity.get_attack(), 0)

    def test_set_attack(self):
        self.entity.set_attack(1)
        self.assertEqual(self.entity.get_attack(), 1)
    
    # test attribute physical_resistance
    def test_get_physical_resistance(self):
        self.assertEqual(self.entity.get_physical_resistance(), 0)

    def test_set_physical_resistance(self):
        self.entity.set_physical_resistance(1)
        self.assertEqual(self.entity.get_physical_resistance(), 1)
    
    # test attribute magical_resistance
    def test_get_magic_resistance(self):
        self.assertEqual(self.entity.get_magic_resistance(), 0)
    
    def test_set_magic_resistance(self):
        self.entity.set_magic_resistance(1)
        self.assertEqual(self.entity.get_magic_resistance(), 1)
    
    # test parsing input
    def test_parse_input(self):
        # create wrong data to parse
        name_wrong = 1
        health_wrong = "test"
        attack_wrong = "test"
        physical_resistance_wrong = "test"
        magic_resistance_wrong = "test"
        
        # test wrong data
        with self.assertRaises(ValueError):
            entity.parse_input(name_wrong, health_wrong, attack_wrong, physical_resistance_wrong, magic_resistance_wrong)

        # create correct data
        name_correct = "test"
        health_correct = "1"  
        attack_correct = "1" 
        physical_resistance_correct = "1" 
        magic_resistance_correct = "1" 
        
        # test correct data
        name, health, attack, physical_resistance, magic_resistance = entity.parse_input(name_correct, health_correct, attack_correct, physical_resistance_correct, magic_resistance_correct)
        self.assertEqual(type(name), str)
        self.assertEqual(type(health), float)
        self.assertEqual(type(attack), float)
        self.assertEqual(type(physical_resistance), float)
        self.assertEqual(type(magic_resistance), float)

if __name__ == '__main__':
    unittest.main()
