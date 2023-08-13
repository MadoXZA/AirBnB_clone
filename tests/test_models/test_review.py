#!/usr/bin/python3
"""Testing Review"""

import unittest
import pep8
from models.review import Review

class ReviewTesting(unittest.TestCase):
    """Check Review class"""

    def test_pep8(self):
        """Test code style"""
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_review = 'models/review.py'
        result = pepstylecode.check_files([path_review])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()

