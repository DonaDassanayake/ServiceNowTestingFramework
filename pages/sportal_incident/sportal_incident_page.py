

from base.basepage import BasePage


class SPCreateIncidentPage(BasePage):
    def __init__(self, driver):
        self.driver = driver


    # Frames
    _frame_id = "gsft_main"

    ###
    # Locators
    ###

    _urgency_dropdown = "//*[@id='s2id_sp_formfield_{{::field.name}}']"
    #"select2-drop"#"//span[contains(text(), 'select2-arrow')]"#"//*[@id='select2-choice']" #"//div[@class='select2-drop']"
    _description_field = "//textarea[@id='sp_formfield_comments']"

    _message_field = "//textarea[@id='post-input']"

    # Links
    _addattachment_link = "//span[contains(text(),'Add attachments')]"
    _home = "//a[contains(@ng-href,'?id=index')]"

    # Buttons
    _addattachment_button = "//input[@type='file']"
    _attachmentbtn_top_ticketform = "//sp-attachment-button[@class='ng-scope']//input[@type='file']"
    _attachmentbtn_bottom_ticketform = "//div[@class='ng-scope']//input[@type='file']"
    _submit_button = "//button[@name='submit']"
    _send_button = "//input[@type='submit' and @value='Send']"

    # Verification elements
    _timeline = "//ul[@class='timeline']"
    _location = "x29af3d50d7000200a9ad1e173e24d4d7"
    _submit_message = "//span[contains(text(),'Your request has been submitted')]"

    _error_msg = "//span[contains(text(),'Measure of the business criticality based on the i')]"
    _error_msg_desc = "//span[contains(text(),'The more information you can provide here, the eas')]"

    _dropdown_search = "//*[@class='select2-input']"
    _dropdown_value = "//span[contains(@class, 'select2-results') and text() = '3 - Low']"

    def clickUrgency(self):
        self.waitForElement(self._urgency_dropdown, locatorType="xpath")
        self.elementClick(self._urgency_dropdown, locatorType="xpath")

    def selectUrgency(self, urgency_value):
        self.waitForElement(urgency_value, locatorType="xpath")
        self.elementClick(urgency_value, locatorType="xpath")

    def enterDescription(self, desc):
        self.waitForElement(self._description_field, locatorType="xpath")
        self.sendKeys(desc, self._description_field, locatorType="xpath")

    def clickSubmit(self):
        self.waitForElement(self._submit_button, locatorType="xpath")
        self.elementClick(self._submit_button, locatorType="xpath")

    # def addAttachement(self, location):
    #     self.waitForElement(self._addattachment_button, locatorType="xpath")
    #     self.elementClick(self._addattachment_button, locatorType="xpath")

    def enterMessage(self, message):
        self.waitForElement(self._message_field,locatorType="xpath")
        self.sendKeys(message,self._message_field, locatorType="xpath")

    def clickSendButton(self):
        self.waitForElement(self._send_button, locatorType="xpath")
        self.elementClick(self._send_button, locatorType="xpath")

    def loadHome(self):

        self.waitForElement(self._home, locatorType="xpath")
        self.elementClick(self._home, locatorType="xpath")

    def selectAttachmentUsingButton(self, attachmentLoc):
        self.waitForElement(self._addattachment_button,locatorType="xpath")
        self.sendKeys(attachmentLoc,self._addattachment_button,
                      locatorType="xpath")

    def selectAttachmentUsingLink(self, attachmentLoc):
        self.waitForElement(self._addattachment_link,locatorType="xpath")
        self.sendKeys(attachmentLoc,self._addattachment_link,
                      locatorType="xpath")

    def selectAttachmentUsingBtnTopTicketForm(self, attachmentLoc):
        self.waitForElement(self._addattachment_link,locatorType="xpath")
        self.sendKeys(attachmentLoc,self._attachmentbtn_top_ticketform,
                      locatorType="xpath")

    def selectAttachmentUsingBtnBottomTicketForm(self, attachmentLoc):
        self.waitForElement(self._addattachment_link,locatorType="xpath")
        self.sendKeys(attachmentLoc,self._attachmentbtn_bottom_ticketform,
                      locatorType="xpath")


    def createSPIncident(self, urgency, description):
        self.clickUrgency()
        self.selectUrgency(urgency)
        self.enterDescription(description)
        self.clickSubmit()
        self.webScroll("up")

    def createSPIncidentWithAttachement(self, urgency, description, attachmentLocation):
        self.clickUrgency()
        self.selectUrgency(urgency)
        self.enterDescription(description)
        self.selectAttachmentUsingButton(attachmentLocation)
        self.clickSubmit()
        self.webScroll("up")

    def createSPIncidentWithMessage(self, urgency, description, message):
        self.clickUrgency()
        self.selectUrgency(urgency)
        self.enterDescription(description)
        self.clickSubmit()
        self.webScroll("up")
        self.enterMessage(message)
        self.clickSendButton()
        self.webScroll("up")

    def createSPIncidentWithMsgAndAttachement(self, urgency, description, message, attachmentLocation):
        self.clickUrgency()
        self.selectUrgency(urgency)
        self.enterDescription(description)
        self.selectAttachmentUsingButton(attachmentLocation)
        self.clickSubmit()
        self.webScroll("up")
        self.enterMessage(message)
        self.clickSendButton()
        self.webScroll("up")

    def selectUrgencyUsingDropdownSearch(self, urgency, description):
        self.clickUrgency()
        self.selectFromUrgenecyDropDown(urgency)
        self.enterDescription(description)
        self.clickSubmit()
        self.webScroll("up")

    def addAttachmentUsingLink(self, urgency, description, attachmentLocation):
        self.clickUrgency()
        self.selectUrgency(urgency)
        self.enterDescription(description)
        self.selectAttachmentUsingLink(attachmentLocation)
        self.clickSubmit()
        self.webScroll("up")

    def addAttachmentUsingBtnInTopTicketForm(self, urgency, description, attachmentLocation):
        self.clickUrgency()
        self.selectUrgency(urgency)
        self.enterDescription(description)
        self.clickSubmit()
        self.webScroll("up")
        self.selectAttachmentUsingBtnTopTicketForm(attachmentLocation)
        self.webScroll("up")

    def addAttachmentUsingBtnInBottomTicketForm(self, urgency, description, attachmentLocation):
        self.clickUrgency()
        self.selectUrgency(urgency)
        self.enterDescription(description)
        self.clickSubmit()
        self.webScroll("up")
        self.selectAttachmentUsingBtnBottomTicketForm(attachmentLocation)
        self.webScroll("up")


    def verifyUrgencyIsRequired(self, description):
        self.enterDescription(description)
        self.clickSubmit()

    def readUrgencyErrorMessage(self):
        self.waitForElement(self._error_msg, locatorType="xpath")

        if self.isElementDisplayed(self._error_msg, locatorType="xpath") is False:
            result = False
        else:
            result = True
        return result

    def readDescriptionErrorMessage(self):
        self.waitForElement(self._error_msg_desc, locatorType="xpath")

        if self.isElementDisplayed(self._error_msg_desc, locatorType="xpath") is False:
            result = False
        else:
            result = True
        return result

    def verifySubmitSuccessfull(self):
        self.waitForElement(self._location)
        if self.isElementDisplayed(self._location) is False:
            return False
        else:
            return True

    def verifyDescriptionIsRequired(self, urgency):
        self.clickUrgency()
        self.selectUrgency(urgency)
        self.clickSubmit()


    def selectFromUrgenecyDropDown(self, urgValue):
        self.waitForElement(self._dropdown_search, locatorType="xpath")
        self.sendKeys(urgValue, self._dropdown_search, locatorType="xpath")
        self.pressEnterKey()



