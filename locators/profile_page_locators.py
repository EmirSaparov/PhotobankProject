from selenium.webdriver.common.by import By


class ProfilePageLocators:
    FAVORITES_BUTTON = (By.CSS_SELECTOR, '.menu-list > a:nth-child(1)')
    MY_PHOTOS_BUTTON = (By.CSS_SELECTOR, '.menu-list > a:nth-child(2)')
    SETTINGS_BUTTON = (By.CSS_SELECTOR, '.menu-list > a:nth-child(3)')
    ADMINISTRATION_BUTTON = (By.CSS_SELECTOR, '.menu-list > a:nth-child(4)')
    STATISTICS_BUTTON = (By.CSS_SELECTOR, '.menu-list > a:nth-child(5)')
    FAVORITES_TITLE = (By.CLASS_NAME, 'title')
    MY_PHOTOS_TITLE = (By.CLASS_NAME, 'title')
    SETTINGS_TITLE = (By.CLASS_NAME, 'title')
    ADMINISTRATION_TITLE = (By.CLASS_NAME, 'title')
    STATISTICS_TITLE = (By.CLASS_NAME, 'stats-title')

    """Administration page"""
    USERS_SEARCH_INPUT = (By.CSS_SELECTOR, 'div.search > input')
    USERS_SEARCH_BUTTON = (By.CSS_SELECTOR, 'div.search > span:nth-child(2)')
    FOUND_USER_NAME = (By.CLASS_NAME, 'list-item__name')
    CHANGE_ROLE_BUTTON = (By.CLASS_NAME, 'list-item__change')
    BUILD_ROLE = (By.CSS_SELECTOR, '.user-roles > div:nth-child(2)')
    SAVE_ROLE_BUTTON = (By.CLASS_NAME, 'user-save')
