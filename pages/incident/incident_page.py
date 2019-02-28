
import time
from base.basepage import BasePage


class CreateIncidentPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # Frames
    _frame_id = "gsft_main"

    ###
    # Locators
    ###

    #Fields
    _number_field = "incident.number"
    _caller_search_button = "lookup.incident.caller_id"
    _caller_field = "sys_display.incident.caller_id"
    _b_service_field = "sys_display.incident.business_service"
    _configitem_field = "sys_display.incident.cmdb_ci"
    _priority_field = "incident.priority"
    _assignmentgrp_field = "sys_display.incident.assignment_group"
    _shortdesc_field = "incident.short_description"
    _description_field = "incident.description"
    _comments_field = "incident.comments"
    _worknotes_field = "incident.work_notes"
    _parent_inc_field = "sys_display.incident.parent_incident"
    _problem_field = "sys_display.incident.problem_id"
    _change_req_field = "sys_display.incident.rfc"
    _causeby_field = "sys_display.incident.caused_by"
    _knw_checkbox = "label.ni.incident.knowledge"
    _res_notes_field = "incident.close_notes"
    _res_by = "sys_display.incident.resolved_by"
    _res_date_field = "incident.resolved_at"
    _res_date_calender = "//span[@class='icon-calendar icon']"
    _res_calender_ok_btn = "GwtDateTimePicker_ok"
    _hold_reason_field = "incident.hold_reason"

    # Drop Down Lists
    _category_list = "incident.category"
    _subcategory_list = "incident.subcategory"
    _contacttype_list = "incident.contact_type"
    _state_list = "incident.state"
    _impact_list = "incident.impact"
    _urgency_list = "incident.urgency"
    _res_code_list = "incident.close_code"
    _on_hold_reason_list = "incident.hold_reason"

    # Tabs
    _notes_tab = "//span[contains(text(),'Notes')]"
    _related_records_tab = "//span[contains(text(),'Related Records')]"
    _res_info_tab = "//span[contains(text(),'Resolution Information')]"

    # Buttons
    _submit_button_bottom = "//div[@class='form_action_button_container']//button[@id='sysverb_insert']"
    _resolve_button_bottom = "//div[@class='form_action_button_container']//button[@id='resolve_incident']"
    _submit_button_top = "//span[@class='navbar_ui_actions']//button[@id='sysverb_insert']"
    _resolve_button_top = "//span[@class='navbar_ui_actions']//button[@id='resolve_incident']"
    _attachment_button = "header_add_attachment"
    _attachfile_button = "attachFile"
    _addme_watchlist_button = "add_me_locked.incident.watch_list"
    _addme_worknote_button = "add_me_locked.incident.work_notes_list"
    _update_button_bottom ="//div[@class='form_action_button_container']//button[@id='sysverb_update']"
    _update_button_top="//span[@class='navbar_ui_actions']//button[@id='sysverb_update']"
    _close_button_bottom ="//div[@class='form_action_button_container']//button[@id='close_incident']"
    _close_button_top="//span[@class='navbar_ui_actions']//button[@id='close_incident']"
    _delete_button_bottom="//div[contains(@class,'form_action_button_container')]//button[@id='sysverb_delete']"
    _delete_button_top="//span[@class='navbar_ui_actions']//button[@id='sysverb_delete']"

    # Search Buttons
    _b_service_search_button = "lookup.incident.business_service"
    _configitem_search_button = "lookup.incident.cmdb_ci"
    _assignmentgrp_search_button = "lookup.incident.assignment_group"
    _parent_inc_search_button = "lookup.incident.parent_incident"
    _searchresult_button = "cxs_maximize_results"
    _problem_search_button = "lookup.incident.problem_id"
    _change_req_search_button = "lookup.incident.rfc"
    _causeby_button = "lookup.incident.caused_by"
    _res_by_search_button = "lookup.incident.resolved_by"

    # Windows
    _caller_window = "show_incidents_2c5e54ebdb2323000c090181ca961998:incident.caller_id"

    # Verification Fields
    _nav_bar = "list_nav_incident"
    _error_msg = "output_messages"


    # Set values
    def clickCallerSearchOption(self):
        # Set values using customized Selenium class
        self.waitForElement(self._caller_search_button, timeout=20)
        self.elementClick(self._caller_search_button)

    def selectCaller(self, caller):
        self.waitForElement(caller, locatorType="xpath")
        self.elementClick(caller, locatorType="xpath")

    def enterCallerValue(self, caller):
        self.waitForElement(self._caller_field)
        self.sendKeys(caller, self._caller_field)
        self.pressTabKey()

    def setCallerValue(self, caller):
        self.waitForElement(self._caller_field)
        self.sendKeys(caller, self._caller_value)

    def selectCategory(self, category):
        self.waitForElement(self._category_list)
        self.elementClick(self._category_list)
        self.waitForElement(category)
        self.elementClick(category, locatorType="xpath")

    def selectSubCategory(self, subcategory):
        self.waitForElement(self._subcategory_list)
        self.elementClick(self._subcategory_list)
        self.elementClick(subcategory, locatorType="xpath")

    def clickBsnsServiceSearchBtn(self):
        self.elementClick(self._b_service_search_button)

    def selectBsnsService(self, bsns_srv):
        self.frame_switch(self._frame_id)
        self.window_switch_select_value(self._b_service_search_button, self._frame_id, bsns_srv, locatorType="xpath")

    def enterBsnsService(self, service):
        self.waitForElement(self._b_service_field)
        self.sendKeys(service, self._b_service_field)

    def clickConfigItemSearchBtn(self):
        self.elementClick(self._configitem_search_button)

    def selectConfigItem(self):
        self.elementClick(self._config_item_valuef, locatorType="xpath")

    def enterConfigItem(self, config_item):
        self.waitForElement(self._configitem_field)
        self.sendKeys(config_item, self._configitem_field)

    def selectContactType(self, contacttype):
        self.waitForElement(self._contacttype_list)
        self.elementClick(self._contacttype_list)
        self.waitForElement(contacttype, locatorType="xpath")
        self.elementClick(contacttype, locatorType="xpath")

    def selectState(self, state):
        self.waitForElement(self._state_list)
        self.elementClick(self._state_list)
        self.waitForElement(state, locatorType="xpath" )
        self.elementClick(state, locatorType="xpath")

    def selectImpact(self, impact):
        self.waitForElement(self._impact_list)
        self.elementClick(self._impact_list)
        self.elementClick(impact, locatorType="xpath")

    def selectUrgency(self, urgency):
        self.waitForElement(self._urgency_list)
        self.elementClick(self._urgency_list)
        self.elementClick(urgency, locatorType="xpath")

    def clickAssigmentGrpSearchBtn(self):
        self.elementClick(self._assignmentgrp_search_button)

    def selectAssignmentGrp(self):
        self.elementClick(self._assignmentgrp_value, locatorType="xpath")

    def enterAssignmentGrp(self, group):
        self.waitForElement(self._assignmentgrp_field)
        self.sendKeys(group, self._assignmentgrp_field)

    def enterShortDesc(self, shortDescription):
        self.waitForElement(self._shortdesc_field)
        self.sendKeys(shortDescription, self._shortdesc_field)

    def enterDescription(self, description):
        self.waitForElement(self._description_field)
        self.sendKeys(description, self._description_field)

    def selectNotesTab(self):
        self.waitForElement(self._notes_tab)
        self.elementClick(self._notes_tab, locatorType="xpath")

    def clickAddMeWatchList(self):
        self.waitForElement(self._addme_watchlist_button)
        self.elementClick(self._addme_watchlist_button)

    def clickAddMeWorkNotes(self):
        self.waitForElement(self._addme_worknote_button)
        self.elementClick(self._addme_worknote_button)

    def enterAdditionalComments(self, comments):
        self.waitForElement(self._comments_field)
        self.sendKeys(comments, self._comments_field)

    def enterWorkNotes(self, worknotes):
        self.waitForElement(self._worknotes_field)
        self.sendKeys(worknotes, self._worknotes_field)

    def clickRelRecordsTab(self):
        self.waitForElement(self._related_records_tab)
        self.elementClick(self._related_records_tab, locatorType="xpath")

    def clickParentIncSearchBtn(self):
        self.elementClick(self._parent_inc_search_button)

    def selectParentInc(self):
        self.elementClick(self._parent_inc_value, locatorType="xpath")

    def enterParentInc(self, parent_inc):
        self.waitForElement(self._parent_inc_field)
        self.sendKeys(parent_inc, self._parent_inc_field)

    def clickProbSearchBtn(self):
        self.elementClick(self._problem_search_button)

    def selectProblem(self):
        self.elementClick(self._problem_value, locatorType="xpath")

    def enterProblem(self, problem):
        self.waitForElement(self._problem_field)
        self.sendKeys(problem, self._problem_field)

    def clickChangeReqSearchBtn(self):
        self.elementClick(self._change_req_search_button)

    def selectChangeReq(self):
        self.elementClick(self._change_req_value, locatorType="xpath")

    def enterChangeReq(self, request):
        self.waitForElement(self._change_req_field)
        self.sendKeys(request, self._change_req_field)

    def clickCauseByChangeSearchBtn(self):
        self.elementClick(self._causeby_button)

    def selectCauseBy(self):
        self.elementClick(self._change_causeby_value, locatorType="xpath")

    def enterCauseBy(self, cause_by):
        self.waitForElement(self._causeby_field)
        self.sendKeys(cause_by, self._causeby_field)

    def clickResolutionTab(self):
        self.waitForElement(self._res_info_tab)
        self.elementClick(self._res_info_tab, locatorType="xpath")

    def clickKnowledgeCheckBox(self):
        self.waitForElement(self._knw_checkbox)
        self.elementClick(self._knw_checkbox)

    def selectResCode(self, code):
        self.waitForElement(self._res_code_list)
        self.elementClick(self._res_code_list)
        self.elementClick(code, locatorType="xpath")

    def enterResolveBy(self, by):
        self.waitForElement(self._res_by)
        self.sendKeys(by, self._res_by)

    def enterResDate(self):
        self.waitForElement(self._res_date_calender, locatorType="xpath")
        self.elementClick(self._res_date_calender, locatorType="xpath")
        self.waitForElement(self._res_calender_ok_btn)
        self.elementClick(self._res_calender_ok_btn)

    def enterResNotes(self, note):
        self.waitForElement(self._res_notes_field)
        self.sendKeys(note, self._res_notes_field)

    def clickSubmitBottom(self):
        self.waitForElement(self._submit_button_bottom, locatorType="xpath")
        self.elementClick(self._submit_button_bottom, locatorType="xpath")

    def clickResolveButtonBottom(self):
        self.waitForElement(self._resolve_button_bottom, locatorType="xpath")
        self.elementClick(self._resolve_button_bottom, locatorType="xpath")

    def clickSubmitTop(self):
        self.waitForElement(self._submit_button_top, locatorType="xpath")
        self.elementClick(self._submit_button_top, locatorType="xpath")

    def clickResolveButtonTop(self):
        self.waitForElement(self._resolve_button_top, locatorType="xpath")
        self.elementClick(self._resolve_button_top, locatorType="xpath")

    def selectOnHoldReason(self, reason):
        if self.isElementPresent(self._on_hold_reason_list) is True:
            self.waitForElement(self._on_hold_reason_list)
            self.elementClick(self._on_hold_reason_list)
            self.waitForElement(reason, locatorType="xpath")
            self.elementClick(reason, locatorType="xpath")

    def enterIncNumber(self, number):
        self.waitForElement(self._number_field)
        self.sendKeys(number, self._number_field)


    ###
    # Get field values
    ###
    def getStateValue(self):
        self.waitForElement(self._state_list)
        self.getText(self._state_list)

    def getIncNumber(self):
        self.waitForElement(self._number_field)
        self.getText(self._number_field)

    # Create incident
    def createIncident(self, caller="", category="", subcategory="", bsns_srv="", config_item="",
                         contact_type="", state="", impact="", urgency="", assignment_grp="",
                         short_desc="", desc= "", comment="", work_note="", parent_inc="", problem="",
                         change_req="", cause="", code="", resolve_by="", note="", onhold_reason="", btn_layer="bottom" ):

        # Switch to frame which contains the form
        self.frame_switch(self._frame_id)

        # self.changeWindow(caller)
        # self.frame_switch(self._frame_id)
        # Call common funcation to select Caller value from Pop up window
        self.window_switch_select_value(self._caller_search_button, self._frame_id, caller, locatorType="xpath")

        self.selectCategory(category)
        self.selectSubCategory(subcategory)
        self.window_switch_select_value(self._b_service_search_button, self._frame_id, bsns_srv, locatorType="xpath")
        self.window_switch_select_value(self._configitem_search_button, self._frame_id, config_item, locatorType="xpath")
        self.selectContactType(contact_type)
        self.selectState(state)
        self.selectOnHoldReason(onhold_reason)
        self.selectImpact(impact)
        self.selectUrgency(urgency)
        self.window_switch_select_value(self._assignmentgrp_search_button, self._frame_id, assignment_grp, locatorType="xpath")
        self.enterShortDesc(short_desc)
        self.enterDescription(desc)
        self.selectNotesTab()
        self.clickAddMeWatchList()
        self.clickAddMeWorkNotes()
        self.enterAdditionalComments(comment)
        self.enterWorkNotes(work_note)
        self.clickRelRecordsTab()
        self.window_switch_select_value(self._parent_inc_search_button, self._frame_id, parent_inc, locatorType="xpath")
        self.window_switch_select_value(self._problem_search_button, self._frame_id, problem, locatorType="xpath")
        self.window_switch_select_value(self._change_req_search_button, self._frame_id, change_req, locatorType="xpath")
        self.window_switch_select_value(self._causeby_button, self._frame_id, cause, locatorType="xpath")
        self.clickResolutionTab()
        self.clickKnowledgeCheckBox()
        self.selectResCode(code)
        self.window_switch_select_value(self._res_by_search_button, self._frame_id, resolve_by, locatorType="xpath")
        self.enterResDate()
        self.enterResNotes(note)

        if btn_layer == "top":
            self.clickSubmitTop()
        else:
            self.clickSubmitBottom()

    # Create incident
    def createIncidentWithManualIncNum(self, inc_number="", caller="", state="", short_desc=""):
        # Switch to frame which contains the form
        self.frame_switch(self._frame_id)

        self.enterIncNumber(inc_number)
        self.window_switch_select_value(self._caller_search_button, self._frame_id, caller, locatorType="xpath")
        self.selectState(state)
        self.enterShortDesc(short_desc)
        self.clickSubmitBottom()

    # Try to create incident without caller
    def createIncidentWithoutCaller(self, state="", short_desc=""):
        # Switch to frame which contains the form
        self.frame_switch(self._frame_id)

        self.selectState(state)
        self.enterShortDesc(short_desc)
        self.clickSubmitBottom()

    def createIncidentWithoutShortDesc(self, caller="", state=""):
        # Switch to frame which contains the form
        self.frame_switch(self._frame_id)
        self.window_switch_select_value(self._caller_search_button, self._frame_id, caller, locatorType="xpath")
        self.selectState(state)
        self.clickSubmitBottom()

    def createResolvedIncident(self, caller="", state="", short_desc="", res_code="", res_note="", btn_layer="bottom"):
        # Switch to frame which contains the form
        self.frame_switch(self._frame_id)
        self.window_switch_select_value(self._caller_search_button, self._frame_id, caller, locatorType="xpath")
        self.selectState(state)
        self.enterShortDesc(short_desc)
        self.webScroll(direction="down")
        self.clickResolutionTab()
        self.selectResCode(res_code)
        self.enterResDate()
        self.enterResNotes(res_note)
        if btn_layer == "top":
            self.clickResolveButtonTop()
        else:
            self.clickResolveButtonBottom()

    def verifySubmitSuccessfull(self):
        navigationElement = self.waitForElement(self._nav_bar)
        result = self.isElementDisplayed(element=navigationElement)
        self.frame_switchback_main()
        return result

    def readCallerErrorMessage(self):
        self.waitForElement(self._error_msg)
        message = self.getText(self._error_msg)
        expectedMessage = "The following mandatory fields are not filled in: Caller"

        self.log.info("Message = " + message)
        self.log.info("Expected Message = " + expectedMessage)

        if expectedMessage in message:
            result = True
        else:
            result = False

        self.driver.switchTo().alert().accept()
        self.frame_switchback_main()

        return result

    def readShortDescErrorMessage(self):
        self.waitForElement(self._error_msg)
        message = self.getText(self._error_msg)
        expectedMessage = "The following mandatory fields are not filled in: Short description"

        self.log.info("Message = " + message)
        self.log.info("Expected Message = " + expectedMessage)

        if expectedMessage in message:
            result = True
        else:
            result = False

        self.frame_switchback_main()

        return result

    def verifyUpdateButtonIsHidden(self, layer="bottom"):
        # Switch to frame which contains the form
        self.frame_switch(self._frame_id)
        # Check the update button is visible
        if layer == "top":
            # If the update button is NOT visible, this will return False
            if self.isElementDisplayed(self._update_button_top, locatorType="xpath") is False:
                self.frame_switchback_main()
                return True
            else:
                self.frame_switchback_main()
                return False
        else:
            if self.isElementDisplayed(self._update_button_bottom, locatorType="xpath") is False:
                self.frame_switchback_main()
                return True
            else:
                self.frame_switchback_main()
                return False

    def verifyCloseButtonIsHidden(self, layer="bottom"):
        # Switch to frame which contains the form
        self.frame_switch(self._frame_id)
        # Check the Close button is visible
        if layer=="top":
            # If the close button is NOT visible, this will return False
            if self.isElementDisplayed(self._close_button_top, locatorType="xpath") is False:
                self.frame_switchback_main()
                return True
            else:
                self.frame_switchback_main()
                return False
        else:
            if self.isElementDisplayed(self._close_button_bottom, locatorType="xpath") is False:
                self.frame_switchback_main()
                return True
            else:
                self.frame_switchback_main()
                return False

    def verifyDeleteButtonIsHidden(self, layer="bottom"):
        # Switch to frame which contains the form
        self.frame_switch(self._frame_id)
        # Check the Delete button is visible
        if layer == "top":
            # If the Delete button is NOT visible, this will return False
            if self.isElementDisplayed(self._delete_button_top, locatorType="xpath") is False:
                self.frame_switchback_main()
                return True
            else:
                self.frame_switchback_main()
                return False
        else:
            if self.isElementDisplayed(self._delete_button_bottom, locatorType="xpath") is False:
                self.frame_switchback_main()
                return True
            else:
                self.frame_switchback_main()
                return False

