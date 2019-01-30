import time

import random
import string

from base_test_case import BaseTestCase
from views.views import SignInView


class TestTask(BaseTestCase):

    def find_project(self, filter_name, filter_value):
        for _ in range(6):
            self.api.sync()
            projects = self.api.projects.all(lambda i: i[filter_name] == filter_value)
            if projects:
                return projects
            time.sleep(10)
        else:
            raise AssertionError("API: Can't find a project by %s %s" % (filter_name, filter_value))

    def find_task(self, filter_name, filter_value):
        for _ in range(6):
            self.api.sync()
            tasks = self.api.items.all(lambda i: i[filter_name] == filter_value)
            if tasks:
                return tasks
            time.sleep(10)
        else:
            raise AssertionError("API: Can't find a task by %s %s" % (filter_name, filter_value))

    def test_create_task_via_mobile_phone(self):
        sign_in_view = SignInView(self.driver)
        home_view = sign_in_view.sign_in_with_email('dhkhk@gmail.com', '12345678')
        home_view.change_view_button.click()
        project_view = home_view.get_list_item_by_name('Projects').add_button.click()
        project_name = ''.join(random.sample(string.ascii_lowercase, 7))
        project_view.project_name_input.set_value(project_name)
        project_view.submit_project_button.click()
        task_view = home_view.plus_button.click()
        task_name = project_name + ' task'
        task_view.task_name_input.set_value(task_name)
        task_view.submit_task_button.click()

        project_id = self.find_project('name', project_name)[0]['id']
        current_task_name = self.find_task('project_id', project_id)[0]['content']
        assert current_task_name == task_name, "API: Task '%s' was not created in the project '%s'" \
                                               % (task_name, project_name)

    def test_reopen_task(self):
        sign_in_view = SignInView(self.driver)
        home_view = sign_in_view.sign_in_with_email('dhkhk@gmail.com', '12345678')
        home_view.change_view_button.click()
        project_view = home_view.get_list_item_by_name('Projects').add_button.click()
        project_name = ''.join(random.sample(string.ascii_lowercase, 7))
        project_view.project_name_input.set_value(project_name)
        project_view.submit_project_button.click()
        task_view = home_view.plus_button.click()
        task_name = project_name + ' task'
        task_view.task_name_input.set_value(task_name)
        task_view.submit_task_button.click()
        for _ in range(2):
            task_view.get_element_by_text(task_name).click()
        task_view.complete_button.click()
        project_view.find_full_text('No tasks for %s.' % project_name)

        task_id = self.find_task('content', task_name)[0]['id']
        self.api.items.get_by_id(task_id).uncomplete()
        self.api.commit()

        project_view.pull_to_refresh()
        project_view.find_full_text(task_name)
