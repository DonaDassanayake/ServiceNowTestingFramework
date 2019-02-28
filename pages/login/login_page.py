
from base.basepage import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    #Locators
    _username_field = "user_name"
    _password_field = "user_password"
    _login_button = "sysverb_login"

    #Set values
    def enterUsername(self, username):
        # Set values using customized Selenium class
        self.sendKeys(username, self._username_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="id")

    #Login
    def login(self, username="", password=""):
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLoginButton()


