#!/usr/bin/python3
"""Testing city"""

import unittest
import pep8
from models.city import City


class CityTesting(unittest.TestCase):
    """Check City class"""

    def test_pep8(self):
        """Test code style"""
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_city = 'models/city.py'
        result = pepstylecode.check_files([path_city])
        self.assertEqual(
                result.total_errors, 0,
                "Found code style errors (and warnings)."
                )


if __name__ == '__main__':
    unittest.main()
