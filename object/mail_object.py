from selenium.webdriver.common.by import By


def input_username(driver):
    return driver.find_element(By.XPATH, "//*[@id='username']")


def input_password(driver):
    return driver.find_element(By.XPATH, "//*[@id='password']")


def submit_auth(driver):
    return driver.find_element(By.XPATH, "//input[@type='submit']")


def refresh(driver):
    return driver.find_element(By.XPATH, "//div[@class='ImgRefreshAll']")


def msg_list_1(driver):
    return driver.find_element(By.XPATH, "/html/body/div[4]/div[10]/div[1]/table/tbody/tr[2]/td/ul/li[1]")


def date_get(driver):
    return driver.find_element(By.XPATH, "//td[contains(@class, 'DateCol')]")
