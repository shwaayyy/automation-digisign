import time

from selenium.webdriver import Keys, ActionChains
from conftest import url
from object import *
from test_document_new import test_web3_6

mail = mail_object
doc = doc_object
form = form_object
url_mail = url["mail-testing"]


def delay(sec):
    time.sleep(sec)


def test_1(driver):
    time.sleep(5)
    jetbrains_object.h1_essential_tools_for_software(driver).click()
    assert jetbrains_object.h1_essential_tools_for_software(driver) is not None


def test_2(driver):
    time.sleep(5)
    jetbrains_object.subtitle(driver).click()
    assert jetbrains_object.subtitle(driver) is not None


def test_mail_otp(driver):
    driver.execute_script("window.open('about:blank','tab2')")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url_mail)

    mail.input_username(driver).send_keys("ditest6@tandatanganku.com")
    mail.input_password(driver).send_keys("ditest123" + Keys.ENTER)
    delay(5)

    for i in range(10):
        mail.refresh(driver).click()
        delay(1.5)

    ActionChains(driver).double_click(mail.msg_list_1(driver)).perform()

    driver.switch_to.frame(mail.iframe_main_body(driver))
    otp = mail.otp_selector(driver).text

    print("this is otp: " + otp)


def test_web6_2(driver, **kwargs):
    auto = kwargs.get('auto', True)
    used = kwargs.get('used', False)
    denial = kwargs.get('denial', False)
    otp_type = kwargs.get('otp_type', 'email')
    form.username(driver).send_keys("wahyuhi" + Keys.ENTER)
    form.password(driver).send_keys("Kijang321!" + Keys.ENTER)
    doc.choose_account(driver).click()

    delay(3)

    doc.need_sign(driver).click()
    doc.latest_inbox(driver).click()

    doc.button_proses_sign_one(driver).click()
    delay(2)

    if denial is True:
        doc.label_tidak(driver).click()
        delay(3)
        doc.text_area_reason(driver).send_keys("testing")

    if otp_type is "email":
        doc.btn_otp_email(driver).click()
    elif otp_type is "sms":
        doc.btn_otp_sms(driver).click()

    if auto is True:
        doc.otp_input_number(driver).send_keys("002383")

    if auto is False and otp_type is "email":
        test_web3_6(driver, otp_auto_use=True)

    if auto is False and otp_type is "email":
        pass
    else:
        doc.btn_prosign(driver).click()
        doc.btn_saya_yakin(driver).click()

    if used is False:
        try:
            assert doc.swal_otp_none(driver) is not None
        except Exception as e:
            raise e

    delay(10)

