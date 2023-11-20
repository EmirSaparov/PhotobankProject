import time

from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from data.data import BuildData


class ProfilePage(BasePage):

    def go_to_favorites(self):
        self.browser.find_element(*ProfilePageLocators.FAVORITES_BUTTON).click()
        page_title = self.browser.find_element(*ProfilePageLocators.TITLE)
        assert page_title.is_displayed(), 'This is not Favorites page'

    def go_to_settings(self):
        self.browser.find_element(*ProfilePageLocators.SETTINGS_BUTTON).click()
        page_title = self.browser.find_element(*ProfilePageLocators.TITLE)
        assert page_title.is_displayed(), 'This is not Settings page'

    def change_username_in_settings(self):
        self.browser.find_element(*ProfilePageLocators.FIRST_NAME).click()
        self.browser.find_element(*ProfilePageLocators.FIRST_NAME).clear()
        self.browser.find_element(*ProfilePageLocators.FIRST_NAME).send_keys('Максим')
        self.browser.find_element(*ProfilePageLocators.LAST_NAME).click()
        self.browser.find_element(*ProfilePageLocators.LAST_NAME).clear()
        self.browser.find_element(*ProfilePageLocators.LAST_NAME).send_keys('Сергеев')
        self.browser.find_element(*ProfilePageLocators.MIDDLE_NAME).click()
        self.browser.find_element(*ProfilePageLocators.MIDDLE_NAME).clear()
        self.browser.find_element(*ProfilePageLocators.MIDDLE_NAME).send_keys('Алексеевич')
        self.browser.find_element(*ProfilePageLocators.SETTINGS_SUBMIT_BUTTON).click()
        time.sleep(2)
        profile_name = self.browser.find_element(*ProfilePageLocators.MENU_PROFILE_NAME).text
        assert profile_name == 'Сергеевв Максимм Алексеевичч', 'Profile username is not changed'

    def change_username_filling_required_fields_in_settings(self):
        self.browser.find_element(*ProfilePageLocators.FIRST_NAME).click()
        self.browser.find_element(*ProfilePageLocators.FIRST_NAME).clear()
        self.browser.find_element(*ProfilePageLocators.FIRST_NAME).send_keys('Максим')
        self.browser.find_element(*ProfilePageLocators.LAST_NAME).click()
        self.browser.find_element(*ProfilePageLocators.LAST_NAME).clear()
        self.browser.find_element(*ProfilePageLocators.LAST_NAME).send_keys('Сергеев')
        self.browser.find_element(*ProfilePageLocators.MIDDLE_NAME).click()
        for _ in range(10):
            self.browser.find_element(*ProfilePageLocators.MIDDLE_NAME).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*ProfilePageLocators.SETTINGS_SUBMIT_BUTTON).click()
        time.sleep(2)
        profile_name = self.browser.find_element(*ProfilePageLocators.MENU_PROFILE_NAME).text
        assert profile_name == 'Сергеев Максим', 'Profile username is not changed'

    def change_username_not_filling_required_fields_in_settings(self):
        self.browser.find_element(*ProfilePageLocators.FIRST_NAME).click()
        for _ in range(6):
            self.browser.find_element(*ProfilePageLocators.FIRST_NAME).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*ProfilePageLocators.SETTINGS_SUBMIT_BUTTON).click()
        unfilled_input = (WebDriverWait(self.browser, 10).until
                          (EC.presence_of_element_located(ProfilePageLocators.FIRST_NAME_INPUT_UNFILLED)))
        assert unfilled_input.is_displayed(), 'Profile username remains empty'

    def go_to_administration(self):
        self.browser.find_element(*ProfilePageLocators.ADMINISTRATION_BUTTON).click()
        page_title = self.browser.find_element(*ProfilePageLocators.TITLE)
        assert page_title.is_displayed(), 'This is not Administration page'

    def go_to_statistics(self):
        self.browser.find_element(*ProfilePageLocators.STATISTICS_BUTTON).click()
        page_title = self.browser.find_element(*ProfilePageLocators.STATISTICS_TITLE)
        assert page_title.is_displayed(), 'This is not Statistics page'

    def search_for_users_in_administration_page(self):
        self.browser.find_element(*ProfilePageLocators.ADMINISTRATION_BUTTON).click()
        search_input = self.browser.find_element(*ProfilePageLocators.USERS_SEARCH_INPUT)
        search_input.send_keys(BuildData.email)
        self.browser.find_element(*ProfilePageLocators.USERS_SEARCH_BUTTON).click()
        WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element
                                              (ProfilePageLocators.FOUND_USER_NAME, BuildData.build_full_name))
        found_user_name = self.browser.find_element(*ProfilePageLocators.FOUND_USER_NAME).text
        print(found_user_name)
        assert found_user_name == BuildData.build_full_name, 'Search result fail'

    def appoint_users_role_build(self):
        self.browser.find_element(*ProfilePageLocators.ADMINISTRATION_BUTTON).click()
        search_input = self.browser.find_element(*ProfilePageLocators.USERS_SEARCH_INPUT)
        search_input.send_keys(BuildData.email)
        self.browser.find_element(*ProfilePageLocators.USERS_SEARCH_BUTTON).click()
        WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element
                                              (ProfilePageLocators.FOUND_USER_NAME, BuildData.build_full_name))
        self.browser.find_element(*ProfilePageLocators.CHANGE_ROLE_BUTTON).click()
        self.browser.find_element(*ProfilePageLocators.BUILD_ROLE).click()
        self.browser.find_element(*ProfilePageLocators.SAVE_ROLE_BUTTON).click()
        self.browser.refresh()
        search_input = self.browser.find_element(*ProfilePageLocators.USERS_SEARCH_INPUT)
        search_input.send_keys(BuildData.email)
        self.browser.find_element(*ProfilePageLocators.USERS_SEARCH_BUTTON).click()
        WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element
                                              (ProfilePageLocators.FOUND_USER_NAME, BuildData.build_full_name))
        self.browser.find_element(*ProfilePageLocators.CHANGE_ROLE_BUTTON).click()
        build_role = self.browser.find_element(*ProfilePageLocators.BUILD_ROLE)
        build_role_class_attribute = build_role.get_attribute('class')
        assert build_role_class_attribute == 'user-roles__item active', 'Build role for user is not activated'

    def remove_build_role_from_user(self):
        self.browser.find_element(*ProfilePageLocators.ADMINISTRATION_BUTTON).click()
        search_input = self.browser.find_element(*ProfilePageLocators.USERS_SEARCH_INPUT)
        search_input.send_keys(BuildData.email)
        self.browser.find_element(*ProfilePageLocators.USERS_SEARCH_BUTTON).click()
        WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element
                                              (ProfilePageLocators.FOUND_USER_NAME, BuildData.build_full_name))
        self.browser.find_element(*ProfilePageLocators.CHANGE_ROLE_BUTTON).click()
        self.browser.find_element(*ProfilePageLocators.BUILD_ROLE).click()
        self.browser.find_element(*ProfilePageLocators.SAVE_ROLE_BUTTON).click()
        self.browser.refresh()
        search_input = self.browser.find_element(*ProfilePageLocators.USERS_SEARCH_INPUT)
        search_input.send_keys(BuildData.email)
        self.browser.find_element(*ProfilePageLocators.USERS_SEARCH_BUTTON).click()
        WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element
                                              (ProfilePageLocators.FOUND_USER_NAME, BuildData.build_full_name))
        self.browser.find_element(*ProfilePageLocators.CHANGE_ROLE_BUTTON).click()
        build_role = self.browser.find_element(*ProfilePageLocators.BUILD_ROLE)
        build_role_class_attribute = build_role.get_attribute('class')
        assert build_role_class_attribute == 'user-roles__item', 'Build role for user is not deactivated'
