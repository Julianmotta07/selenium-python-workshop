from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginFBPage(BasePage):
    USER_EMAIL = (By.ID, 'email')
    USER_PASSWORD = (By.ID, 'pass')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-testid='royal_login_button']")
    
    def login(self, email, password):
        self.enter_text(self.USER_EMAIL, email)
        self.enter_text(self.USER_PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

