import pytest
from pages.main_page import MainPage
from pages.project_page import ProjectPage
from pages.profile_page import ProfilePage


class TestMainPage:

    url = 'https://stage.rcfb.abolsoft.ru'

    def test_login(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.login()

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
    def test_delete_proj_from_slider(self, browser):
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

    # @pytest.mark.create_project
    # def test_create_project(self, browser):
    #     page = MainPage(browser=browser, url=self.url)
    #     page.open()
    #     page.login()
    #     page.create_parental_project()
    #
    # @pytest.mark.create_project
    # def test_create_subproject(self, browser):
    #     page = MainPage(browser=browser, url=self.url)
    #     page.open()
    #     page.login()
    #     page.create_child_project()
    @pytest.mark.footer_links
    def test_go_to_projects_page_from_footer(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.go_to_projects_page_from_footer()

    @pytest.mark.footer_links
    def test_go_to_photo_of_the_day_from_footer(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.go_to_photo_of_the_day_from_footer()

    @pytest.mark.burger_menu
    def test_go_to_my_photos_page_from_burger_menu(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_my_photos_burger_menu()

    @pytest.mark.burger_menu
    def test_go_to_favorites_page_from_burger_menu(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_favorites_burger_menu()

    @pytest.mark.burger_menu
    def test_go_to_settings_page_from_burger_menu(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_settings_burger_menu()

    @pytest.mark.burger_menu
    def test_go_to_administration_page_from_burger_menu(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_administration_burger_menu()

    @pytest.mark.burger_menu
    def test_go_to_statistics_page_from_burger_menu(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_statistics_burger_menu()

    """Project page test"""
    def test_create_album(self, browser):
        page = ProjectPage(browser=browser, url=f'{self.url}/ru/projects')
        page.open()
        page.login()
        page.create_album()

    def test_create_album_out_of_date(self, browser):
        page = ProjectPage(browser=browser, url=f'{self.url}/ru/projects')
        page.open()
        page.login()
        page.create_album_out_of_date()

    def test_create_album_no_filter(self, browser):
        page = ProjectPage(browser=browser, url=f'{self.url}/ru/projects')
        page.open()
        page.login()
        page.create_album_no_filter()

    def test_upload_photo(self, browser):
        page = ProjectPage(browser=browser, url=f'{self.url}/ru/projects')
        page.open()
        page.login()
        page.add_photo_in_album()

    def test_filter_album_by_rubric(self, browser):
        page = ProjectPage(browser=browser, url=f'{self.url}/ru/projects')
        page.open()
        page.login()
        page.album_filter_by_rubric()

    def test_hide_photo_in_album(self, browser):
        page = ProjectPage(browser=browser, url=f'{self.url}/ru/projects')
        page.open()
        page.login()
        page.hide_photos_in_album()

    def test_show_photo_in_album(self, browser):
        page = ProjectPage(browser=browser, url=f'{self.url}/ru/projects')
        page.open()
        page.login()
        page.show_photos_in_album()

    def test_download_one_photo_hover(self, browser):
        page = ProjectPage(browser=browser, url=f'{self.url}/ru/projects')
        page.open()
        page.login()
        page.download_photo_in_album_hover()

    def test_delete_one_photo(self, browser):
        page = ProjectPage(browser=browser, url=f'{self.url}/ru/projects')
        page.open()
        page.login()
        page.delete_photo_in_album()

    def test_upload_several_photo(self, browser):
        page = ProjectPage(browser=browser, url=f'{self.url}/ru/projects')
        page.open()
        page.login()
        page.add_several_photo_in_album()

    def test_download_all_photo(self, browser):
        page = ProjectPage(browser=browser, url=f'{self.url}/ru/projects')
        page.open()
        page.login()
        page.download_all_photo_in_album()

    def test_hide_multiple_photo_in_album(self, browser):
        page = ProjectPage(browser=browser, url=f'{self.url}/ru/projects')
        page.open()
        page.login()
        page.hide_multiple_photos_in_albums()

    def test_show_multiple_photo_in_album(self, browser):
        page = ProjectPage(browser=browser, url=f'{self.url}/ru/projects')
        page.open()
        page.login()
        page.show_multiple_photos_in_albums()

    def test_delete_several_photo(self, browser):
        page = ProjectPage(browser=browser, url=f'{self.url}/ru/projects')
        page.open()
        page.login()
        page.delete_several_photo_in_album()

    def test_show_album(self, browser):
        page = ProjectPage(browser=browser, url=f'{self.url}/ru/projects')
        page.open()
        page.login()
        page.show_album()

    def test_hide_album(self, browser):
        page = ProjectPage(browser=browser, url=f'{self.url}/ru/projects')
        page.open()
        page.login()
        page.hide_album()

    def test_edit_album(self, browser):
        page = ProjectPage(browser=browser, url=f'{self.url}/ru/projects')
        page.open()
        page.login()
        page.edit_album()

    def test_delete_album(self, browser):
        page = ProjectPage(browser=browser, url=f'{self.url}/ru/projects')
        page.open()
        page.login()
        page.album_delete()

    @pytest.mark.new
    def test_edit_project(self, browser):
        page = MainPage(browser=browser, url=f'{self.url}/ru/projects')
        page.open()
        page.login()
        page.edit_project()

    # def test_photo_reposition(self, browser):
    #     page = ProjectPage(browser=browser, url=self.url)
    #     page.open()
    #     page.login()
    #     page.add_several_photo_in_album()
    #     page.go_to_main_page()
    #     page.reposition_photos()

    """Profile page test"""

    def test_go_to_my_photos_page(self, browser):
        page = ProfilePage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_favorites_burger_menu()
        page.go_to_my_photos()

    def test_go_to_favorites_page(self, browser):
        page = ProfilePage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_my_photos_burger_menu()
        page.go_to_favorites()

    def test_go_to_settings_page(self, browser):
        page = ProfilePage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_favorites_burger_menu()
        page.go_to_settings()

    def test_go_to_administration_page(self, browser):
        page = ProfilePage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_favorites_burger_menu()
        page.go_to_administration()

    def test_go_to_statistics_page(self, browser):
        page = ProfilePage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_favorites_burger_menu()
        page.go_to_statistics()

    def test_superadmin_can_search_users(self, browser):
        page = ProfilePage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_favorites_burger_menu()
        page.search_for_users_in_administration_page()

    def test_appoint_user_build(self, browser):
        page = ProfilePage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_favorites_burger_menu()
        page.appoint_users_role_build()

    def test_remove_build_role_from_user(self, browser):
        page = ProfilePage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_favorites_burger_menu()
        page.remove_build_role_from_user()

    """Build Role test"""
    @pytest.mark.build
    def test_superadmin_appoint_build(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_projects_page()
        page.appoint_build_on_project_by_superadmin()

    @pytest.mark.build
    def test_build_have_charges_on_project_as_build(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.login_as_build()
        page.go_to_projects_page()
        page.build_have_charges_on_project_as_build()

    @pytest.mark.build
    def test_build_can_edit_project(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.login_as_build()
        page.go_to_projects_page()
        page.build_can_edit_project()

    @pytest.mark.build
    def test_superadmin_remove_build(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.login()
        page.go_to_projects_page()
        page.remove_build_from_project_by_superadmin()

    @pytest.mark.build
    def test_build_dont_have_charges_on_project_as_build(self, browser):
        page = MainPage(browser=browser, url=self.url)
        page.open()
        page.login_as_build()
        page.go_to_projects_page()
        page.build_dont_have_charges_on_project_after_remove_as_build()
