import pytest
from appium.webdriver import Remote
from todoist.api import TodoistAPI


class BaseTestCase:

    def setup_method(self, method):
        capabilities = dict()
        capabilities['app'] = pytest.config.getoption('apk')
        capabilities['deviceName'] = 'nexus_6'
        capabilities['platformName'] = 'Android'
        capabilities['appiumVersion'] = '1.7.2'
        capabilities['platformVersion'] = '8.0'
        capabilities['newCommandTimeout'] = 600
        capabilities['automationName'] = 'UiAutomator2'
        capabilities['appWaitActivity'] = 'com.todoist.activity.WelcomeActivity'
        self.driver = Remote('http://localhost:4723/wd/hub', capabilities)
        self.driver.implicitly_wait(5)
        self.api = TodoistAPI('f2c945f22636b263da979b96d115e2a2e2a63a99')

    def teardown_method(self, method):
        self.driver.quit()
