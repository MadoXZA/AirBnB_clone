#!/usr/bin/python3
"""
Initialization for the models module.
"""

from models.engine.file_storage import FileStorage

# Create a single instance of FileStorage named storage
storage = FileStorage()
storage.reload()
