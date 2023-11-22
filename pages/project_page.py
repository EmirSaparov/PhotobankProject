import os
from selenium.webdriver import ActionChains
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.data import CreateAlbumData, EditAlbumData
from locators.main_page_locators import MainPageLocators
from locators.projects_page_locators import ProjectPageLocators
from pages.base_page import BasePage
import time
import urllib.request


class ProjectPage(BasePage):
    def create_album(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        try:
            self.browser.find_element(*ProjectPageLocators.ADD_ALBUM_BUTTON_ALBUMS_EXIST).click()
        except NoSuchElementException:
            self.browser.find_element(*ProjectPageLocators.ADD_ALBUM_BUTTON_NO_ALBUMS).click()
        time.sleep(2)
        self.browser.find_element(*ProjectPageLocators.ALBUM_OUT_OF_DATE_CHECKBOX).click()
        self.browser.find_element(*ProjectPageLocators.ALBUM_DATE_TIME_PICKER).click()
        time.sleep(2)
        self.browser.find_element(*ProjectPageLocators.DATE_SELECT).click()
        self.browser.find_element(*ProjectPageLocators.ALBUM_SELECT_BUTTON).click()
        self.browser.find_element(*ProjectPageLocators.RUBRICS_MULTISELECT).click()
        self.browser.find_element(*ProjectPageLocators.RUBRIC_CHOOSE).click()
        album_name_ru = self.browser.find_element(*ProjectPageLocators.ALBUM_NAME_RU)
        album_name_en = self.browser.find_element(*ProjectPageLocators.ALBUM_NAME_EN)
        album_desc_ru = self.browser.find_element(*ProjectPageLocators.ALBUM_DESC_RU)
        album_desc_en = self.browser.find_element(*ProjectPageLocators.ALBUM_DESC_EN)
        album_name_ru.send_keys(CreateAlbumData.album_name_ru)
        album_name_en.send_keys(CreateAlbumData.album_name_en)
        album_desc_ru.send_keys(CreateAlbumData.album_desc_ru)
        album_desc_en.send_keys(CreateAlbumData.album_desc_en)
        self.browser.find_element(*ProjectPageLocators.ALBUM_CREATE_BUTTON).click()
        created_album = self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM)
        assert created_album.is_displayed(), 'Album is not created'

    def create_album_out_of_date(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        try:
            self.browser.find_element(*ProjectPageLocators.ADD_ALBUM_BUTTON_ALBUMS_EXIST).click()
        except NoSuchElementException:
            self.browser.find_element(*ProjectPageLocators.ADD_ALBUM_BUTTON_NO_ALBUMS).click()
        time.sleep(2)
        self.browser.find_element(*ProjectPageLocators.ALBUM_OUT_OF_DATE_CHECKBOX).click()
        self.browser.find_element(*ProjectPageLocators.ALBUM_DATE_TIME_PICKER).click()
        time.sleep(2)
        self.browser.find_element(*ProjectPageLocators.OUT_OF_DATE_SELECT).click()
        self.browser.find_element(*ProjectPageLocators.ALBUM_SELECT_BUTTON).click()
        self.browser.find_element(*ProjectPageLocators.RUBRICS_MULTISELECT).click()
        self.browser.find_element(*ProjectPageLocators.RUBRIC_CHOOSE).click()
        album_name_ru = self.browser.find_element(*ProjectPageLocators.ALBUM_NAME_RU)
        album_name_en = self.browser.find_element(*ProjectPageLocators.ALBUM_NAME_EN)
        album_desc_ru = self.browser.find_element(*ProjectPageLocators.ALBUM_DESC_RU)
        album_desc_en = self.browser.find_element(*ProjectPageLocators.ALBUM_DESC_EN)
        album_name_ru.send_keys(CreateAlbumData.album_name_ru_out_of_date)
        album_name_en.send_keys(CreateAlbumData.album_name_en_out_of_date)
        album_desc_ru.send_keys(CreateAlbumData.album_desc_ru_out_of_date)
        album_desc_en.send_keys(CreateAlbumData.album_desc_en_out_of_date)
        self.browser.find_element(*ProjectPageLocators.ALBUM_CREATE_BUTTON).click()
        created_album = self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM_OUT_OF_DATE)
        assert created_album.is_displayed(), 'Album is not created'

    def create_album_no_filter(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        try:
            self.browser.find_element(*ProjectPageLocators.ADD_ALBUM_BUTTON_ALBUMS_EXIST).click()
        except NoSuchElementException:
            self.browser.find_element(*ProjectPageLocators.ADD_ALBUM_BUTTON_NO_ALBUMS).click()
        time.sleep(2)
        self.browser.find_element(*ProjectPageLocators.ALBUM_OUT_OF_DATE_CHECKBOX).click()
        self.browser.find_element(*ProjectPageLocators.ALBUM_DATE_TIME_PICKER).click()
        time.sleep(2)
        self.browser.find_element(*ProjectPageLocators.DATE_SELECT).click()
        self.browser.find_element(*ProjectPageLocators.ALBUM_SELECT_BUTTON).click()
        album_name_ru = self.browser.find_element(*ProjectPageLocators.ALBUM_NAME_RU)
        album_name_en = self.browser.find_element(*ProjectPageLocators.ALBUM_NAME_EN)
        album_desc_ru = self.browser.find_element(*ProjectPageLocators.ALBUM_DESC_RU)
        album_desc_en = self.browser.find_element(*ProjectPageLocators.ALBUM_DESC_EN)
        album_name_ru.send_keys(CreateAlbumData.album_name_ru_no_filter)
        album_name_en.send_keys(CreateAlbumData.album_name_en_no_filter)
        album_desc_ru.send_keys(CreateAlbumData.album_desc_ru_no_filter)
        album_desc_en.send_keys(CreateAlbumData.album_desc_en_no_filter)
        self.browser.find_element(*ProjectPageLocators.ALBUM_CREATE_BUTTON).click()
        created_album = self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM_NO_FILTER)
        assert created_album.is_displayed(), 'Album is not created'

    def add_photo_in_album(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM).click()
        self.browser.find_element(*ProjectPageLocators.ADD_PHOTO_BUTTON).click()
        upload_input = self.browser.find_element(*ProjectPageLocators.UPLOAD_PHOTO_INPUT)
        upload_input.send_keys(os.getcwd() + '/images/album_photo0.jpg')
        self.browser.find_element(*ProjectPageLocators.UPLOAD_PHOTO_BUTTON).click()
        time.sleep(2)
        self.browser.find_element(*ProjectPageLocators.CLOSE_UPLOAD_MODAL).click()
        uploaded_photo_list = self.browser.find_elements(*ProjectPageLocators.UPLOADED_PHOTOS_LIST)
        assert len(uploaded_photo_list) == 1, 'Photo is not added in album'

    def download_photo_in_album_hover(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM).click()
        actions = ActionChains(self.browser)
        image = self.browser.find_element(*ProjectPageLocators.DOWNLOAD_IMAGE)
        actions.move_to_element(image).perform()
        image_url = image.get_attribute('src')
        save_path = os.path.join(os.getcwd(), 'downloads', 'download_photo.jpg')
        urllib.request.urlretrieve(url=image_url, filename=save_path)
        self.browser.find_element(*ProjectPageLocators.DOWNLOAD_PHOTO_HOVER_BUTTON).click()
        time.sleep(1)
        assert os.path.exists(save_path), 'Photo is not downloaded'

    def delete_photo_in_album(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM).click()
        actions = ActionChains(self.browser)
        image = self.browser.find_element(*ProjectPageLocators.PHOTO_PREVIEW)
        actions.move_to_element(image).perform()
        self.browser.find_element(*ProjectPageLocators.DELETE_BUTTON).click()
        self.browser.find_element(*ProjectPageLocators.DELETE_ASSERTION_BUTTON).click()
        self.browser.refresh()
        try:
            image = self.browser.find_element(*ProjectPageLocators.PHOTO_PREVIEW)
            assert not image.is_displayed(), 'Photo is not deleted'
        except NoSuchElementException:
            assert True, 'Photo is not deleted'

    def add_several_photo_in_album(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM).click()
        self.browser.find_element(*ProjectPageLocators.ADD_PHOTO_BUTTON).click()
        upload_input = self.browser.find_element(*ProjectPageLocators.UPLOAD_PHOTO_INPUT)
        upload_input.send_keys(os.getcwd() + '/images/album_photo1.jpg\n'
                               + os.getcwd() + '/images/album_photo2.jpg\n'
                               + os.getcwd() + '/images/album_photo3.jpg')
        self.browser.find_element(*ProjectPageLocators.UPLOAD_PHOTO_BUTTON).click()
        WebDriverWait(self.browser, 20).until(EC.text_to_be_present_in_element(
            ProjectPageLocators.UPLOAD_STATE, '100%'))
        self.browser.find_element(*ProjectPageLocators.CLOSE_UPLOAD_MODAL).click()
        uploaded_photo_list = self.browser.find_elements(*ProjectPageLocators.UPLOADED_PHOTOS_LIST)
        print(len(uploaded_photo_list))
        assert len(uploaded_photo_list) == 1, 'Photos are not added in album'

    def download_all_photo_in_album(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM).click()
        images_zip = self.browser.find_element(*ProjectPageLocators.DOWNLOAD_ALL_PHOTO_BUTTON)
        images_url = images_zip.get_attribute('href')
        save_path = os.path.join(os.getcwd(), 'downloads', 'download_zip.zip')
        urllib.request.urlretrieve(images_url, save_path)
        time.sleep(1)
        assert os.path.exists(save_path), 'Album is not downloaded'

    def delete_several_photo_in_album(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM).click()
        self.browser.find_element(*ProjectPageLocators.PHOTO_GROUP_EDIT_BUTTON).click()
        self.browser.find_element(*ProjectPageLocators.FIRST_PHOTO_CHECKBOX).click()
        self.browser.find_element(*ProjectPageLocators.SECOND_PHOTO_CHECKBOX).click()
        self.browser.find_element(*ProjectPageLocators.THIRD_PHOTO_CHECKBOX).click()
        self.browser.find_element(*ProjectPageLocators.PHOTO_GROUP_EDIT_SELECTOR).click()
        time.sleep(2)
        delete_choose = WebDriverWait(self.browser, 3).until(
            EC.element_to_be_clickable(ProjectPageLocators.PHOTO_GROUP_EDIT_SELECTOR_DELETE)
        )
        delete_choose.click()
        self.browser.find_element(*ProjectPageLocators.APPLY_BUTTON).click()
        self.browser.refresh()
        try:
            image_list = self.browser.find_element(*ProjectPageLocators.PHOTO_PREVIEW)
            assert not image_list.is_displayed(), 'Photos are not deleted'
        except NoSuchElementException:
            assert True, 'Photos are not deleted'

    def album_delete(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        actions = ActionChains(self.browser)
        hover_album = (self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM_HOVER))
        actions.move_to_element(hover_album).perform()
        time.sleep(1)
        self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM_DELETE_BUTTON).click()
        self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM_DELETE_CONFIRMATION).click()
        self.browser.refresh()
        try:
            album = self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM)
            assert not album.is_displayed(), 'Album is not deleted'
        except NoSuchElementException:
            assert True, 'Album is not deleted'

    def album_filter_by_rubric(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        self.browser.find_element(*ProjectPageLocators.SPECIFIC_RUBRIC_FILTER).click()
        try:
            album = self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM_NO_FILTER)
            assert not album.is_displayed(), 'Albums are not filtered'
        except NoSuchElementException:
            assert True, 'Album are not filtered'

    def hide_photos_in_album(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM).click()
        actions = ActionChains(self.browser)
        image = self.browser.find_element(*ProjectPageLocators.PHOTO_PREVIEW)
        actions.move_to_element(image).perform()
        self.browser.find_element(*ProjectPageLocators.HIDE_AND_SHOW_BUTTON).click()
        hidden_image = self.browser.find_element(*ProjectPageLocators.HIDDEN_PHOTO_PREVIEW)
        assert hidden_image.is_displayed(), 'Photo is not hidden'

    def show_photos_in_album(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM).click()
        actions = ActionChains(self.browser)
        image = self.browser.find_element(*ProjectPageLocators.HIDDEN_PHOTO_PREVIEW)
        actions.move_to_element(image).perform()
        self.browser.find_element(*ProjectPageLocators.HIDE_AND_SHOW_BUTTON).click()
        hidden_image = self.browser.find_element(*ProjectPageLocators.PHOTO_PREVIEW)
        assert hidden_image.is_displayed(), 'Photo is not revealed'

    def hide_multiple_photos_in_albums(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM).click()
        self.browser.find_element(*ProjectPageLocators.PHOTO_GROUP_EDIT_BUTTON).click()
        self.browser.find_element(*ProjectPageLocators.FIRST_PHOTO_CHECKBOX).click()
        self.browser.find_element(*ProjectPageLocators.CHOOSE_ALL_CHECKBOXES).click()
        time.sleep(2)
        self.browser.find_element(*ProjectPageLocators.PHOTO_GROUP_EDIT_SELECTOR).click()
        hide_choose = WebDriverWait(self.browser, 3).until(
            EC.element_to_be_clickable(ProjectPageLocators.PHOTO_GROUP_EDIT_SELECTOR_HIDE)
        )
        hide_choose.click()
        self.browser.find_element(*ProjectPageLocators.APPLY_BUTTON).click()
        self.browser.refresh()
        hidden_photos = self.browser.find_elements(*ProjectPageLocators.HIDDEN_PHOTO_PREVIEW)
        assert len(hidden_photos) == 3, 'Photos are not hidden'

    def show_multiple_photos_in_albums(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM).click()
        self.browser.find_element(*ProjectPageLocators.PHOTO_GROUP_EDIT_BUTTON).click()
        self.browser.find_element(*ProjectPageLocators.FIRST_PHOTO_CHECKBOX).click()
        self.browser.find_element(*ProjectPageLocators.CHOOSE_ALL_CHECKBOXES).click()
        time.sleep(2)
        self.browser.find_element(*ProjectPageLocators.PHOTO_GROUP_EDIT_SELECTOR).click()
        hide_choose = WebDriverWait(self.browser, 3).until(
            EC.element_to_be_clickable(ProjectPageLocators.PHOTO_GROUP_EDIT_SELECTOR_SHOW)
        )
        hide_choose.click()
        self.browser.find_element(*ProjectPageLocators.APPLY_BUTTON).click()
        self.browser.refresh()
        hidden_photos = self.browser.find_elements(*ProjectPageLocators.PHOTO_PREVIEW)
        assert len(hidden_photos) == 3, 'Photos are not revealed'

    def edit_album(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM).click()
        self.browser.find_element(*ProjectPageLocators.EDIT_ALBUM_BUTTON).click()
        time.sleep(2)
        self.browser.find_element(*ProjectPageLocators.ALBUM_NAME_RU).click()
        self.browser.find_element(*ProjectPageLocators.ALBUM_NAME_RU).clear()
        self.browser.find_element(*ProjectPageLocators.ALBUM_NAME_RU).send_keys(EditAlbumData.name_ru_edit)
        self.browser.find_element(*ProjectPageLocators.ALBUM_NAME_EN).click()
        self.browser.find_element(*ProjectPageLocators.ALBUM_NAME_EN).clear()
        self.browser.find_element(*ProjectPageLocators.ALBUM_NAME_EN).send_keys(EditAlbumData.name_en_edit)
        self.browser.find_element(*ProjectPageLocators.ALBUM_DESC_RU).click()
        self.browser.find_element(*ProjectPageLocators.ALBUM_DESC_RU).clear()
        self.browser.find_element(*ProjectPageLocators.ALBUM_DESC_RU).send_keys(EditAlbumData.desc_ru_edit)
        self.browser.find_element(*ProjectPageLocators.ALBUM_DESC_EN).click()
        self.browser.find_element(*ProjectPageLocators.ALBUM_DESC_EN).clear()
        self.browser.find_element(*ProjectPageLocators.ALBUM_DESC_EN).send_keys(EditAlbumData.desc_en_edit)
        self.browser.find_element(*ProjectPageLocators.ALBUM_CREATE_BUTTON).click()
        time.sleep(1)
        self.browser.refresh()
        edited_album = self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM_EDITED)
        assert edited_album.is_displayed(), 'Album is not edited'

    def hide_album(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM).click()
        self.browser.find_element(*ProjectPageLocators.HIDE_SHOW_ALBUM_BUTTON).click()
        visibility_status = self.browser.find_element(*ProjectPageLocators.VISIBILITY_STATUS_ALBUM)
        assert visibility_status.is_displayed(), 'Album is not hidden'

    def show_album(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM).click()
        self.browser.find_element(*ProjectPageLocators.HIDE_SHOW_ALBUM_BUTTON).click()
        time.sleep(2)
        try:
            visibility_status = self.browser.find_element(*ProjectPageLocators.VISIBILITY_STATUS_ALBUM)
            assert not visibility_status.is_displayed(), 'Album is not shown'
        except NoSuchElementException:
            assert True, 'Album is not shown'

    """Not working"""
    def reposition_photos(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        self.browser.find_element(*ProjectPageLocators.SPECIFIC_ALBUM).click()
        time.sleep(2)
        self.browser.find_element(*ProjectPageLocators.PHOTO_POSITION_EDIT).click()
        source = self.browser.find_element(*ProjectPageLocators.POSITION_PHOTO_PREV)
        print(source)
        target = self.browser.find_element(*ProjectPageLocators.POSITION_PHOTO_NEXT)
        print(target)
        actions = ActionChains(self.browser)
        actions.drag_and_drop(source, target).perform()
        self.browser.find_element(*ProjectPageLocators.SAVE_POSITION_BUTTON).click()
        new_position = self.browser.find_element(*ProjectPageLocators.POSITION_PHOTO_NEXT)
        print(new_position)
        assert target != new_position, 'Photo position is not changed'
