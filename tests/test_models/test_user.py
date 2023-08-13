#!/usr/bin/python3
"""Testing User"""

import unittest
import pep8
from models.user import User

class UserTesting(unittest.TestCase):
    """Check User class"""

    def test_pep8(self):
        """Test code style"""
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/user.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()

