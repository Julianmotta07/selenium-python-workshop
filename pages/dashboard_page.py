from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    SOMETHING = (By.CSS_SELECTOR, "[aria-label='Home']")

    def isTopDisplayed(self):
        return self.find_element(self.SOMETHING).is_displayed()

