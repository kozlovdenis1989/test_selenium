from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.logger import logger

class SabyDownloadPage(BasePage):
    DOWNLOAD_PLUGIN = (By.XPATH, "//a[@class='sbis_ru-DownloadNew-loadLink__link js-link' and contains(., 'Скачать (Exe') ]")


    def download_plagin(self):
        logger.info("Начало скачивания плагина для Windows")
        file = self.find_clicable(self.DOWNLOAD_PLUGIN)
        file_size = float(''.join([item for item in file.text if item.isdigit() or item == '.']))
        file_name = file.get_attribute('href').split('/')[-1]
        file.click()
        logger.info(f"Файл для скачивания: {file_name}, размер: {file_size} МБ (по данным сайта)")
        return file_size, file_name