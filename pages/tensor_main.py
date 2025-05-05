from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.logger import logger

class TensorMainPage(BasePage):
    SILA_LUDEY_BLOCK = (By.CSS_SELECTOR,  ".tensor_ru-Index__block4-content.tensor_ru-Index__card")
    SILA_LUDEY_MORE = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content.tensor_ru-Index__card a")

    def sila_v_lyudyakh_block_exists(self):
        try:
            self.find(self.SILA_LUDEY_BLOCK)
            logger.info("Блок 'Сила в людях' найден")
            return True
        except Exception as e:
            logger.warning(f"Блок 'Сила в людях' не найден: {e}")
            return False

    def go_to_about(self):
        logger.info("Переход на страницу 'О компании'")
        element = self.find(self.SILA_LUDEY_BLOCK)
        self.scroll_to_element(element)
        self.skip_load_element(self.PREALOADER)
        self.find_clicable(self.SILA_LUDEY_MORE).click()