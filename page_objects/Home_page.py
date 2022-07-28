from selenium.webdriver.common.by import By

from page_objects.checkout_page import CheckoutPage


class Homepage:


     shop = (By.CSS_SELECTOR, "a[href*='shop']")
     name_feild=(By.NAME,"name")
     email_feild = (By.NAME, "email")
     name_feild = (By.NAME, "name")
     pswd_field=(By.ID,"exampleInputPassword1")
     checkbox=(By.ID,"exampleCheck1")
     dropdown=(By.ID,"exampleFormControlSelect1")
     dfb_element=(By.NAME,"bday")
     submit_element=(By.CSS_SELECTOR,"input[type='submit']")
     def __init__(self, driver):
         self.driver=driver

     def shop_items(self):
         self.driver.find_element(*Homepage.shop).click()
         checkoutpage = CheckoutPage(self.driver)
         return checkoutpage
     def enter_namefiled(self):
         return self.driver.find_element(*Homepage.name_feild)
     def enter_emailfield(self):
         return self.driver.find_element(*Homepage.email_feild)
     def enter_passwordfield(self):
         return self.driver.find_element(*Homepage.pswd_field)
     def click_on_checkbox(self):
         return self.driver.find_element(*Homepage.checkbox)

     def select_dropdown_value(self):
         return self.driver.find_element(*Homepage.dropdown)
     def enter_bday(self):
         return self.driver.find_element(*Homepage.dfb_element)
     def click_on_submit_button(self):
         return self.driver.find_element(*Homepage.submit_element)