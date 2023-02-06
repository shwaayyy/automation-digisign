import time
import re

from datetime import datetime, timedelta
from typing import Union
from conftest import url
from test_document_new import delay

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select

from object import *

doc = doc_object
form = form_object
wna = form_wna_object
mail = mail_object
url_mail = url["mail-testing"]
url_staging = url["test"]


def test_crp1_1(driver):
    wna.link_create_account(driver).click()
    wna.link_foreign_registration(driver).click()

    try:
        assert wna.card_reg(driver) is not None
    except AssertionError as e:
        raise e


def test_crp1_2(driver, **kwargs):
    not_filled = kwargs.get("not_filled", "kitas")
    is_same = kwargs.get("is_same", False)
    test_crp1_1(driver)

    text_method = wna.option_onsite_face_verification_visiting(driver).text
    Select(wna.select_metode_verifikasi(driver)).select_by_visible_text(text_method)

    if not_filled is "kitas":
        wna.input_passport(driver).send_keys("123456789")
        if is_same:
            wna.input_kitas(driver).send_keys("123456789")
    else:
        wna.input_kitas(driver).send_keys("123456789")
        if is_same:
            wna.input_passport(driver).send_keys("123456789")

    wna.input_fullname(driver).send_keys("John Doe")
    wna.input_place_birth(driver).send_keys("Bangkok")
    wna.input_nationality(driver).send_keys("Thailand")
    Select(wna.select_year(driver)).select_by_visible_text("1993")

    delay(10)

    wna.button_next(driver).click()

    try:
        assert wna.invalid_input(driver) is not None
    except AssertionError as e:
        raise e

    # ada yang salah jadi ada yang harus di ubah


def test_crp1_3(driver):
    test_crp1_2(driver, not_filled="passport")


def test_crp1_4(driver):
    test_crp1_2(driver, is_same=True)
