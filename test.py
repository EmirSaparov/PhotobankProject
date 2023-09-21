import pytest
from pages.main_page import MainPage
from pages.project_page import ProjectPage


class TestMainPage:
    url = 'https://rcfb.stage.magnatmedia.com/'

    def test_login(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.login()

    def test_search_by_text(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.search_by_text()
        page.go_to_main_page()

    def test_logout(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.logout()

    @pytest.mark.potd
    def test_go_to_photo_of_the_day(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.go_to_photo_of_the_day()

    @pytest.mark.proj_page
    def test_go_to_projects(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.go_to_projects_page()

    @pytest.mark.lang_switch
    def test_switch_language(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.change_language()

    @pytest.mark.slider
    def test_go_to_project_from_slider(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.open_project_from_slider()

    @pytest.mark.slider
    def test_add_proj_in_slider(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.add_new_project_in_slider()

    @pytest.mark.slider
    def test_delete_prof_from_slider(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.delete_added_project_in_slider()

    @pytest.mark.slider
    def test_can_move_forth_and_back(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.slider_can_go_forward_back()

    @pytest.mark.proj_page
    def test_go_projects_page_from_description(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.go_to_projects_from_description()

    @pytest.mark.proj_page
    def test_go_projects_page_from_all_proj_button(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.more_projects_button()

    @pytest.mark.potd
    def test_check_potd_slider_can_move_forth_back(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.go_to_photo_of_the_day()
        page.potd_slider_can_go_forward_back()

    @pytest.mark.create_project
    def test_create_project(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.create_parental_project()

    @pytest.mark.create_project
    def test_create_subproject(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.create_child_project()


class TestProjectPage:
    url = 'https://rcfb.stage.magnatmedia.com/'

    @pytest.mark.create_album
    def test_create_album(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.create_album()

    # @pytest.mark.create_album
    def test_create_album_out_of_date(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.create_album_out_of_date()

    # @pytest.mark.create_album
    def test_create_album_no_filter(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.create_album_no_filter()

    @pytest.mark.upload_photo
    def test_upload_photo(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.add_photo_in_album()

    @pytest.mark.upload_photo
    def test_upload_several_photo(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.add_several_photo_in_album()

    @pytest.mark.download
    def test_download_one_photo_hover(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.download_photo_in_album_hover()

    @pytest.mark.delete_photo
    def test_delete_one_photo(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.delete_photo_in_album()

    @pytest.mark.download
    def test_download_all_photo(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.download_all_photo_in_album()

    @pytest.mark.delete_photo
    def test_delete_several_photo(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.delete_several_photo_in_album()

    @pytest.mark.delete_album
    def test_delete_album(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.album_delete()

    @pytest.mark.rubric_album
    def test_filter_album_by_rubric(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.album_filter_by_rubric()

    @pytest.mark.display_type
    def test_display_type_change(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.display_type_by_photos_and_albums()

    # @pytest.mark.hide
    def test_hide_photo_in_album(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.hide_photos_in_album()

    # @pytest.mark.show
    def test_show_photo_in_album(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.show_photos_in_album()

    # @pytest.mark.hide
    def test_hide_multiple_photo_in_album(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.hide_multiple_photos_in_albums()

    # @pytest.mark.show
    def test_show_multiple_photo_in_album(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.show_multiple_photos_in_albums()

    @pytest.mark.edit
    def test_edit_project(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.edit_project()

    @pytest.mark.edit
    def test_edit_album(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.edit_album()

    @pytest.mark.hide
    def test_hide_album(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.hide_album()

    @pytest.mark.show
    def test_show_album(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.show_album()

    @pytest.mark.reposition
    def test_photo_reposition(self, browser):
        page = ProjectPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.add_several_photo_in_album()
        page.go_to_main_page()
        page.reposition_photos()
