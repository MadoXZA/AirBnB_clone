#!/usr/bin/python3
"""
Unit tests for console using Mock module from python standard library
Check console for capturing stdout into a stringIO object
"""
import sys
import unittest
from unittest.mock import patch, create_autospec
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """
    Unittest for the console model
    """

    def setUp(self):
        """Redirecting stdin and stdout"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        self.err = ["** class name missing **",
                    "** class doesn't exist **",  # Corrected typo
                    "** instance id missing **",
                    "** no instance found **",
                    ]
        self.cls = ["BaseModel",
                    "User",
                    "State",
                    "City",
                    "Place",
                    "Amenity",
                    "Review"]

    def create(self):
        """
        Redirects stdin and stdout to the mock module
        """
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def last_write(self, nr=None):
        """Returns last n output lines"""
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(lambda c: c[0][0],
                           self.mock_stdout.write.call_args_list[-nr:]))

    def test_quit(self):
        """Quit command"""
        cli = self.create()
        with self.assertRaises(SystemExit):
            cli.onecmd("quit")

    # You can add more tests below this line to test other commands.

if __name__ == '__main__':
    unittest.main()
