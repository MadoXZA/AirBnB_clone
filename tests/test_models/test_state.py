#!/usr/bin/python3
"""Testing State"""


import unittest
import pep8
from models.state import State


class StateTesting(unittest.TestCase):
    """Check State class"""

    def test_pep8(self):
        """Test code style"""
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_state = 'models/state.py'
        result = pepstylecode.check_files([path_state])
        self.assertEqual(
                result.total_errors, 0,
                "Found code style errors (and warnings)."
                )


if __name__ == '__main__':
    unittest.main()
