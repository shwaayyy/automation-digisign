import base64
from datetime import datetime

import pytest
from pytest_html import extras

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

url = {
    "prod": "https://app.digisign.id",
    "test": "https://app.tandatanganku.com",
    "mail-testing": "https://mail.tandatanganku.com",
    "mail-digi": "https://mail.digi-id.id",
    "dummy": "https://www.jetbrains.com/"
}


def driver_manager(driver):
    if driver is "chrome":
        return webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    elif driver is "firefox":
        return webdriver.Firefox()


# How to run the test you can run with CLI: pytest --html=reports/report.html --self-contained-html <test_case_file>.py
@pytest.fixture
def driver():
    browser = driver_manager("chrome")

    browser.maximize_window()
    browser.implicitly_wait(20)
    browser.get(url["test"])

    yield browser

    browser.close()


def pytest_configure(config):
    config._metadata.update({
        'PIC': 'Wahyu Hidayat',
        'Time Test': datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
    })


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        browser = item.funcargs['driver']
        try:
            screenshot = browser.get_screenshot_as_png()
            screenshot_b64 = base64.b64encode(screenshot).decode("utf-8", "ignore")
            extra.append(extras.image(screenshot_b64, "Screenshot"))
        except Exception as e:
            print("Couldn't get screenshot")
            print(e)
        report.extra = extra
