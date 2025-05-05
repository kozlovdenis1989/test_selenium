import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import os

@pytest.fixture(scope="function")
def browser():
    download_dir = os.path.dirname(os.path.abspath(__file__))
    
    options = Options()
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.dir", download_dir)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf,application/octet-stream")
    options.set_preference("pdfjs.disabled", True)

    service = Service(GeckoDriverManager().install())

    driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()