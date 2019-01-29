import time

import random
import string
from todoist.api import TodoistAPI

from base_test_case import BaseTestCase
from views.views import SignInView


class TestTask(BaseTestCase):

    def test_create_task_via_mobile_phone(self):
        api = TodoistAPI('f2c945f22636b263da979b96d115e2a2e2a63a99')
        project_name = ''.join(random.sample(string.ascii_lowercase, 7))
        project = api.projects.add(project_name)
        api.commit()
        project_id = project['id']
        api.sync()

        sign_in_view = SignInView(self.driver)
        home_view = sign_in_view.sign_in_with_email('dhkhk@gmail.com', '12345678')
        home_view.change_view_button.click()
        home_view.get_item_by_name('Projects').click()
        home_view.get_item_by_name(project_name).click()
        task_view = home_view.plus_button.click()
        task_name = project_name + ' task'
        task_view.task_name_input.set_value(task_name)
        task_view.submit_button.click()

        api.sync()
        for _ in range(3):
            tasks_list = api.items.all(lambda i: i['project_id'] == project_id)
            try:
                if tasks_list[0]['content'] == task_name:
                    break
            except IndexError:
                pass
            time.sleep(10)
        else:
            raise AssertionError("Task '%s' was not added to the project '%s'" % (task_name, project_name))
