from selenium.webdriver.common.by import By


def link_reg(driver):
    return driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div[1]/a[1]")


def username(driver):
    return driver.find_element(By.XPATH, "//*[@id='username']")


def password(driver):
    return driver.find_element(By.XPATH, "//input[@id='pd']")


def saldo_sign(driver):
    return driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div/div")


def nik_input(driver):
    return driver.find_element(By.XPATH, "//*[@id='idcard']")


def password_submit(driver):
    return driver.find_element(By.XPATH, "//*[@id='submit']")


def doc_file(driver):
    return driver.find_element(By.XPATH, "//input[@type='file']")


def btn_input_file(driver):
    return driver.find_element(By.XPATH, "//span[@class='btn btn-danger ']")


def doc_submit(driver):
    return driver.find_element(By.XPATH, "//button[@type='submit']")


def password_salah(driver):
    return driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")


def error_username(driver):
    return driver.find_element(By.XPATH, "//*[@id='e_username']")


def pass_error(driver):
    return driver.find_element(
        By.XPATH, "//*[text() = '[Password salah sebanyak 3x. Silakan coba kembali setelah 10 menit.]']")


def error_format16_nik(driver):
    return driver.find_element(
        By.XPATH, "//div[@id = 'e_idcard' and (text() = 'Harus 16 Digit.' or . = 'Harus 16 Digit.')]")


def error_format_false(driver):
    return driver.find_element(By.XPATH, "//*[text() = 'Format NIK Salah']")


def birth_place_input(driver):
    return driver.find_element(By.XPATH, "//*[@id='lbrith']")


def btn_next_step1(driver):
    return driver.find_element(By.XPATH, "//button[@onclick='step1()']")


def validation_name(driver):
    return driver.find_element(
        By.XPATH, "//input[@id='name'][contains(@class,'form-control input-md is-invalid')]")


def name_input(driver):
    return driver.find_element(By.XPATH, "//*[@id='name']")


def gender_select(driver):
    return driver.find_element(By.XPATH, "//*[@id='jk']")


def validation_place(driver):
    return driver.find_element(
        By.XPATH, "//input[@id='lbrith'][@class='form-control input-md is-invalid']")


def step2(driver):
    return driver.find_element(By.XPATH, "//*[text() = 'Informasi Akun']")


def password_reg(driver):
    return driver.find_element(By.XPATH, "//*[@id='password']")


def password_confirmation(driver):
    return driver.find_element(By.XPATH, "//*[@id='password2']")


def email_input_register(driver):
    return driver.find_element(By.XPATH, "//*[@id='email']")


def phone_input_register(driver):
    return driver.find_element(By.XPATH, "//*[@id='handphone']")


def step3(driver):
    return driver.find_element(By.XPATH, "//button[@onclick='step3()']")


def validation_username(driver):
    return driver.find_element(
        By.XPATH, "//input[@id='username'][@class='form-control input-md is-invalid']")


def err_username(driver):
    return driver.find_element(By.XPATH, "//*[@id='e_username']")


def username_registered(driver):
    return driver.find_element(By.XPATH, "/html/body/div[11]/form/div/div[4]/div[1]/div/div[2]/i")


def password_too_short(driver):
    return driver.find_element(By.XPATH, "//*[text() = 'Password terlalu pendek, min 8 character']")


def password_minus_symbol(driver):
    return driver.find_element(
        By.XPATH, "//*[text() = 'Password harus mengandung minimal 1 Simbol/Karakter Spesial']")


def strong_password(driver):
    return driver.find_element(By.XPATH, "//*[text() = 'Strong password']")


def pass_not_same(driver):
    return driver.find_element(By.XPATH, "//*[@id='e_password2']")


def validation_email(driver):
    return driver.find_element(
        By.XPATH, "//input[@id='email'][@class='form-control input-md is-invalid']")


def email_taken(driver):
    return driver.find_element(By.XPATH, "//*[text() = 'Email sudah terdaftar gunakan email lain']")


def number_taken(driver):
    return driver.find_element(
        By.XPATH,
        "//div[@id = 'e_handphone' and (text() = 'No HP sudah terdaftar gunakan nomor lain' or . = 'No HP sudah terdaftar gunakan nomor lain')]")


def email_invalid(driver):
    return driver.find_element(By.XPATH, "//*[text() = 'Invalid Email Address']")


def number_invalid(driver):
    return driver.find_element(
        By.XPATH, "//input[@id='handphone'][@class='NumOnly form-control input-md is-invalid']")


def false_number_format(driver):
    return driver.find_element(By.XPATH, "//*[text() = 'Format nomor salah']")


def number_less_than_8(driver):
    return driver.find_element(By.XPATH, "//*[text() = 'Nomor HP Minimal 8 digit']")


def step3_title(driver):
    return driver.find_element(
        By.XPATH, "//h3[(text() = 'Foto dan Tandatangan' or . = 'Foto dan Tandatangan')]")


def ktp_input(driver):
    return driver.find_element(By.XPATH, "//input[@type='file']")


def span_ktp_input(driver):
    return driver.find_element(By.XPATH, "//span[.//*[@id='imgektp']]")
