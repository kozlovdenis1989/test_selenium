from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.logger import logger

class TensorAboutPage(BasePage):

    HISTORY_BLOCK = (By.CSS_SELECTOR, '.tensor_ru-header-h2.tensor_ru-About__block-title')
    IMAGES = (By.CSS_SELECTOR, '.tensor_ru-About__block3-image-wrapper')
    
    def get_history_img_sizes(self):
        element = self.find(self.HISTORY_BLOCK)
        self.scroll_to_element(element) 
        images = self.finds(self.IMAGES)
        sizes = [img.size for img in images]
        logger.info(f"Список размеров изображений {sizes} ")
        return sizes