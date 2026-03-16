from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "login-email-input")
    PASSWORD_INPUT = (By.ID, "login-password-input")
    LOGIN_BUTTON = (By.ID, "login-submit-btn")
    ADMIN_BUTTON = (By.ID, "login-fill-admin-btn")
    USER_BUTTON = (By.ID, "login-fill-user-btn")

    def select_admin_role(self):
        self.click(self.ADMIN_BUTTON)

    def select_user_role(self):
        self.click(self.USER_BUTTON)

    def enter_username(self, username):
        self.type(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login_as_admin(self, username, password):
        self.select_admin_role()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def login_as_user(self, username, password):
        self.select_user_role()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()