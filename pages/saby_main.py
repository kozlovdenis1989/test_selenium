from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.logger import logger

class SabyMainPage(BasePage):
    CONTACTS = (By.CSS_SELECTOR, ".sbisru-Header__menu-link.sbis_ru-Header__menu-link.sbisru-Header__menu-link--hover")
    CONTACTS_LINK = (By.XPATH, "//a[@class='sbisru-link sbis_ru-link' and @href='/contacts']")
    DOWNLOAD_VERSIONS = (By.XPATH, "//a[@class='sbisru-Footer__link' and @href='/download']")

    def go_to_contacts(self):
        self.skip_load_element(self.PREALOADER)
        logger.info("Переход в раздел 'Контакты'")
        self.find_clicable(self.CONTACTS).click()
        self.find_clicable(self.CONTACTS_LINK).click()

    def download_locals_versions(self):
        self.skip_load_element(self.PREALOADER)
        logger.info("Переход на страницу скачивания версий")
        self.find_clicable(self.DOWNLOAD_VERSIONS).click()
       