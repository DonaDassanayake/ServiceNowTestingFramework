import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_field = "filter"
    _create_new_incident = "//a[@id='14641d70c611228501114133b3cc88a1']"
    _sp_search_field = "//input[@placeholder='How can we help?']"
    _sp_create_new_incident = "//span[contains(text(), 'Create')]"
    _sp_incpage_search_field = "//input[@placeholder='Search']"
    _sp_incpage_create_new_incident = "//strong[contains(text(),'Incident')]"
    _sp_ticketfm_search_field = "//input[@placeholder='Search']"

    # Values
    _search_text = "incident"

    def searchIncident(self):
        #wait until _serch_field
        self.waitForElement(self._search_field, timeout=20)
        self.elementClick(self._search_field)
        self.sendKeys(self._search_text, self._search_field)

    def clickCreateIncident(self):
        time.sleep(10)
        self.waitForElement(self._create_new_incident, locatorType="xpath")
        self.elementClick(self._create_new_incident, locatorType="xpath")

    def isSPSearchFieldVisible(self):
        self.waitForElement(self._sp_ticketfm_search_field, locatorType="xpath")
        if self.isElementDisplayed(self._sp_ticketfm_search_field, locatorType="xpath") is False:
            return False
        else:
            return True


    def isMainSearchVisible(self):
        self.waitForElement(self._sp_search_field, locatorType="xpath")
        if self.isElementDisplayed(self._sp_search_field,locatorType="xpath") is False:
            return False
        else:
            return True

    def searchServicePortalIncident(self):
        self.waitForElement(self._sp_search_field, locatorType="xpath")
        self.sendKeys(self._search_text, self._sp_search_field, locatorType="xpath")

    def clickSPCreateIncident(self):
        self.waitForElement(self._sp_create_new_incident,locatorType="xpath")
        self.elementClick(self._sp_create_new_incident, locatorType="xpath")

    def navigateToCreateIncident(self):
        self.searchIncident()
        self.clickCreateIncident()

    def loadSPCreateIncidentFromHome(self):
        self.searchServicePortalIncident()
        self.clickSPCreateIncident()

    def searchSPCreateIncidentFromIncPage(self):
        self.waitForElement(self._sp_incpage_search_field,locatorType="xpath")
        self.sendKeys(self._search_text,self._sp_incpage_search_field, locatorType="xpath")

    def searchSPCreateIncidentFromTicketForm(self):
        self.waitForElement(self._sp_ticketfm_search_field, locatorType="xpath")
        self.sendKeys(self._search_text, self._sp_ticketfm_search_field, locatorType="xpath")

    def clickSPCreateIncidentFromIncPage(self):
        self.waitForElement(self._sp_incpage_create_new_incident, locatorType="xpath")
        self.elementClick(self._sp_incpage_create_new_incident, locatorType="xpath")

    def loadSPCreateIncidentFromIncPage(self):
        self.searchSPCreateIncidentFromIncPage()
        self.clickSPCreateIncidentFromIncPage()

    def loadSPCreateIncidentFromTicketForm(self):
        self.waitForElement(self._sp_ticketfm_search_field,locatorType="xpath", timeout=50)
        self.searchSPCreateIncidentFromTicketForm()
        self.clickSPCreateIncident()
