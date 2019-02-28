"""

Base Page class implementation
It implements methods which are common to all the pages of the application
This class needs to be inherited by all the page classes

"""
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
import time

class BasePage(SeleniumDriver):

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver

    # Switch to required frame using name
    def frame_switch(self, id):
        self.waitForElement(self.getElement(id))
        self.driver.switch_to.frame(self.getElement(id))
        #self.driver.switch_to.frame(self.driver.find_element_by_name(name))
        #self.driver.switch_to.frame(id)

    # Switch back to main frame
    def frame_switchback_main(self):
        self.driver.switch_to.default_content()

    # Switch to alert
    def alert_switch(self):
        self.driver.switch_to.alert()

    def window_switch_select_value(self, searchbutton ="", frameIdToSwitch="", locator="", locatorType="id"):
        # Find parent handle -> Main Window
        parentHandle = self.driver.current_window_handle
        self.log.info("Parent Handle: " + parentHandle)
        self.log.info("Parent Window Title : " + self.driver.title)

        # Find open window button and click it
        self.waitForElement(searchbutton)
        self.elementClick(searchbutton)

        time.sleep(10)

        # Find all handles
        handles = self.driver.window_handles

        # Switch to window and search course
        for handle in handles:
            self.log.info("Handle: " + handle)
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                self.log.info("Switched to window:: " + handle)
                self.log.info("Child Window Title : "+self.driver.title)
                self.waitForElement(locator, locatorType=locatorType)
                self.elementClick(locator, locatorType=locatorType)

                time.sleep(2)
                # self.driver.close()
                break

        # Switch back to the parent handle
        self.driver.switch_to.window(parentHandle)
        self.log.info("Switched to parent window" + parentHandle )
        self.log.info("Current Window Title : " + self.driver.title)
        self.frame_switch(frameIdToSwitch)

    """
    Verify the page title 
    """
    def verifyPageTitle(self, titleToVerify):
        try:
            actualTitle = self.getTitle()
            if actualTitle.lower() in titleToVerify.lower():
                self.log.info("### VERIFICATION CONTAINS !!!")
                return True
            else:
                self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
                return False

        except:
            self.log.error("Failed to get page title")
            #print_stack()
            return False
