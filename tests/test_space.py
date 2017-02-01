# Licensed under MIT
# <tom@viabledata.co.uk>
"""The tests for space.py
"""
import pytest

from core.space import Spaceship


def setup():
    """This function will always run before any tests.\n
    Use it to set up the test environment, as required.
    """
    print("SETUP!")


def teardown():
    """This function will always run after all of the tests.\n
    Use it to clean up.
    """
    print("TEAR DOWN!")


def test_create_spaceship():
    """Tests the creation of a new Spaceship instance.
    """
    serenity = Spaceship("Serenity",
                         "Captain Reynold's favourite place")
    assert serenity.name == "Serenity"
    assert serenity.model == "Firefly"
    assert serenity.description == "Captain Reynold's favourite place"
    assert serenity.inventory == []
