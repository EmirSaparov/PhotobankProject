from selenium.webdriver.common.by import By
from data.data import CreateAlbumData, EditAlbumData


class ProjectPageLocators:
    PROJECTS_PAGE_TITLE = (By.CLASS_NAME, 'projects-title')
    PROJECT_TITLE_ON_ITS_PAGE = (By.CLASS_NAME, 'intro-information__title')
    PHOTO_GROUP_EDIT_BUTTON = (By.CSS_SELECTOR, ' div.event-head__mul-sel > div.btns > span')
    SPECIFIC_RUBRIC_FILTER = (By.XPATH, f'//div[@class="filter"] //div[text()="{CreateAlbumData.rubric_name}"]')

    """Album add modal window"""
    PHOTO_ITEM = (By.CLASS_NAME, 'events-list__image')
    ALBUM_ITEM = (By.CLASS_NAME, 'events-item')
    ALL_ALBUMS_CONTAINER = (By.CLASS_NAME, 'events')
    ADD_ALBUM_BUTTON_NO_ALBUMS = (By.CSS_SELECTOR, '.events-item.addNew')
    ADD_ALBUM_BUTTON_ALBUMS_EXIST = (By.CLASS_NAME, 'type-wrapper__addalbum')
    ALBUM_DATE_TIME_PICKER = (By.CSS_SELECTOR, 'div:nth-child(3) > div.dp__main.dp__theme_light > div > div > input')
    DATE_SELECT = (By.CLASS_NAME, 'dp__today')
    OUT_OF_DATE_SELECT = (By.CSS_SELECTOR,
                          'div.dp__calendar > div > div > div.dp__calendar > div:nth-child(1) > div:nth-child(1) > div')
    ALBUM_SELECT_BUTTON = (By.CLASS_NAME, 'dp__select')
    ALBUM_OUT_OF_DATE_CHECKBOX = (By.CSS_SELECTOR, 'div:nth-child(2) > div.event-row__checkbox')
    RUBRICS_MULTISELECT = (By.CLASS_NAME, 'multiselect-tags-search')
    RUBRIC_CHOOSE = (By.XPATH, f'//li[@aria-label="{CreateAlbumData.rubric_name}"]')
    ALBUM_NAME_RU = (By.ID, 'name-ru')
    ALBUM_NAME_EN = (By.ID, 'name-en')
    ALBUM_DESC_RU = (By.CSS_SELECTOR, 'div:nth-child(1) > div:nth-child(2) > textarea')
    ALBUM_DESC_EN = (By.CSS_SELECTOR, 'div:nth-child(2) > div:nth-child(2) > textarea')
    ALBUM_CREATE_BUTTON = (By.CSS_SELECTOR, '.event-row__btn.primary')
    SPECIFIC_ALBUM = (By.XPATH, f'//div[text()="{CreateAlbumData.album_name_ru}"]')
    SPECIFIC_ALBUM_EDITED = (By.XPATH, f'//div[contains(text(),"{EditAlbumData.name_ru_edit}")]')
    SPECIFIC_ALBUM_NO_FILTER = (By.XPATH, f'//div[contains(text(),"{CreateAlbumData.album_name_ru_no_filter}")]')
    SPECIFIC_ALBUM_OUT_OF_DATE = (By.XPATH, f'//div[contains(text(),"{CreateAlbumData.album_name_ru_out_of_date}")]')
    SPECIFIC_ALBUM_DELETE_BUTTON = (By.CSS_SELECTOR, ' div:nth-child(1) > div > div > div.events-item__delete')
    SPECIFIC_ALBUM_HOVER = (By.CSS_SELECTOR, 'div.events > div:nth-child(1) > div')
    DISPLAY_TYPE = (By.CLASS_NAME, 'type-selected')
    DISPLAY_TYPE_ALBUMS = (By.CSS_SELECTOR, '.type-select > div:nth-child(1)')
    DISPLAY_TYPE_PHOTOS = (By.CSS_SELECTOR, '.type-select > div:nth-child(2)')
    EDIT_ALBUM_BUTTON = (By.CLASS_NAME, 'event-head__title--edit')
    HIDE_SHOW_ALBUM_BUTTON = (By.CLASS_NAME, 'event-head__title--visibility')
    VISIBILITY_STATUS_ALBUM = (By.CLASS_NAME, 'event-head__title--status')

    """Add photo"""
    ADD_PHOTO_BUTTON = (By.XPATH, '//div[text()=" Добавить фото "]')
    UPLOAD_PHOTO_INPUT = (By.ID, 'hiddenUploader')
    UPLOAD_PHOTO_BUTTON = (By.CLASS_NAME, 'event-head__upload')
    CLOSE_UPLOAD_MODAL = (By.CSS_SELECTOR, '.event-head__title-actions--item.event-head__title-actions--item-selected')
    UPLOADED_PHOTOS_LIST = (By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]')

    """Download photo"""
    DOWNLOAD_PHOTO_HOVER_BUTTON = (By.CLASS_NAME, 'event-list__image--download')
    PHOTO_PREVIEW = (By.CLASS_NAME, 'event-list__image')
    HIDDEN_PHOTO_PREVIEW = (By.CLASS_NAME, 'event-list__image--hidden')
    DOWNLOAD_PHOTO_PREVIEW_BUTTON = (By.CLASS_NAME, 'primary')
    DOWNLOAD_ALL_PHOTO_BUTTON = (By.CSS_SELECTOR, 'div.event-head > div > div > a')
    FULLSIZE_BUTTON = (By.CSS_SELECTOR, '.event-list__image--actions')

    """Action photo"""
    DELETE_BUTTON = (By.CLASS_NAME, 'delete')
    PHOTO_EDIT_BUTTON = (By.CLASS_NAME, 'edit')
    DELETE_ASSERTION_BUTTON = (By.CLASS_NAME, 'delete-confirm__accept')
    FIRST_PHOTO_CHECKBOX = (By.CSS_SELECTOR, 'div.event-list > div:nth-child(1)')
    SECOND_PHOTO_CHECKBOX = (By.CSS_SELECTOR, 'div.event-list > div:nth-child(2)')
    THIRD_PHOTO_CHECKBOX = (By.CSS_SELECTOR, 'div.event-list > div:nth-child(3')
    HIDE_AND_SHOW_BUTTON = (By.CSS_SELECTOR, ' div.event-list > div:nth-child(1) > div > div:nth-child(2)')

    """Photo edit modal window"""
    PHOTO_GROUP_EDIT_SELECTOR = (By.CLASS_NAME, 'vs__search')
    PHOTO_GROUP_EDIT_SELECTOR_DELETE = (By.ID, 'vs1__option-3')
    PHOTO_GROUP_EDIT_SELECTOR_HIDE = (By.ID, 'vs1__option-1')
    PHOTO_GROUP_EDIT_SELECTOR_SHOW = (By.ID, 'vs1__option-2')
    APPLY_BUTTON = (By.CSS_SELECTOR, ' div.fixed__btns > span:nth-child(1)')
    CHOOSE_ALL_CHECKBOXES = (By.CSS_SELECTOR, ' div.fixed__btns > span:nth-child(2)')
    PHOTO_EDIT_DATE_TIME_PICKER = (By.CLASS_NAME, '.dp__pointer.dp__input')
    PHOTO_EDIT_PLACE_RU = (By.CSS_SELECTOR, ' span:nth-child(4) > input')
    PHOTO_EDIT_PLACE_EN = (By.CSS_SELECTOR, ' span:nth-child(5) > input')
    PHOTO_EDIT_ON_PHOTO_RU = (By.CSS_SELECTOR, ' span:nth-child(7) > input')
    PHOTO_EDIT_ON_PHOTO_EN = (By.CSS_SELECTOR, ' span:nth-child(8) > input')
    PHOTO_EDIT_AUTHOR_RU = (By.CSS_SELECTOR, ' span:nth-child(10) > input')
    PHOTO_EDIT_AUTHOR_EN = (By.CSS_SELECTOR, ' span:nth-child(11) > input')
    PHOTO_EDIT_SAVE_BUTTON = (By.CLASS_NAME, 'primary')
    PHOTO_POSITION_EDIT = (By.CSS_SELECTOR, 'div > div.event-head > div > div > span')
    POSITION_PHOTO_PREV = (By.CSS_SELECTOR, 'div.event-list > div:nth-child(1)')
    POSITION_PHOTO_NEXT = (By.CSS_SELECTOR, 'div.event-list > div:nth-child(3)')
    SAVE_POSITION_BUTTON = (By.CSS_SELECTOR, 'div.event-head > div > div > span')
