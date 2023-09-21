from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CLASS_NAME, 'header-login')
    EMAIL_INPUT = (By.CSS_SELECTOR, '.email > input[type=text]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '.password > input[type=password]')
    SUBMIT_BUTTON = (By.CLASS_NAME, 'loginBtn')
    PROFILE_BUTTON = (By.CLASS_NAME, 'header-profile')
    LOGOUT_BUTTON = (By.CLASS_NAME, 'mobileProfile-logout')
    HEADER_LOGO = (By.CLASS_NAME, 'header-logo')
    PROJECTS_LINK = (By.CSS_SELECTOR, '.header-menu > a:nth-child(1)')
    PHOTO_OF_THE_DAY_LINK = (By.CSS_SELECTOR, '.header-menu > a:nth-child(2)')
    LANGUAGE_SWITCH_BUTTON = (By.CLASS_NAME, 'header-lang')
    SEARCH_BUTTON = (By.CLASS_NAME, 'header-search')
    SEARCH_INPUT = (By.CSS_SELECTOR, '.header-search > input[type=text]')
    RESULT_IMAGE = (By.CLASS_NAME, 'search-list__image')

