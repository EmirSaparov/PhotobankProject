import pytest

from pages.main_page import MainPage
from pages.project_page import ProjectPage


class TestSmoke:

    url = 'https://stage.rcfb.abolsoft.ru'

    def test_login(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.login()

    def test_search_by_text(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.search_by_text()
        page.go_to_main_page()

    # def test_create_project(self, browser):
    #     page = MainPage(browser=browser, url=self.url)
    #     page.open()
    #     page.login()
    #     page.create_parental_project()

    # def test_create_subproject(self, browser):
    #     page = MainPage(browser=browser, url=self.url)
    #     page.open()
    #     page.login()
    #     page.create_child_project()

    def test_create_album(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_projects_page()
        page.create_album()

    def test_upload_photo(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_projects_page()
        page.add_photo_in_album()

    def test_download_one_photo_hover(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_projects_page()
        page.download_photo_in_album_hover()

    def test_delete_one_photo(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_projects_page()
        page.delete_photo_in_album()

    def test_upload_several_photo(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_projects_page()
        page.add_several_photo_in_album()

    @pytest.mark.new
    def test_download_all_photo(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_projects_page()
        page.download_all_photo_in_album()

    def test_delete_several_photo(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_projects_page()
        page.delete_several_photo_in_album()

    def test_delete_album(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_projects_page()
        page.album_delete()
