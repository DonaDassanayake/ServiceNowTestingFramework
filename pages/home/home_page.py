from base.basepage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # Locators
    _search_field = "filter"
    _create_incident = "//div[@class='sn-widget-list-title'][contains(text(),'Create New')]"
    _create_newincident ="dead1309c611228701e2bda7b4252474"
    _create_new = "//div[@class='sn-widget-list-title'][contains(text(),'Create New')]"
    _locator = "//a[@id='14641d70c611228501114133b3cc88a1']"


    # Set values
    def searchIncident(self, searchText):
        #wait until _serch_field
        self.waitForElement(self._search_field, timeout=20)
        #self.isElementPresent(self._search_field)
        self.sendKeys(searchText, self._search_field)

    def clickCreateIncident(self):
        self.waitForElement(self._locator)
        self.elementClick(self._locator, locatorType="xpath")

    def selectCreateIncident(self, searchText=""):
        self.searchIncident(searchText)
        self.clickCreateIncident()
