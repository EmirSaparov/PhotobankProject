from selenium.webdriver.common.by import By


class BasePageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, '.email > input[type=text]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '.password > input[type=password]')
    CONFIRMATION_PASSWORD_INPUT = (By.CSS_SELECTOR, 'div:nth-child(5) > input[type=password]')
    PASSWORD_VISIBILITY_BUTTON = (By.CSS_SELECTOR, '.password > span')
    INVALID_LOGIN_ALERT = (By.CLASS_NAME, 'modal-alert')
    EMAIL_SENT_ALERT = (By.CLASS_NAME, 'modal-alert')
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
    PROJECTS_LINK_FOOTER = (By.CSS_SELECTOR, '.footer-menu > a:nth-child(1)')
    PHOTO_OF_THE_DAY_LINK_FOOTER = (By.CSS_SELECTOR, '.footer-menu > a:nth-child(3)')
    FAVORITES_BUTTON = (By.CSS_SELECTOR, '.mobileProfile-list > a:nth-child(1)')
    SETTINGS_BUTTON = (By.CSS_SELECTOR, '.mobileProfile-list > a:nth-child(2)')
    ADMINISTRATION_BUTTON = (By.CSS_SELECTOR, '.mobileProfile-list > a:nth-child(4)')
    STATISTICS_BUTTON = (By.CSS_SELECTOR, '.mobileProfile-list > a:nth-child(3)')
    REGISTRATION_LINK = (By.CSS_SELECTOR, 'header  span.secondary')
    PASSWORD_RECOVER_LINK = (By.CSS_SELECTOR, '.modal-sublinks .primary')

