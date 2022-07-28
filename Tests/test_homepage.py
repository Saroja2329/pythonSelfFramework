import pytest
from selenium.webdriver.support.select import Select

from Utiities.BaseClass import Baseclass
from page_objects.Home_page import Homepage

@pytest.mark.sanity
class Testtwo(Baseclass):
    def test_homepage(self,getData):
        homepage=Homepage(self.driver)
        homepage.enter_namefiled().send_keys(getData['name'])
        homepage.enter_emailfield().send_keys(getData['email'])
        homepage.enter_passwordfield().send_keys(getData['password'])
        homepage.click_on_checkbox().click()
        webelement= homepage.select_dropdown_value()
        self.select_value_by_visible_text("Female",webelement)
        homepage.enter_bday().send_keys(getData['dataofbirth'])
        homepage.click_on_submit_button().click()
        self.driver.refresh()
    @pytest.fixture(params=[{'name':"rahul",'email':"shetty@123",'password':"admin@123",'dataofbirth':'"09041998"'},{'name':"deepthi",'email':"sunaina@123",'password':"admin@153",'dataofbirth':"09041997"}])
    def getData(self,request):
        return request.param




