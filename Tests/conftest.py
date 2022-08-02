

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_name",
#         action="store",
#         default='chrome'
#     )

@pytest.fixture(scope='class')
def setup(request):
    global driver
    selenium_grid_url = "http://192.168.1.100:4444/wd/hub"
    # Create a desired capabilities object as a starting point.
    chromeOptions = webdriver.ChromeOptions()

    chromeOptions.add_argument("start-maximized")
    chromeOptions.add_argument("--ignore-certificate-errors")
    chromeOptions.add_argument("--disable-features=RendererCodeIntegrity")
    capabilities = chromeOptions.to_capabilities()
    #browser_name=request.config.getoption("browser_name")
    driver = webdriver.Remote(desired_capabilities=capabilities,
                              command_executor=selenium_grid_url)
    # if browser_name=='chrome':
    #     chrome_options = webdriver.ChromeOptions()
    #     # chrome_options.add_argument("headless")
    #     service_obj = Service("C:\drivers\chromedriver.exe")
    #     driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    # elif browser_name=='firefox':
    #     service_obj = Service("C:\drivers\geckodriver.exe")
    #     driver=webdriver.firefox(service=service_obj)

         #
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(10)
    request.cls.driver=driver
