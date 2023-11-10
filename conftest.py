import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-cache')
    print('\nstart browser...')
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nquit browser...')
    browser.quit()
