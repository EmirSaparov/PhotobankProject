import base64
import re
import time

from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators
from locators.projects_page_locators import ProjectPageLocators
from data.data import LoginData, BuildData, IMAPServiceData, RegistrationData, PasswordRecoverData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import imaplib
import email


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    """Method for getting data from mailbox"""

    @staticmethod
    def get_text_from_imap():
        server = imaplib.IMAP4_SSL(IMAPServiceData.imap_server, IMAPServiceData.imap_port)
        server.login(user=IMAPServiceData.username, password=IMAPServiceData.password)
        server.select('INBOX')
        status, email_ids = server.search(None, 'ALL')
        latest_email_id = email_ids[0].split()[-1]
        status, email_data = server.fetch(latest_email_id, '(RFC822)')
        raw_email = email_data[0][1]
        parsed_email = email.message_from_bytes(raw_email)
        content = parsed_email.get_payload()
        for part in content:
            text = base64.b64decode(part.get_payload()).decode()
            pattern = r"Ваш новый пароль: (\w+)"
            match = re.search(pattern, text)
            if match:
                password = match.group(1)
                return password

    def registration(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        self.browser.find_element(*BasePageLocators.REGISTRATION_LINK).click()
        registration_email = self.browser.find_element(*BasePageLocators.EMAIL_INPUT)
        registration_email.send_keys(RegistrationData.email)
        registration_password = self.browser.find_element(*BasePageLocators.PASSWORD_INPUT)
        registration_password.send_keys(RegistrationData.password)
        confirmation_password = self.browser.find_element(*BasePageLocators.CONFIRMATION_PASSWORD_INPUT)
        confirmation_password.send_keys(RegistrationData.password)
        self.browser.find_element(*BasePageLocators.SUBMIT_BUTTON).click()
        assert self.browser.find_element(*BasePageLocators.PROFILE_BUTTON), 'Registration is not complete'

    def registration_if_already_have_account(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        self.browser.find_element(*BasePageLocators.REGISTRATION_LINK).click()
        registration_email = self.browser.find_element(*BasePageLocators.EMAIL_INPUT)
        registration_email.send_keys(LoginData.email)
        registration_password = self.browser.find_element(*BasePageLocators.PASSWORD_INPUT)
        registration_password.send_keys(LoginData.password)
        confirmation_password = self.browser.find_element(*BasePageLocators.CONFIRMATION_PASSWORD_INPUT)
        confirmation_password.send_keys(LoginData.password)
        self.browser.find_element(*BasePageLocators.SUBMIT_BUTTON).click()
        alert_message = (WebDriverWait(self.browser, 10).
                         until(EC.visibility_of_element_located(BasePageLocators.INVALID_LOGIN_ALERT)))
        alert_message_text = (WebDriverWait(self.browser, 10).
                              until(EC.visibility_of_element_located(BasePageLocators.INVALID_LOGIN_ALERT))).text
        assert alert_message.is_displayed(), 'Fail registration went wrong'
        assert alert_message_text == 'Почта уже используется', 'Registrartion alert is incorrect'

    def password_recover(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        self.browser.find_element(*BasePageLocators.PASSWORD_RECOVER_LINK).click()
        self.browser.find_element(*BasePageLocators.EMAIL_INPUT).click()
        self.browser.find_element(*BasePageLocators.EMAIL_INPUT).clear()
        self.browser.find_element(*BasePageLocators.EMAIL_INPUT).send_keys(PasswordRecoverData.email)
        self.browser.find_element(*BasePageLocators.SUBMIT_BUTTON).click()
        alert_message_text = (WebDriverWait(self.browser, 10).
                              until(EC.visibility_of_element_located(BasePageLocators.EMAIL_SENT_ALERT))).text
        assert alert_message_text == 'Новый пароль отправлен на указанную почту', 'Registrartion alert is incorrect'
        time.sleep(5)
        new_password = self.get_text_from_imap()
        print(new_password)
        self.browser.find_element(*BasePageLocators.REGISTRATION_LINK).click()
        time.sleep(2)
        self.browser.find_element(*BasePageLocators.EMAIL_INPUT).click()
        self.browser.find_element(*BasePageLocators.EMAIL_INPUT).clear()
        self.browser.find_element(*BasePageLocators.EMAIL_INPUT).send_keys(PasswordRecoverData.email)
        self.browser.find_element(*BasePageLocators.PASSWORD_INPUT).click()
        self.browser.find_element(*BasePageLocators.PASSWORD_INPUT).clear()
        self.browser.find_element(*BasePageLocators.PASSWORD_INPUT).send_keys(new_password)
        self.browser.find_element(*BasePageLocators.SUBMIT_BUTTON).click()
        assert self.browser.find_element(*BasePageLocators.PROFILE_BUTTON), 'Password recover is not complete'

    def visibility_button_switch(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        email_input = self.browser.find_element(*BasePageLocators.EMAIL_INPUT)
        email_input.send_keys(LoginData.email)
        password_input = self.browser.find_element(*BasePageLocators.PASSWORD_INPUT)
        password_input.send_keys(LoginData.password)
        visibility_button = self.browser.find_element(*BasePageLocators.PASSWORD_VISIBILITY_BUTTON)
        visibility_button.click()
        visibility_on_text = visibility_button.get_attribute('title')
        print(visibility_on_text)
        assert visibility_on_text == 'Скрыть пароль', 'Password is not visible'
        visibility_button.click()
        visibility_off_text = visibility_button.get_attribute('title')
        assert visibility_off_text == 'Показать пароль', 'Password is visible'

    def login(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        email_input = self.browser.find_element(*BasePageLocators.EMAIL_INPUT)
        email_input.send_keys(LoginData.email)
        password_input = self.browser.find_element(*BasePageLocators.PASSWORD_INPUT)
        password_input.send_keys(LoginData.password)
        self.browser.find_element(*BasePageLocators.SUBMIT_BUTTON).click()
        assert self.browser.find_element(*BasePageLocators.PROFILE_BUTTON), 'Authentication data is not valid'

    def login_invalid_email(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        email_input = self.browser.find_element(*BasePageLocators.EMAIL_INPUT)
        email_input.send_keys('emir' + LoginData.email)
        password_input = self.browser.find_element(*BasePageLocators.PASSWORD_INPUT)
        password_input.send_keys(LoginData.password)
        self.browser.find_element(*BasePageLocators.SUBMIT_BUTTON).click()
        alert_message = (WebDriverWait(self.browser, 10).
                         until(EC.visibility_of_element_located(BasePageLocators.INVALID_LOGIN_ALERT)))
        alert_message_text = (WebDriverWait(self.browser, 10).
                              until(EC.visibility_of_element_located(BasePageLocators.INVALID_LOGIN_ALERT))).text
        assert alert_message.is_displayed(), 'Fail authentication went wrong'
        assert alert_message_text == 'Неверный логин или пароль', 'Authentication alert is incorrect'

    def login_invalid_password(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        email_input = self.browser.find_element(*BasePageLocators.EMAIL_INPUT)
        email_input.send_keys(LoginData.email)
        password_input = self.browser.find_element(*BasePageLocators.PASSWORD_INPUT)
        password_input.send_keys('11' + LoginData.password)
        self.browser.find_element(*BasePageLocators.SUBMIT_BUTTON).click()
        alert_message = (WebDriverWait(self.browser, 10).
                         until(EC.visibility_of_element_located(BasePageLocators.INVALID_LOGIN_ALERT)))
        alert_message_text = (WebDriverWait(self.browser, 10).
                              until(EC.visibility_of_element_located(BasePageLocators.INVALID_LOGIN_ALERT))).text
        assert alert_message.is_displayed(), 'Fail authentication went wrong'
        assert alert_message_text == 'Неверный логин или пароль', 'Authentication alert is incorrect'

    def login_empty_email(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        password_input = self.browser.find_element(*BasePageLocators.PASSWORD_INPUT)
        password_input.send_keys(LoginData.password)
        self.browser.find_element(*BasePageLocators.SUBMIT_BUTTON).click()
        alert_message = (WebDriverWait(self.browser, 10).
                         until(EC.visibility_of_element_located(BasePageLocators.INVALID_LOGIN_ALERT)))
        alert_message_text = (WebDriverWait(self.browser, 10).
                              until(EC.visibility_of_element_located(BasePageLocators.INVALID_LOGIN_ALERT))).text
        assert alert_message.is_displayed(), 'Fail authentication went wrong'
        assert alert_message_text == 'Некорректный E-mail', 'Authentication alert is incorrect'

    def login_empty_password(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        email_input = self.browser.find_element(*BasePageLocators.EMAIL_INPUT)
        email_input.send_keys('emir' + LoginData.email)
        self.browser.find_element(*BasePageLocators.SUBMIT_BUTTON).click()
        alert_message = (WebDriverWait(self.browser, 10).
                         until(EC.visibility_of_element_located(BasePageLocators.INVALID_LOGIN_ALERT)))
        alert_message_text = (WebDriverWait(self.browser, 10).
                              until(EC.visibility_of_element_located(BasePageLocators.INVALID_LOGIN_ALERT))).text
        assert alert_message.is_displayed(), 'Fail authentication went wrong'
        assert alert_message_text == 'Неизвестная ошибка', 'Authentication alert is incorrect'

    def login_as_build(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        email_input = self.browser.find_element(*BasePageLocators.EMAIL_INPUT)
        email_input.send_keys(BuildData.email)
        password_input = self.browser.find_element(*BasePageLocators.PASSWORD_INPUT)
        password_input.send_keys(BuildData.password)
        self.browser.find_element(*BasePageLocators.SUBMIT_BUTTON).click()
        assert self.browser.find_element(*BasePageLocators.PROFILE_BUTTON), 'Authentication data of build is not valid'

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

    def go_to_projects_page_from_footer(self):
        self.browser.find_element(*BasePageLocators.PROJECTS_LINK_FOOTER).click()
        assert WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProjectPageLocators.PROJECTS_PAGE_TITLE)
        ), 'Projects page is not loaded'

    def go_to_photo_of_the_day_from_footer(self):
        self.browser.find_element(*BasePageLocators.PHOTO_OF_THE_DAY_LINK_FOOTER).click()

        assert (WebDriverWait(self.browser, 10).until
                (EC.visibility_of_element_located(MainPageLocators.PHOTO_OF_THE_DAY))), 'There is no carousel on page'

    def go_to_favorites_burger_menu(self):
        self.browser.find_element(*BasePageLocators.PROFILE_BUTTON).click()
        self.browser.find_element(*BasePageLocators.FAVORITES_BUTTON).click()
        assert (WebDriverWait(self.browser, 10).until
                (EC.visibility_of_element_located(ProfilePageLocators.TITLE))), 'This is not Favorites page'

    def go_to_settings_burger_menu(self):
        self.browser.find_element(*BasePageLocators.PROFILE_BUTTON).click()
        self.browser.find_element(*BasePageLocators.SETTINGS_BUTTON).click()
        assert (WebDriverWait(self.browser, 10).until
                (EC.visibility_of_element_located(ProfilePageLocators.TITLE))), 'This is not Settings page'

    def go_to_administration_burger_menu(self):
        self.browser.find_element(*BasePageLocators.PROFILE_BUTTON).click()
        self.browser.find_element(*BasePageLocators.ADMINISTRATION_BUTTON).click()
        assert (WebDriverWait(self.browser, 10).until
                (EC.visibility_of_element_located(ProfilePageLocators.TITLE))), \
            'This is not Administration page'

    def go_to_statistics_burger_menu(self):
        self.browser.find_element(*BasePageLocators.PROFILE_BUTTON).click()
        self.browser.find_element(*BasePageLocators.STATISTICS_BUTTON).click()
        assert (WebDriverWait(self.browser, 10).until
                (EC.visibility_of_element_located(ProfilePageLocators.STATISTICS_TITLE))), 'This is not Statistics page'
