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
    USERS_SEARCH_CLEAR_BUTTON = (By.CSS_SELECTOR, 'div.search > span:nth-child(3)')
    DELETE_BUTTON = (By.CLASS_NAME, 'list-item__delete')
    FOUND_USER_NAME = (By.CLASS_NAME, 'list-item__name')
    SEARCH_RESULT = (By.CLASS_NAME, 'list-item')
    CHANGE_ROLE_BUTTON = (By.CLASS_NAME, 'list-item__change')
    BUILD_ROLE = (By.CSS_SELECTOR, '.user-roles > div:nth-child(2)')
    SAVE_ROLE_BUTTON = (By.CLASS_NAME, 'user-save')
    SUCCESS_DELETE_ALERT = (By.CLASS_NAME, 'footer-modal__text')

    """Settings page"""
    FIRST_NAME = (By.ID, 'firstName')
    LAST_NAME = (By.ID, 'lastName')
    MIDDLE_NAME = (By.CSS_SELECTOR, '.settings-fields > :nth-child(6)')
    SETTINGS_SUBMIT_BUTTON = (By.CLASS_NAME, 'settings-fields__save')
    MENU_PROFILE_NAME = (By.CLASS_NAME, 'menu-profile__name')
    FIRST_NAME_INPUT_UNFILLED = (By.CSS_SELECTOR, '.settings-fields__input.error')
