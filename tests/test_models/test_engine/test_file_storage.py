#!/usr/bin/python3
""" Check Filestorage class """

import unittest
import os


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class TestFileStorage(unittest.TestCase):
    """ Check the class """


    def setUp(self):
        """ Set up test environment """
        self.storage = FileStorage()
        self.storage_path = "file.json"
        if os.path.exists(self.storage_path):
            os.remove(self.storage_path)
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down test environment """
        if os.path.exists(self.storage_path):
            os.remove(self.storage_path)

    def test_all(self):
        """ Test all method """
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """ Test new method """
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), self.storage.all())

    def test_save(self):
        """ Test save method """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage_path))

    def test_reload(self):
        """ Test reload method """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertIn("BaseModel.{}".format(obj.id), self.storage.all())


if __name__ == '__main__':
    unittest.main()
