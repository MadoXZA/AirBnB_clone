#!/usr/bin/python3
"""Testing Place"""

import unittest
import pep8
from models.place import Place


class PlaceTesting(unittest.TestCase):
    """Check Place class"""

    def test_pep8(self):
        """Test code style"""
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_place = 'models/place.py'
        result = pepstylecode.check_files([path_place])
        self.assertEqual(
                result.total_errors, 0,
                "Found code style errors (and warnings)."
                )


if __name__ == '__main__':
    unittest.main()
