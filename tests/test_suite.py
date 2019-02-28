import unittest
from tests.incident.createincident_tests import CreateIncidentTests
from tests.sportal_incident.sportal_createincident_tests import SPCreateIncidentTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(CreateIncidentTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SPCreateIncidentTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)