class BaseElement:

    def __init__(self, driver, locator_by, locator_value):
        self.driver = driver
        self.locator_by = locator_by
        self.locator_value = locator_value

    def find_element(self):
        return self.driver.find_element(self.locator_by, self.locator_value)


class BaseButton(BaseElement):
    def __init__(self, driver, locator_by, locator_value, return_view=None):
        super(BaseButton, self).__init__(driver, locator_by, locator_value)
        self.return_view = return_view

    def click(self):
        self.find_element().click()
        return self.return_view


class BaseEditBox(BaseElement):

    def __init__(self, driver, locator_by, locator_value):
        super(BaseEditBox, self).__init__(driver, locator_by, locator_value)

    def set_value(self, value):
        self.find_element().set_value(value)
