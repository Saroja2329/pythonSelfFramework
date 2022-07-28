from selenium.webdriver.common.by import By


class ConfirmPage:
    # self.driver.find_element(By.ID, "country")
    confirm_button=(By.ID,"country")
    # self.driver.find_element(By.LINK_TEXT, "India")
    click_text = (By.LINK_TEXT, "India")
    #self.driver.find_element(By.XPATH, "//div[contains(@class,'checkbox')]")
    check_box=(By.XPATH,"//div[contains(@class,'checkbox')]")
    #self.driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']")
    click_purchase=(By.CSS_SELECTOR,"input[value='Purchase']")
    #self.driver.find_element(By.CLASS_NAME, "alert-success")
    text_search=(By.CLASS_NAME,"alert-success")
    def __init__(self,driver):
        self.driver=driver

    def click_confirm_button(self):
        return self.driver.find_element(*ConfirmPage.confirm_button)
    def click_on_text(self):
        return self.driver.find_element(*ConfirmPage.click_text)
    def click_checkbox(self):
        return self.driver.find_element(*ConfirmPage.check_box)
    def click_on_purchase_button(self):
        return self.driver.find_element(*ConfirmPage.click_purchase)
    def validate_textmatch(self):
        return self.driver.find_element(*ConfirmPage.text_search)