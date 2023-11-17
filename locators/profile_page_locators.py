from selenium.webdriver.common.by import By


class ProfilePageLocators:
    FAVORITES_BUTTON = (By.CSS_SELECTOR, '.menu-list > a:nth-child(1)')
    SETTINGS_BUTTON = (By.CSS_SELECTOR, '.menu-list > a:nth-child(2)')
    ADMINISTRATION_BUTTON = (By.CSS_SELECTOR, '.menu-list > a:nth-child(3)')
    STATISTICS_BUTTON = (By.CSS_SELECTOR, '.menu-list > a:nth-child(4)')
    TITLE = (By.CLASS_NAME, 'title')
    STATISTICS_TITLE = (By.CLASS_NAME, 'stats-title')

    """Administration page"""
    USERS_SEARCH_INPUT = (By.CSS_SELECTOR, 'div.search > input')
    USERS_SEARCH_BUTTON = (By.CSS_SELECTOR, 'div.search > span:nth-child(2)')
    FOUND_USER_NAME = (By.CLASS_NAME, 'list-item__name')
    CHANGE_ROLE_BUTTON = (By.CLASS_NAME, 'list-item__change')
    BUILD_ROLE = (By.CSS_SELECTOR, '.user-roles > div:nth-child(2)')
    SAVE_ROLE_BUTTON = (By.CLASS_NAME, 'user-save')
