import random
import string

from base_test_case import BaseTestCase
from views.views import SignInView


class TestProject(BaseTestCase):

    def test_create_project(self):
        project_name = ''.join(random.sample(string.ascii_lowercase, 7))
        project = self.api.projects.add(project_name)
        self.api.commit()
        assert project.data['name'] == project_name

        sign_in_view = SignInView(self.driver)
        home_view = sign_in_view.sign_in_with_email('dhkhk@gmail.com', '12345678')
        home_view.change_view_button.click()
        home_view.get_list_item_by_name('Projects').click()
        home_view.find_full_text(project_name)
