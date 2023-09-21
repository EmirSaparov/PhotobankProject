from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.projects_page_locators import ProjectPageLocators
from data.data import LoginData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def login(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        email_input = self.browser.find_element(*BasePageLocators.EMAIL_INPUT)
        email_input.send_keys(*LoginData.email)
        password_input = self.browser.find_element(*BasePageLocators.PASSWORD_INPUT)
        password_input.send_keys(*LoginData.password)
        self.browser.find_element(*BasePageLocators.SUBMIT_BUTTON).click()
        assert self.browser.find_element(*BasePageLocators.PROFILE_BUTTON), 'Authentication data is not valid'

    def logout(self):
        self.browser.find_element(*BasePageLocators.PROFILE_BUTTON).click()
        self.browser.find_element(*BasePageLocators.LOGOUT_BUTTON).click()
        assert self.browser.find_element(*BasePageLocators.LOGIN_LINK), 'Logout is not done'

    def go_to_main_page(self):
        self.browser.find_element(*BasePageLocators.HEADER_LOGO).click()
        assert WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(MainPageLocators.DESCRIPTION_TITLE)
        ), 'Main page is not loaded'

    def go_to_projects_page(self):
        self.browser.find_element(*BasePageLocators.PROJECTS_LINK).click()
        assert WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProjectPageLocators.PROJECTS_PAGE_TITLE)
        ), 'Projects page is not loaded'

    def go_to_photo_of_the_day(self):
        self.browser.find_element(*BasePageLocators.PHOTO_OF_THE_DAY_LINK).click()

        assert (WebDriverWait(self.browser, 10).until
               (EC.visibility_of_element_located(MainPageLocators.PHOTO_OF_THE_DAY))), 'There is no carousel on page'

    def change_language(self):
        initial_button = self.browser.find_element(*BasePageLocators.LANGUAGE_SWITCH_BUTTON).text
        self.browser.find_element(*BasePageLocators.LANGUAGE_SWITCH_BUTTON).click()
        changed_button = self.browser.find_element(*BasePageLocators.LANGUAGE_SWITCH_BUTTON).text
        assert initial_button != changed_button, 'Language switch button does not work'

    def search_by_text(self):
        self.browser.find_element(*BasePageLocators.SEARCH_BUTTON).click()
        search_input = self.browser.find_element(*BasePageLocators.SEARCH_INPUT)
        search_input.send_keys('пмэф')
        search_input.send_keys(Keys.ENTER)
        assert self.browser.find_element(*BasePageLocators.RESULT_IMAGE), 'No results by text search'
