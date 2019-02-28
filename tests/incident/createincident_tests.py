from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.incident.incident_page import CreateIncidentPage
from utilities.teststatus import TstStatus
import unittest
import pytest
from pages.home.navigate_page import NavigationPage
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class CreateIncidentTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.incpage = CreateIncidentPage(self.driver)
        self.tstatus = TstStatus(self.driver)
        self.navpage = NavigationPage(self.driver)

    # Run Test to Verify Caller is a mandatory field
    # @pytest.mark.run(order=3)
    # @data(*getCSVData("/Users/gayani/PycharmProjects/ServiceNowTestingFramework/data/verify_caller_testdata.csv"))
    # @unpack
    # def test_verifyCallerIsRequired(self, stateValue, shortDescValue):
    #     self.navpage.clickCreateIncident()
    #     self.incpage.createIncidentWithoutCaller(state=stateValue, short_desc=shortDescValue)
    #     result = self.incpage.readCallerErrorMessage()
    #     self.tstatus.markFinal("test_verifyCallerIsRequired", result,
    #                            "Caller field is mandatory to create Incident.")

    # Run Test to Verify Short Description is a mandatory field
    @pytest.mark.run(order=4)
    @data(*getCSVData("/Users/gayani/PycharmProjects/ServiceNowTestingFramework/data/verify_shortdesc_testdata.csv"))
    @unpack
    def test_verifyShortDescRequired(self, callerValue, stateValue):
        self.navpage.clickCreateIncident()
        self.incpage.createIncidentWithoutShortDesc(caller=callerValue, state=stateValue)
        result = self.incpage.readShortDescErrorMessage()
        self.tstatus.markFinal("test_verifyShortDescRequired", result,
                               "Short Description field is mandatory to create Incident.")


    # Run Valid Tests with different Incident States - New, In Progress...
    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/gayani/PycharmProjects/ServiceNowTestingFramework/data/incident_testdata.csv"))
    @unpack
    def test_validIncidentCreate(self, callerValue, categoryValue, subcategoryValue, bsnsSrvValue, configItemValue,
                                 contactTypeValue, stateValue, impactValue, urgencyValue, assignmentGrpValue,
                                 shortDescValue, descValue, commentValue, workNoteValue, parentIncValue,
                                 problemValue, changeReqValue, causeValue, codeValue, resolveByValue, onHoldValue,
                                 noteValue, state, buttonLayer):
        self.navpage.clickCreateIncident()
        self.incpage.createIncident(caller=callerValue, category=categoryValue, subcategory=subcategoryValue,
                                    bsns_srv=bsnsSrvValue,
                                    config_item=configItemValue, contact_type=contactTypeValue, state=stateValue,
                                    impact=impactValue,
                                    urgency=urgencyValue, assignment_grp=assignmentGrpValue,
                                    short_desc=shortDescValue,
                                    desc=descValue,
                                    comment=commentValue, work_note=workNoteValue, parent_inc=parentIncValue,
                                    problem=problemValue,
                                    change_req=changeReqValue, cause=causeValue, code=codeValue,
                                    resolve_by=resolveByValue,
                                    onhold_reason=onHoldValue, note=noteValue, btn_layer=buttonLayer)

        result = self.incpage.verifySubmitSuccessfull()
        self.tstatus.markFinal("test_validIncidentCreate", result,
                               "Incident Submit Successful Verification... State: " + state +
                               ". Clicked submit button in " + buttonLayer + " the layer")

    # Run Valid Tests with manually entered Incident Numbers with different number formats
    @pytest.mark.run(order=2)
    @data(*getCSVData("/Users/gayani/PycharmProjects/ServiceNowTestingFramework/data/manual_inc_num_testdata.csv"))
    @unpack
    def test_validIncidentCreateWithManualIncNumber(self, incNumValue, callerValue, stateValue, shortDescValue):
        self.navpage.clickCreateIncident()
        self.incpage.createIncidentWithManualIncNum(inc_number=incNumValue, caller=callerValue, state=stateValue,
                                                    short_desc=shortDescValue)
        result = self.incpage.verifySubmitSuccessfull()
        self.tstatus.markFinal("test_validIncidentCreateWithManualIncNumber", result,
                               "Incident Submit Successful Verification... Incident Number : " + incNumValue)



    # Run Test to Verify character limit of Incident Number field
    @pytest.mark.run(order=5)
    @data(*getCSVData("/Users/gayani/PycharmProjects/ServiceNowTestingFramework/data/verify_incnum_charlimit_testdata.csv"))
    @unpack
    def test_verifyCharacterLimitOfIncNumber(self, incNumberValue, callerValue, stateValue, shortDescValue):
        self.navpage.clickCreateIncident()
        self.incpage.createIncidentWithManualIncNum(inc_number=incNumberValue, caller=callerValue,
                                                    state=stateValue, short_desc=shortDescValue)
        result = self.incpage.verifySubmitSuccessfull()
        self.tstatus.markFinal("test_verifyCharacterLimitOfIncNumber", result,
                               "Short Description field is mandatory to create Incident.")

    # Run valid test to save resolved incidents
    @pytest.mark.run(order=6)
    @data(*getCSVData("/Users/gayani/PycharmProjects/ServiceNowTestingFramework/data/resolve_incident_testdata.csv"))
    @unpack
    def test_resolvedIncidentCreate(self, callerValue, stateValue, shortDesc, resCodeValue, resNoteValue, buttonLayer):
        self.navpage.clickCreateIncident()
        self.incpage.createResolvedIncident(caller=callerValue, state=stateValue, short_desc=shortDesc,
                                            res_code=resCodeValue, res_note=resNoteValue, btn_layer=buttonLayer)

        result = self.incpage.verifySubmitSuccessfull()
        self.tstatus.markFinal("test_resolvedIncidentCreate", result,
                               "Incident Resolved Successful Verification. Clicked button in " + buttonLayer + " the layer")

    # Verify Update button is hidden
    @pytest.mark.run(order=7)
    @data(*getCSVData("/Users/gayani/PycharmProjects/ServiceNowTestingFramework/data/button_layer_testdata.csv"))
    @unpack
    def test_verifyUpdateButtonIsHidden(self, layer):
        self.navpage.clickCreateIncident()
        result = self.incpage.verifyUpdateButtonIsHidden(layer=layer)

        if layer == "":
            layer = "bottom"

        self.tstatus.markFinal("test_verifyUpdateButtonIsHidden", result,
                               "Update Button Verification Successful. "
                               "Update Button in the " + layer + " layer is not visible")

    # Verify Close button is hidden
    @pytest.mark.run(order=8)
    @data(*getCSVData("/Users/gayani/PycharmProjects/ServiceNowTestingFramework/data/button_layer_testdata.csv"))
    @unpack
    def test_verifyCloseButtonIsHidden(self, layer):
        self.navpage.clickCreateIncident()
        result = self.incpage.verifyCloseButtonIsHidden(layer=layer)

        if layer == "":
            layer = "bottom"

        self.tstatus.markFinal("test_verifyCloseButtonIsHidden", result,
                               "Close Button Verification Successful. "
                               "Close Button in the " + layer + " layer is not visible")

    # Verify Delete button is hidden
    @pytest.mark.run(order=9)
    @data(*getCSVData("/Users/gayani/PycharmProjects/ServiceNowTestingFramework/data/button_layer_testdata.csv"))
    @unpack
    def test_verifyDeleteButtonIsHidden(self, layer):
        self.navpage.clickCreateIncident()
        result = self.incpage.verifyDeleteButtonIsHidden(layer=layer)

        if layer == "":
            layer = "bottom"

        self.tstatus.markFinal("test_verifyDeleteButtonIsHidden", result,
                               "Delete Button Verification Successful. "
                               "Delete Button in the " + layer + " layer is not visible")

