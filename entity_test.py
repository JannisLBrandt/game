import unittest
import entity

class TestEntity(unittest.TestCase):
    def test_name(self):
        object = entity.Entity("test", 0)
        self.assertEqual(object.get_name(), "test")

if __name__ == '__main__':
    unittest.main()
