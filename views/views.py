import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from views.base_element import BaseButton, BaseEditBox


class BaseView:
    def __init__(self, driver):
        self.driver = driver
        self.ok_button = BaseButton(driver, MobileBy.XPATH, "//*[@text='OK']")
        self.never_ask_button = BaseButton(driver, MobileBy.XPATH, "//*[@text='NEVER ASK']")

    def find_full_text(self, exp_text, wait_time=20):
        try:
            cond = expected_conditions.visibility_of_element_located((MobileBy.XPATH, "//*[@text='%s']" % exp_text))
            return WebDriverWait(self.driver, wait_time).until(cond)
        except TimeoutException:
            raise TimeoutException("Text '%s' was not found" % exp_text) from None

    def get_element_by_text(self, text):
        return BaseButton(self.driver, MobileBy.XPATH, "//*[@text='%s']" % text)

    def pull_to_refresh(self):
        self.driver.swipe(500, 500, 500, 1000)


class SignInView(BaseView):
    def __init__(self, driver):
        super(SignInView, self).__init__(driver)
        self.welcome_by_email_button = BaseButton(driver, MobileBy.ID, 'com.todoist:id/btn_welcome_continue_with_email')
        self.email_input = BaseEditBox(driver, MobileBy.ID, 'com.todoist:id/email_exists_input')
        self.continue_with_email_button = BaseButton(driver, MobileBy.ID, 'com.todoist:id/btn_continue_with_email')
        self.login_password_button = BaseEditBox(driver, MobileBy.ID, 'com.todoist:id/log_in_password')
        self.login_button = BaseButton(driver, MobileBy.ID, 'com.todoist:id/btn_log_in', HomeView(self.driver))

    def sign_in_with_email(self, email, password):
        if self.ok_button.is_visible():
            self.ok_button.click()
        self.welcome_by_email_button.click()
        self.email_input.set_value(email)
        self.continue_with_email_button.click()
        self.login_password_button.set_value(password)
        home_view = self.login_button.click()
        if self.ok_button.is_visible():
            self.ok_button.click()
        if home_view.never_ask_button.is_visible():
            home_view.never_ask_button.click()
        return home_view


class ListItem(BaseButton):
    def __init__(self, driver, locator_by, locator_value):
        super(BaseButton, self).__init__(driver, locator_by, locator_value)
        self.driver = driver
        self.return_view = None
        self.add_button = BaseButton(self.driver, locator_by, locator_value + "/../*[@content-desc='Add']",
                                     ProjectView(self.driver))


class HomeView(BaseView):
    def __init__(self, driver):
        super(HomeView, self).__init__(driver)
        self.driver = driver
        self.change_view_button = BaseButton(driver, MobileBy.ACCESSIBILITY_ID, 'Change the current view')
        self.plus_button = BaseButton(driver, MobileBy.ID, 'com.todoist:id/fab', TaskView(self.driver))

    def get_list_item_by_name(self, item_name):
        return ListItem(self.driver, MobileBy.XPATH, "//*[@text='%s']" % item_name)


class ProjectNameInput(BaseEditBox):
    def __init__(self, driver):
        super(ProjectNameInput, self).__init__(driver, MobileBy.ID, 'com.todoist:id/name')

    def set_value(self, value):
        time.sleep(3)  # temporary solution for StaleObjectException which appears
        # from time to time when setting value on the ProjectNameInput
        super(ProjectNameInput, self).set_value(value)


class ProjectView(BaseView):
    def __init__(self, driver):
        super(ProjectView, self).__init__(driver)
        self.project_name_input = ProjectNameInput(driver)
        self.submit_project_button = BaseButton(driver, MobileBy.ACCESSIBILITY_ID, 'Done')


class TaskView(BaseView):
    def __init__(self, driver):
        super(TaskView, self).__init__(driver)
        self.task_name_input = BaseEditBox(driver, MobileBy.ID, 'android:id/message')
        self.submit_task_button = BaseButton(driver, MobileBy.ID, 'android:id/button1')
        self.complete_button = BaseButton(driver, MobileBy.ACCESSIBILITY_ID, 'Complete')
