from selenium.webdriver.common.by import By

from page_objects.confirm_page import ConfirmPage


class CheckoutPage:
    #self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    items=(By.XPATH,"//div[@class='card h-100']")
    #product.find_element(By.XPATH, "div/h4/a")
    item=(By.XPATH,"div/h4/a")
    #find_element(By.XPATH, "div/button")
    add_button=(By.XPATH,"div/button")
    # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']")
    cart=(By.CSS_SELECTOR,"a[class*='btn-primary']")
    #self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']")
    check_button=(By.CSS_SELECTOR,"button[class*='btn-success']")
    #self.driver.find_element(By.LINK_TEXT, "India")
    click_text=(By.LINK_TEXT,"India")
    def __init__(self,driver):
        self.driver=driver

    def checkout_items(self):
        return self.driver.find_elements(*CheckoutPage.items)
    def checkout_singleitem(self):
        return self.driver.find_element(*CheckoutPage.items)
    # def Click_add_button(self):
    #     return find_element(*CheckoutPage.add_button)
    def Validate_cart(self):
        return self.driver.find_element(*CheckoutPage.cart)

    def validate_checkout_button(self):
         self.driver.find_element(*CheckoutPage.check_button).click()
         confirmpage = ConfirmPage(self.driver)
         return confirmpage