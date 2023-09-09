import os
import time

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# from webdriver_manager.core import driver


###### only for chrome browser #############
@pytest.fixture(autouse=True, scope='function')
# @pytest.fixture(scope="class")
def setup(request):
    ##head less run
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.headless = False
    ##inialize webdriver
    driver = webdriver.Chrome(options=options)
    ## driver.get() to get in to mentioned urll
    driver.get(
        "https://www.ryanair.com/ie/en")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()





