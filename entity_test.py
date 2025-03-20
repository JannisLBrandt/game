import unittest
import entity

class TestEntity(unittest.TestCase):
    def setUp(self):
        self.entity = entity.Entity("test", 0)

    def test_get_name(self):
        self.assertEqual(self.entity.get_name(), "test")

    def test_set_name(self):
        self.entity.set_name("test1")
        self.assertEqual(self.entity.get_name(), "test1")

    def test_get_health(self):
        self.assertEqual(self.entity.get_health(), 0)

    def test_set_health(self):
        self.entity.set_health(1)
        self.assertEqual(self.entity.get_health(), 1)

if __name__ == '__main__':
    unittest.main()
