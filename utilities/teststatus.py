"""
To provide functionality to Assertion
"""

from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as CLogger
import logging


class TstStatus(SeleniumDriver):

    log = CLogger.customLogger(logging.INFO)

    def __init__(self, driver):
        super(TstStatus, self).__init__(driver)
        # Using a list to keep track of the all the results
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.info("### Exception Occurred !!!")

    def mark(self, result, resultMessage):
        self.setResult(result,resultMessage)

    def markFinal(self, testName, result, resultMessage):
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName + " ### TEST FALIED ")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName+ " ### Test Passed ")
            self.resultList.clear()
            assert True == True
