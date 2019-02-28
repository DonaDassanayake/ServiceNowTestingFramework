from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.sportal_incident.sportal_incident_page import SPCreateIncidentPage
from utilities.teststatus import TstStatus
import unittest
import pytest
from pages.home.navigate_page import NavigationPage
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUpServicePortal", "setUp")
@ddt
class SPCreateIncidentTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUpServicePortal):
        self.incpage = SPCreateIncidentPage(self.driver)
        self.tstatus = TstStatus(self.driver)
        self.navpage = NavigationPage(self.driver)

    #Run Valid Test to create Service Portal Incident
    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/gayani/PycharmProjects/ServiceNowTestingFramework/data/sportal_incidentdata/sp_incident_testdata.csv"))
    @unpack
    def test_sp_createincident(self,urgencyValue, descValue):
        if self.navpage.isMainSearchVisible() is False:
            self.incpage.loadHome()
            self.navpage.loadSPCreateIncidentFromHome()
        self.incpage.createSPIncident(urgency=urgencyValue, description=descValue)
        result = self.incpage.verifySubmitSuccessfull()
        self.tstatus.markFinal("test_sp_createincident", result,
                               "Incident Submit Successful Verification...")

    # Run valid test to create a Service Portal Incident with an attachment
    @pytest.mark.run(order=2)
    @data(*getCSVData("/Users/gayani/PycharmProjects/ServiceNowTestingFramework/data/sportal_incidentdata/sp_incident_testdata_with_attachment.csv"))
    @unpack
    def test_sp_createincidentWithAttachement(self, urgencyValue, descValue, attachmentLoc):
        if self.navpage.isMainSearchVisible() is False:
            self.incpage.loadHome()
            self.navpage.loadSPCreateIncidentFromHome()
        self.incpage.createSPIncidentWithAttachement(urgency=urgencyValue, description=descValue,
                                                           attachmentLocation=attachmentLoc)
        result = self.incpage.verifySubmitSuccessfull()
        self.tstatus.markFinal("test_sp_createincidentWithAttachement", result,
                               "Incident Submit Successful Verification...")

    # Run valid test to create a Service Portal Incident and add Message
    @pytest.mark.run(order=3)
    @data(*getCSVData("/Users/gayani/PycharmProjects/ServiceNowTestingFramework/data/sportal_incidentdata/sp_incident_testdata_with_message.csv"))
    @unpack
    def test_sp_createincidentWithMsg(self, urgencyValue, descValue, messageValue):
        if self.navpage.isMainSearchVisible() is False:
            self.incpage.loadHome()
            self.navpage.loadSPCreateIncidentFromHome()
        self.incpage.createSPIncidentWithMessage(urgency=urgencyValue, description=descValue,
                                                           message=messageValue)
        result = self.incpage.verifySubmitSuccessfull()
        self.tstatus.markFinal("test_sp_createincidentWithMsg", result,
                               "Incident Submit Successful Verification...")

    # Run valid test to create a Service Portal Incident with an attachment and add Message
    @pytest.mark.run(order=4)
    @data(*getCSVData("/Users/gayani/PycharmProjects/ServiceNowTestingFramework/data/sportal_incidentdata/sp_incident_testdata_message_attachment.csv"))
    @unpack
    def test_sp_createincidentWithMsgAttachement(self, urgencyValue, descValue, messageValue, attachmentLoc):
        if self.navpage.isMainSearchVisible() is False:
            self.incpage.loadHome()
            self.navpage.loadSPCreateIncidentFromHome()
        self.incpage.createSPIncidentWithMsgAndAttachement(urgency=urgencyValue, description=descValue,
                                                           message=messageValue, attachmentLocation=attachmentLoc)
        result = self.incpage.verifySubmitSuccessfull()
        self.tstatus.markFinal("test_sp_createincidentWithMsgAttachement", result,
                               "Incident Submit Successful Verification...")


    # Verify Description is a required field
    @pytest.mark.run(order=5)
    def test_sp_verifyIsDescriptionRequired(self):
        if self.navpage.isMainSearchVisible() is False:
            self.incpage.loadHome()
            self.navpage.loadSPCreateIncidentFromHome()

        self.incpage.verifyDescriptionIsRequired(urgency="//*[@class='select2-result-label' and contains(text(),'High')]")
        result = self.incpage.readDescriptionErrorMessage()
        self.tstatus.markFinal("test_sp_verifyIsDescriptionRequired", result,
                               "Verification Successful...")

    # Verify Urgency is a required field
    @pytest.mark.run(order=6)
    def test_sp_verifyIsUrgencyRequired(self):
        if self.navpage.isMainSearchVisible() is False:
            self.incpage.loadHome()
            self.navpage.loadSPCreateIncidentFromHome()

        self.incpage.verifyUrgencyIsRequired(description="Email error")
        result= self.incpage.readUrgencyErrorMessage()
        self.tstatus.markFinal("test_sp_verifyIsUrgencyRequired", result,
                               "Verification Successful...")

    # # Select Urgency by typing on Search box of Urgency Drop down list
    @pytest.mark.run(order=7)
    def test_sp_addUrgencyUsingSearchbox(self):
        if self.navpage.isMainSearchVisible() is False:
            self.incpage.loadHome()
            self.navpage.loadSPCreateIncidentFromHome()

        self.incpage.selectUrgencyUsingDropdownSearch(urgency="Medium", description="Email error")
        result= self.incpage.verifySubmitSuccessfull()
        self.tstatus.markFinal("test_sp_addUrgencyUsingSearchbox", result,
                               "Verification Successful...")

    # Run valid test to add attachment using attachment Link in the Incident creating page
    @pytest.mark.run(order=8)
    @data(*getCSVData("/Users/gayani/PycharmProjects/ServiceNowTestingFramework/data/sportal_incidentdata/sp_incident_testdata_with_attachment.csv"))
    @unpack
    def test_sp_addAttachementUsingLinkIncPage(self, urgencyValue, descValue, attachmentLoc):
        if self.navpage.isMainSearchVisible() is False:
            self.incpage.loadHome()
            self.navpage.loadSPCreateIncidentFromHome()
        self.incpage.addAttachmentUsingLink(urgency=urgencyValue, description=descValue,
                                                     attachmentLocation=attachmentLoc)
        result = self.incpage.verifySubmitSuccessfull()
        self.tstatus.markFinal("test_sp_addAttachementUsingLinkIncPage", result,
                               "Incident Submit Successful Verification...")

    #Run valid test to add attachment using attachment Button in the top of the Ticket Form
    @pytest.mark.run(order=9)
    @data(*getCSVData("/Users/gayani/PycharmProjects/ServiceNowTestingFramework/data/sportal_incidentdata/sp_incident_testdata_with_attachment.csv"))
    @unpack
    def test_sp_addAttachementUsingTopBtnTicketForm(self, urgencyValue, descValue, attachmentLoc):
        if self.navpage.isMainSearchVisible() is False:
            self.incpage.loadHome()
            self.navpage.loadSPCreateIncidentFromHome()
        self.incpage.addAttachmentUsingBtnInTopTicketForm(urgency=urgencyValue, description=descValue,
                                            attachmentLocation=attachmentLoc)
        result = self.incpage.verifySubmitSuccessfull()
        self.tstatus.markFinal("test_sp_addAttachementUsingTopBtnTicketForm", result,
                               "Incident Submit Successful Verification...")

    # Run valid test to add attachment using attachment Button in the bottom of the Ticket Form
    @pytest.mark.run(order=8)
    @data(*getCSVData("/Users/gayani/PycharmProjects/ServiceNowTestingFramework/data/sportal_incidentdata/sp_incident_testdata_with_attachment.csv"))
    @unpack
    def test_sp_addAttachementUsingBottomBtnTicketForm(self, urgencyValue, descValue, attachmentLoc):
        if self.navpage.isMainSearchVisible() is False:
            self.incpage.loadHome()
            self.navpage.loadSPCreateIncidentFromHome()
        self.incpage.addAttachmentUsingBtnInBottomTicketForm(urgency=urgencyValue, description=descValue,
                                                     attachmentLocation=attachmentLoc)
        result = self.incpage.verifySubmitSuccessfull()
        self.tstatus.markFinal("test_sp_addAttachementUsingBottomBtnTicketForm", result,
                               "Incident Submit Successful Verification...")

