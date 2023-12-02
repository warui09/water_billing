#!/usr/bin/python3
"""Test suite for the user class"""

import unittest
User = __(import)__('User').User

class TestUserInstance(unittest.TestCase):
    def test_instance(self):
        #test instantiation of the User class
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.first_name)
        self.assertIsNotNone(user.last_name)
        self.assertIsNotNone(user.meter_number)
        self.assertIsNotNone(user.phone_number)
        self.assertIsNotNone(user.address)

if __name__ == "__main__":
    unittest.main()