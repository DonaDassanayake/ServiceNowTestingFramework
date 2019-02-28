import pytest
from selenium import webdriver
from pages.login.login_page import LoginPage
from pages.login.sportal_login_page import SPLoginPage
from pages.home.home_page import HomePage
from pages.home.navigate_page import NavigationPage

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    baseURL = "https://dev70471.service-now.com/welcome.do"

    if browser == 'firefox':
        driver = webdriver.Firefox()
        # driver.maximize_window()
        # driver.implicitly_wait(3)

        driver.get(baseURL)
        print("Running tests on Firefox Browser")

    else:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        print("Running tests on Chrome Browser")

    lp = LoginPage(driver)
    lp.login("admin", "Gayani123")

    nav = NavigationPage(driver)
    nav.searchIncident()
    # hp = HomePage(driver)
    # hp.selectCreateIncident("Incident")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    # tear down
    driver.quit()
    print("Running one time tearDown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUpServicePortal(request, browser):
    print("Running one time setUp")
    baseURL = "https://dev70471.service-now.com/sp"

    if browser == 'firefox':
        driver = webdriver.Firefox()
        driver.get(baseURL)
        print("Running tests on Firefox Browser")

    else:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        print("Running tests on Chrome Browser")

    lp = SPLoginPage(driver)
    lp.login("admin", "Gayani123")

    nav = NavigationPage(driver)
    nav.loadSPCreateIncidentFromHome()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    # tear down
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
