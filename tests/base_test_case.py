import pytest
from appium.webdriver import Remote


class BaseTestCase:

    def setup_method(self, method):
        capabilities = dict()
        capabilities['app'] = pytest.config.getoption('apk')
        capabilities['deviceName'] = 'nexus_5'
        capabilities['platformName'] = 'Android'
        capabilities['appiumVersion'] = '1.7.2'
        capabilities['platformVersion'] = '7.1'
        capabilities['newCommandTimeout'] = 600
        capabilities['automationName'] = 'UiAutomator2'
        capabilities['appWaitActivity'] = 'com.todoist.activity.WelcomeActivity'
        self.driver = Remote('http://localhost:4723/wd/hub', capabilities)
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()
