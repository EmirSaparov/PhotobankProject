import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.projects_page_locators import ProjectPageLocators
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
import os
from selenium.common.exceptions import NoSuchElementException
from data.data import CreateProjectData, CreateChildProjectData, EditProjectData


class MainPage(BasePage):

    def open_project_from_slider(self):
        project_name = self.browser.find_element(*MainPageLocators.FIRST_SLIDER_PROJECT_NAME).text
        self.browser.find_element(*MainPageLocators.FIRST_SLIDER_PROJECT).click()
        assert project_name == self.browser.find_element(*ProjectPageLocators.PROJECT_TITLE_ON_ITS_PAGE).text, \
            'Wrong project'

    def add_new_project_in_slider(self):
        projects = (self.browser.find_elements(*MainPageLocators.SLIDER_ALL_PROJECTS))
        if len(projects) < 11:
            self.browser.find_element(*MainPageLocators.SLIDER_CONFIG_BUTTON).click()
            time.sleep(3)
            self.browser.find_element(*MainPageLocators.SLIDER_CONFIG_ADD_PROJECT).click()
            time.sleep(3)
            self.browser.find_element(*MainPageLocators.SLIDER_PHOTO_COUNT_RADIOBUTTON).click()
            cover_input = self.browser.find_element(*MainPageLocators.SLIDER_COVER_INPUT)
            cover_input.send_keys(os.getcwd() + '/images/input_logo.jpeg')
            self.browser.find_element(*MainPageLocators.SLIDER_PROJECT_MULTISELECTOR).click()
            self.browser.find_element(*MainPageLocators.SLIDER_MULTISELECTOR_CHOOSE).click()
            time.sleep(3)
            self.browser.find_element(*MainPageLocators.SLIDER_ADD_PROJECT_SUBMIT_BUTTON).click()
            time.sleep(3)
            self.browser.find_element(*MainPageLocators.SLIDER_PREV_PROJECT_BUTTON).click()
            last_proj = self.browser.find_element(*MainPageLocators.LAST_SLIDER_PROJECT_NAME)
            time.sleep(4)
            assert last_proj.text == 'Петербургский международный экономический форум - 2022', 'Project is not added'
        else:
            try:
                self.browser.find_element(*MainPageLocators.SLIDER_CONFIG_BUTTON).click()
                time.sleep(2)
                add_button = self.browser.find_element(*MainPageLocators.SLIDER_CONFIG_ADD_PROJECT)
                assert False == add_button.is_displayed(),\
                    'Кнопка добавления проекта существует при наличии полного слайдера'
            except NoSuchElementException:
                assert True, 'Кнопка добавления проекта существует при наличии полного слайдера'

    def delete_added_project_in_slider(self):
        self.browser.find_element(*MainPageLocators.SLIDER_CONFIG_BUTTON).click()
        time.sleep(3)
        self.browser.find_element(*MainPageLocators.SLIDER_LAST_PROJECT_DELETE_BUTTON).click()
        time.sleep(3)
        self.browser.find_element(*MainPageLocators.SLIDER_ADD_PROJECT_SUBMIT_BUTTON).click()
        time.sleep(3)
        self.browser.find_element(*MainPageLocators.SLIDER_PREV_PROJECT_BUTTON).click()
        last_proj = self.browser.find_element(*MainPageLocators.LAST_SLIDER_PROJECT_NAME)
        time.sleep(4)
        assert last_proj.text != 'Петербургский международный экономический форум - 2022', 'Project is not deleted'

    def slider_can_go_forward_back(self):
        initial_project = self.browser.find_element(*MainPageLocators.FIRST_SLIDER_PROJECT_NAME).text
        self.browser.find_element(*MainPageLocators.SLIDER_NEXT_PROJECT_BUTTON).click()
        time.sleep(3)
        self.browser.find_element(*MainPageLocators.SLIDER_PREV_PROJECT_BUTTON).click()
        time.sleep(3)
        second_check_project = self.browser.find_element(*MainPageLocators.FIRST_SLIDER_PROJECT_NAME).text
        assert initial_project == second_check_project, 'Move buttons does not work'

    def go_to_projects_from_description(self):
        self.browser.find_element(*MainPageLocators.PROJECTS_LINK_FROM_DESCRIPTION).click()
        assert WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProjectPageLocators.PROJECTS_PAGE_TITLE)
        ), 'Projects page is not loaded'

    def more_projects_button(self):
        self.browser.find_element(*MainPageLocators.ALL_PROJECTS_BUTTON).click()
        assert WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProjectPageLocators.PROJECTS_PAGE_TITLE)
        ), 'Projects page is not loaded'

    def potd_slider_can_go_forward_back(self):
        initial_picture = self.browser.find_element(*MainPageLocators.POTD_CURRENT_PICTURE)
        initial_picture_attr = initial_picture.get_attribute('src')
        self.browser.find_element(*MainPageLocators.POTD_NEXT_BUTTON).click()
        time.sleep(3)
        self.browser.find_element(*MainPageLocators.POTD_PREV_BUTTON).click()
        time.sleep(3)
        second_check_picture = self.browser.find_element(*MainPageLocators.POTD_CURRENT_PICTURE)
        second_check_picture_attr = second_check_picture.get_attribute('src')
        assert initial_picture_attr == second_check_picture_attr, 'Move buttons does not work'

    def create_parental_project(self):
        self.browser.execute_script("window.scrollBy(0, 500);")
        time.sleep(3)
        self.browser.find_element(*MainPageLocators.PROJECT_ADD_BUTTON).click()
        full_name_input_ru = self.browser.find_element(*MainPageLocators.FULL_NAME_RU_INPUT)
        full_name_input_ru.send_keys(CreateProjectData.full_name_ru)
        full_name_input_en = self.browser.find_element(*MainPageLocators.FULL_NAME_EN_INPUT)
        full_name_input_en.send_keys(CreateProjectData.full_name_en)
        short_name_input_ru = self.browser.find_element(*MainPageLocators.SHORT_NAME_RU_INPUT)
        short_name_input_ru.send_keys(CreateProjectData.short_name_ru)
        short_name_input_en = self.browser.find_element(*MainPageLocators.SHORT_NAME_EN_INPUT)
        short_name_input_en.send_keys(CreateProjectData.short_name_en)
        logo_input = self.browser.find_element(*MainPageLocators.LOGO_INPUT)
        logo_input.send_keys(os.getcwd()+'/images/test_logo.jpg')
        time.sleep(2)
        self.browser.find_element(*MainPageLocators.LOGO_APPLY_BUTTON).click()
        modal_element = self.browser.find_element(*MainPageLocators.PROJECT_ADD_MODAL)
        self.browser.execute_script("window.scrollBy(0, 800);", modal_element)
        time.sleep(2)
        self.browser.find_element(*MainPageLocators.PARENT_PROJECT_CHECKBOX).click()
        self.browser.find_element(*MainPageLocators.PROJECT_START_DATE).click()
        self.browser.find_element(*MainPageLocators.PROJECT_ADD_TODAY_DATE).click()
        self.browser.find_element(*MainPageLocators.PROJECT_SELECT_DATE_BUTTON).click()
        self.browser.find_element(*MainPageLocators.PROJECT_END_DATE).click()
        self.browser.find_element(*MainPageLocators.PROJECT_ADD_TODAY_DATE).click()
        self.browser.find_element(*MainPageLocators.PROJECT_SELECT_DATE_BUTTON).click()
        time.sleep(2)
        self.browser.find_element(*MainPageLocators.PROJECT_CREATE_BUTTON).click()
        created_project = self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT)
        assert created_project.is_displayed(), 'Project not created'

    def create_child_project(self):
        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        time.sleep(3)
        self.browser.find_element(*MainPageLocators.PROJECT_ADD_BUTTON).click()
        full_name_input_ru = self.browser.find_element(*MainPageLocators.FULL_NAME_RU_INPUT)
        full_name_input_ru.send_keys(CreateChildProjectData.full_name_ru)
        full_name_input_en = self.browser.find_element(*MainPageLocators.FULL_NAME_EN_INPUT)
        full_name_input_en.send_keys(CreateChildProjectData.full_name_en)
        short_name_input_ru = self.browser.find_element(*MainPageLocators.SHORT_NAME_RU_INPUT)
        short_name_input_ru.send_keys(CreateChildProjectData.short_name_ru)
        short_name_input_en = self.browser.find_element(*MainPageLocators.SHORT_NAME_EN_INPUT)
        short_name_input_en.send_keys(CreateChildProjectData.short_name_en)
        logo_input = self.browser.find_element(*MainPageLocators.LOGO_INPUT)
        logo_input.send_keys(os.getcwd() + '/images/test_logo.jpg')
        time.sleep(2)
        self.browser.find_element(*MainPageLocators.LOGO_APPLY_BUTTON).click()
        modal_element = self.browser.find_element(*MainPageLocators.PROJECT_ADD_MODAL)
        self.browser.execute_script("window.scrollBy(0, 800);", modal_element)
        time.sleep(2)
        self.browser.find_element(*MainPageLocators.PROJECT_START_DATE).click()
        self.browser.find_element(*MainPageLocators.PROJECT_ADD_TODAY_DATE).click()
        self.browser.find_element(*MainPageLocators.PROJECT_SELECT_DATE_BUTTON).click()
        self.browser.find_element(*MainPageLocators.PROJECT_END_DATE).click()
        self.browser.find_element(*MainPageLocators.PROJECT_ADD_TODAY_DATE).click()
        self.browser.find_element(*MainPageLocators.PROJECT_SELECT_DATE_BUTTON).click()
        multiselector_input = self.browser.find_element(*MainPageLocators.PROJECT_PARENTAL_MULTISELECTOR)
        multiselector_input.send_keys('ТПА')
        self.browser.find_element(*MainPageLocators.PROJECT_PARENTAL_MULTISELECTOR_CHOOSE).click()
        time.sleep(2)
        """Когда Макс исправит выбор элементов в селекторе надо убрать нижние 2 строки"""
        self.browser.find_element(*MainPageLocators.PARENT_PROJECT_CHECKBOX).click()
        self.browser.find_element(*MainPageLocators.PARENT_PROJECT_CHECKBOX).click()

        self.browser.find_element(*MainPageLocators.PROJECT_CREATE_BUTTON).click()
        time.sleep(2)
        created_project = self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT)
        assert created_project.is_displayed(), 'Project is not created'

    """Пока не работает полностью !!!"""
    def edit_project(self):
        self.browser.find_element(*MainPageLocators.SPECIFIC_PROJECT).click()
        self.browser.find_element(*MainPageLocators.SPECIFIC_SUBPROJECT).click()
        self.browser.find_element(*MainPageLocators.PROJECT_EDIT_BUTTON).click()
        time.sleep(2)
        self.browser.find_element(*MainPageLocators.FULL_NAME_RU_INPUT).click()
        self.browser.find_element(*MainPageLocators.FULL_NAME_RU_INPUT).clear()
        self.browser.find_element(*MainPageLocators.FULL_NAME_RU_INPUT).send_keys(EditProjectData.full_name_ru_edit)
        self.browser.find_element(*MainPageLocators.FULL_NAME_EN_INPUT).click()
        self.browser.find_element(*MainPageLocators.FULL_NAME_EN_INPUT).clear()
        self.browser.find_element(*MainPageLocators.FULL_NAME_EN_INPUT).send_keys(EditProjectData.full_name_en_edit)
        self.browser.find_element(*MainPageLocators.SHORT_NAME_RU_INPUT).click()
        self.browser.find_element(*MainPageLocators.SHORT_NAME_RU_INPUT).clear()
        self.browser.find_element(*MainPageLocators.SHORT_NAME_RU_INPUT).send_keys(EditProjectData.short_name_ru_edit)
        self.browser.find_element(*MainPageLocators.SHORT_NAME_EN_INPUT).click()
        self.browser.find_element(*MainPageLocators.SHORT_NAME_EN_INPUT).clear()
        self.browser.find_element(*MainPageLocators.SHORT_NAME_EN_INPUT).send_keys(EditProjectData.short_name_en_edit)
        time.sleep(2)
        self.browser.find_element(*MainPageLocators.PROJECT_END_DATE).click()
        self.browser.find_element(*MainPageLocators.PROJECT_ADD_TODAY_DATE).click()
        self.browser.find_element(*MainPageLocators.PROJECT_SELECT_DATE_BUTTON).click()
        time.sleep(2)
        self.browser.find_element(*MainPageLocators.PROJECT_CREATE_BUTTON).click()
        time.sleep(5)
        edited_project = self.browser.find_element(*MainPageLocators.EDITED_SPECIFIC_SUBPROJECT)
        assert edited_project.is_displayed(), 'Project is not edited'
