from conftest import url, robot
from test_document_new import delay

from selenium.webdriver import Keys
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
    registered = kwargs.get("registered", [False, ''])
    num_kitas = kwargs.get("kitas", "123456789")

    test_crp1_1(driver)

    text_method = wna.option_onsite_face_verification_visiting(driver).text
    Select(wna.select_metode_verifikasi(driver)).select_by_visible_text(text_method)

    if not_filled is "kitas":
        wna.input_passport(driver).send_keys("123456789")
        if is_same:
            wna.input_kitas(driver).send_keys(num_kitas)
            for i in range(8):
                wna.input_kitas(driver).send_keys(Keys.BACKSPACE)
                delay(1)
            wna.input_kitas(driver).send_keys("23456789")
        robot.press("ctrl")
        robot.press("alt")
    else:
        wna.input_kitas(driver).send_keys(num_kitas)
        if is_same:
            wna.input_passport(driver).send_keys("123456789")
            for i in range(8):
                wna.input_passport(driver).send_keys(Keys.BACKSPACE)
                delay(1)
            wna.input_passport(driver).send_keys("23456789")
        robot.press("ctrl")
        robot.press("alt")

    if registered[0] is True:
        if registered[1] is "kitas":
            wna.input_kitas(driver).clear()
            wna.input_kitas(driver).send_keys("1")
            wna.input_passport(driver).send_keys("23456789")
        elif registered[1] is "passport":
            wna.input_passport(driver).clear()
            wna.input_passport(driver).send_keys("12")
            wna.input_kitas(driver).send_keys("23456789")
    else:
        pass

    robot.press("ctrl")
    robot.press("alt")
    delay(10)

    wna.input_fullname(driver).send_keys("John Doe")
    wna.input_place_birth(driver).send_keys("Bangkok")
    wna.input_nationality(driver).send_keys("Thailand")
    Select(wna.select_year(driver)).select_by_visible_text("1993")

    delay(10)

    if is_same is False or registered[0] is False:
        wna.button_next(driver).click()

    if is_same is True or registered[0] is True:
        try:
            assert wna.kitas_error(driver) is not None
            print("passed")
        except AssertionError as e:
            raise e
    else:
        try:
            assert wna.invalid_input(driver) is not None
            print("passed")
        except AssertionError as e:
            raise e


def test_crp1_3(driver):
    test_crp1_2(driver, not_filled="passport")


def test_crp1_4(driver):
    test_crp1_2(driver, is_same=True, not_filled="kitas", registered=[True, ''])


def test_crp1_5(driver):
    test_crp1_2(driver, is_same=False, not_filled="passport", registered=[True, "kitas"])


def test_crp1_6(driver):
    test_crp1_2(driver, is_same=False, not_filled="kitas", registered=[True, "passport"])


def test_crp1_7(driver):
    test_crp1_3(driver)


def test_crp1_8(driver):
    test_crp1_2(driver, is_same=True, not_filled="kitas", registered=[True, ""])

    delay(3)

    try:
        assert wna.invalid_input(driver) is not None
        assert wna.input_kitas(driver) is not None
    except AssertionError as e:
        raise e


# def test_crp1_9(driver):
#
