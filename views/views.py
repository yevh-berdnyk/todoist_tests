from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from views.base_element import BaseButton, BaseEditBox


class BaseView:
    def __init__(self, driver):
        self.driver = driver
        self.ok_button = BaseButton(driver=driver, locator_by=MobileBy.XPATH, locator_value="//*[@text='OK']")

    def find_full_text(self, exp_text):
        try:
            cond = expected_conditions.visibility_of_element_located((MobileBy.XPATH, "//*[@text='%s']" % exp_text))
            return WebDriverWait(self.driver, 20).until(cond)
        except TimeoutException:
            raise TimeoutException("Text '%s' was not found" % exp_text) from None


class SignInView(BaseView):

    def __init__(self, driver):
        super(SignInView, self).__init__(driver)
        self.welcome_by_email_button = BaseButton(driver=driver, locator_by=MobileBy.ID,
                                                  locator_value='com.todoist:id/btn_welcome_continue_with_email')
        self.email_input = BaseEditBox(driver=driver, locator_by=MobileBy.ID,
                                       locator_value='com.todoist:id/email_exists_input')
        self.continue_with_email_button = BaseButton(driver=driver, locator_by=MobileBy.ID,
                                                     locator_value='com.todoist:id/btn_continue_with_email')
        self.login_password_button = BaseEditBox(driver=driver, locator_by=MobileBy.ID,
                                                 locator_value='com.todoist:id/log_in_password')
        self.login_button = BaseButton(driver=driver, locator_by=MobileBy.ID, locator_value='com.todoist:id/btn_log_in',
                                       return_view=HomeView(self.driver))


class HomeView(BaseView):
    def __init__(self, driver):
        super(HomeView, self).__init__(driver)
        self.driver = driver
        self.change_view_button = BaseButton(driver=driver, locator_by=MobileBy.ACCESSIBILITY_ID,
                                             locator_value='Change the current view')

    def get_item_by_name(self, item_name):
        return BaseButton(self.driver, MobileBy.XPATH, "//*[@text='%s']" % item_name)