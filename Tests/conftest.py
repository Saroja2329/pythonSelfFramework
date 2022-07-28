

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default='chrome'
    )

@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    if browser_name=='chrome':
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("headless")
        service_obj = Service("C:\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    elif browser_name=='firefox':
        service_obj = Service("C:\drivers\geckodriver.exe")
        driver=webdriver.firefox(service=service_obj)

         #
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(10)
    request.cls.driver=driver
    yield
    driver.close()