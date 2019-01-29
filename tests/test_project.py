from todoist.api import TodoistAPI
from base_test_case import BaseTestCase
from views.views import SignInView


class TestProject(BaseTestCase):

    def test_create_project(self):
        api = TodoistAPI('f2c945f22636b263da979b96d115e2a2e2a63a99')
        project_name = 'Test8000'
        project = api.projects.add(project_name)
        api.commit()
        assert project.data['name'] == project_name

        sign_in_view = SignInView(self.driver)
        home_view = sign_in_view.sign_in_with_email('dhkhk@gmail.com', '12345678')
        home_view.change_view_button.click()
        home_view.get_item_by_name('Projects').click()
        home_view.find_full_text(project_name)
