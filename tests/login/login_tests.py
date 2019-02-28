from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.incident.incident_page import IncidentPage
from utilities.teststatus import TstStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Login(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.incpage = IncidentPage(self.driver)
        self.tstatus = TstStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.incpage.login("admin", "123")

        # verify login
        result = self.incpage.verifyLoginFail()
        assert result == True

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.incpage.login("admin", "Gayani123")

        # verify login
        result1 = self.incpage.verifyLoginTitle()
        self.tstatus.mark(result1, "Title is correct")
        result2 = self.incpage.verifySuccessfulLogin()
        self.tstatus.markFinal("test_validIncidentCreation", result2, "Login is successful")






#chromeTest = CreateIncidentTests()
#chromeTest.test_validIncidentCreation()
