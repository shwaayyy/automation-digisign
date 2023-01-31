import time

from object import *


def test_1(driver):
    time.sleep(5)
    jetbrains_object.h1_essential_tools_for_software(driver).click()
    assert jetbrains_object.h1_essential_tools_for_software(driver) is not None


def test_2(driver):
    time.sleep(5)
    jetbrains_object.subtitle(driver).click()
    assert jetbrains_object.subtitle(driver) is not None
