import random
import string
import random


class LoginData:
    email = 'm.sergeev@magnatmedia.com'
    password = 'GL1kGIm29a'


class RegistrationData:
    email = 'emir-saparo+test@rambler.ru'
    password = 123123123


class PasswordRecoverData:
    email = 'e.saparov@lightdigital.ru'


class BuildData:
    email = 'emir-saparo@rambler.ru'
    password = 'G92gV8GIoo'
    build_full_name = 'Сапаров Эмир Рамблер'


class CreateProjectData:
    full_name_ru = 'Тестовый проект автотест 1'
    full_name_en = 'Test project autotest 1'
    short_name_ru = 'ТПА'
    short_name_en = 'TPA'


class CreateChildProjectData:
    full_name_ru = 'Тестовый подпроект автотест 3'
    full_name_en = 'Test subproject autotest 3'
    short_name_ru = 'ТППА 3'
    short_name_en = 'TSPA 3'


class CreateAlbumData:
    rubric_name = 'тестовая рубрика'
    album_name_ru = 'тестовый альбом'
    album_name_en = 'test album'
    album_desc_ru = 'Этот альбом предназначен для тестов'
    album_desc_en = 'This album for testing purposes'

    album_name_ru_no_filter = 'тестовый альбом без рубрики'
    album_name_en_no_filter = 'test album no rubric'
    album_desc_ru_no_filter = 'Этот альбом предназначен для тестов'
    album_desc_en_no_filter = 'This album for testing purposes'

    album_name_ru_out_of_date = 'тестовый альбом за пределами даты'
    album_name_en_out_of_date = 'test album out of date'
    album_desc_ru_out_of_date = 'Этот альбом предназначен для тестов (за пределами даты'
    album_desc_en_out_of_date = 'This album for testing purposes (out of date)'


class EditProjectData:
    full_name_ru_edit = 'Тестовый проект автотест редактированный'
    full_name_en_edit = 'Test project autotest edited'
    short_name_ru_edit = 'ТПАР'
    short_name_en_edit = 'TPAE'


class EditAlbumData:
    name_ru_edit = 'тестовый альбом редактированный'
    name_en_edit = 'test album edited'
    desc_ru_edit = 'Этот альбом предназначен для тестов редактированный'
    desc_en_edit = 'This album for testing purposes edite'


class IMAPServiceData:
    imap_server = 'imap.mail.ru'
    imap_port = 993
    username = 'e.saparov@lightdigital.ru'
    password = 'UnrhETL4tsCQg4QnGA2g'
