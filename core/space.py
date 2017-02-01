# Licensed under MIT
# <tom@viabledata.co.uk>
"""The main module for the example project.
"""
from .config import settings

class Spaceship(object):
    """Defines a Spaceship class with a couple of basic functions that we will
    test.
    """
    def __init__(self, name, description):
        self.name = name
        self.model = settings['default_model']
        self.description = description
        self.inventory = []

    def get_inventory(self):
        """Gets the Spaceship's inventory
        """
        return self.inventory

    def add_item(self, item):
        """Adds an item to the Spaceship's inventory
        """
        self.inventory.append(item)
