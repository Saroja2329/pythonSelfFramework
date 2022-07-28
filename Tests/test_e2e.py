import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from Utiities.BaseClass import Baseclass


# @pytest.mark.usefixtures("setup")
from page_objects.Home_page import Homepage

from page_objects.checkout_page import  CheckoutPage
from page_objects.confirm_page import ConfirmPage

@pytest.mark.smoke
class TestOne(Baseclass):
    def test_e2e(self):
        home=Homepage(self.driver)
        checkoutpage=home.shop_items()
        self.driver.implicitly_wait(10)

        #self.driver.find_element(By.XPATH, "//a[text()='Shop']").click()
        products = checkoutpage.checkout_items()
        check_item=checkoutpage.checkout_singleitem()
        for product in products:
            product_name = product.find_element(By.XPATH, "div/button").text
            print(product_name)
            if product_name == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
        checkoutpage.Validate_cart().click()
        confirmpage=ConfirmPage(self.driver)
        confirmpage=checkoutpage.validate_checkout_button()
        confirmpage.click_confirm_button().send_keys("India")
        self.verify_link_presence("India")
        confirmpage.click_on_text().click()
        confirmpage.click_checkbox().click()
        confirmpage.click_on_purchase_button().click()
        alert_txt = confirmpage.validate_textmatch().text
        # alert_txt=="Success! Thank you!", "Successfully alert present"
