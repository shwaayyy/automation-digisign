from selenium.webdriver.common.by import By


def link_foreign_registration(driver):
    return driver.find_element(By.XPATH, "//a[@href='https://corp.tandatanganku.com/wna/registration.html']")


def link_create_account(driver):
    return driver.find_element(By.XPATH, "//a[contains(@href, 'registration')]")


def select_metode_verifikasi(driver):
    return driver.find_element(By.XPATH, "//*[@id='metode_verifikasi']")


def input_kitas(driver):
    return driver.find_element(By.XPATH, "//input[@id='kitas']")


def input_passport(driver):
    return driver.find_element(By.XPATH, "//*[@id='passport']")


def input_fullname(driver):
    return driver.find_element(By.XPATH, "//*[@id='fullname']")


def input_place_birth(driver):
    return driver.find_element(By.XPATH, "//*[@id='lbrith']")


def input_nationality(driver):
    return driver.find_element(By.XPATH, "//*[@id='nationality']")


def select_gender(driver):
    return driver.find_element(By.XPATH, "//*[@id='gender']")


def select_day(driver):
    return driver.find_element(By.XPATH, "//*[@id='Day']")


def select_month(driver):
    return driver.find_element(By.XPATH, "//*[@id='Month']")


def select_year(driver):
    return driver.find_element(By.XPATH, "//*[@id='Year']")


def button_next(driver):
    return driver.find_element(By.XPATH, "//button[@onclick='step1()']")


def card_reg(driver):
    return driver.find_element(By.XPATH, "//div[contains(@class, 'p-3')]")


def option_onsite_face_verification_visiting(driver):
    return driver.find_element(By.XPATH, "//option[@value='ONSITE']")


def invalid_input(driver):
    return driver.find_element(By.XPATH, "//input[contains(@class, 'invalid')]")


def kitas_error(driver):
    return driver.find_element(By.XPATH, "//*[@id='e_kitas']")


def passport_error(driver):
    return driver.find_element(By.XPATH, "//*[@id='e_passport']")
