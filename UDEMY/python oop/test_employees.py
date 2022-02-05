import unittest
from employees import Employee

class TestEmployee(unittest.TestCase):
    def test_get_full_name(self):
        e = Employee("John", "Mogi", 0, None)
        self.assertEqual(e.get_full_name(), "Mogi John")