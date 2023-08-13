#!/usr/bin/python3
"""Testing Amenity"""

import unittest
import pep8
from models.amenity import Amenity


class AmenityTesting(unittest.TestCase):
    """Check Amenity class"""

    def test_pep8(self):
        """Test code style"""
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_amenity = 'models/amenity.py'
        result = pepstylecode.check_files([path_amenity])
        self.assertEqual(
                result.total_errors, 0,
                "Found code style errors (and warnings)."
                )


if __name__ == '__main__':
    unittest.main()
