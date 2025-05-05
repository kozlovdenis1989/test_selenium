from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from .base_page import BasePage
from utils.logger import logger
import time

class SabyContactsPage(BasePage):
    TENSOR_BANNER = (By.CSS_SELECTOR, ".sbisru-Contacts__logo-tensor.mb-12")
    MY_REGION = (By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text.sbis_ru-link")
    SELECT_REGION = (By.XPATH, "//span[@class='sbis_ru-link' and @title='Камчатский край']")
    NUM_REGION = (By.XPATH, "//span[@class='controls-DecoratorHighlight' and contains(., 'Камчатский край') ]")
    PARTNERS = (By.CSS_SELECTOR, ".sbisru-Contacts-List__name.sbisru-Contacts-List--ellipsis.sbisru-Contacts__text--md.pb-4.pb-xm-12.pr-xm-32") 
    REGION_PANEL = (By.CSS_SELECTOR, ".sbis_ru-Region-Panel.sbis_ru-Region-Panel-l")

    def click_tensor_banner(self):
        logger.info("Переход по баннеру Тензор")
        self.skip_load_element(self.PREALOADER)
        element = self.find_clicable(self.TENSOR_BANNER)
        self.click_and_switch_to_new_tab(element)

    def my_region_and_list_partners(self):
         
        try:
            my_region = self.find_visibility(self.MY_REGION).text
            list_of_partners = [partners.text for partners in self.finds_visibility(self.PARTNERS)]
        except StaleElementReferenceException as e:
            logger.warning(f"Обновление DOM: StaleElementReferenceException — повторяем попытку: {e}")
            my_region = self.find_visibility(self.MY_REGION).text
            list_of_partners = [partners.text for partners in self.finds_visibility(self.PARTNERS)]
        logger.info(f"Регион на странице: {my_region}. Кол-во партнёров: {len(list_of_partners)}.")
        return my_region, list_of_partners

    def select_region(self):
        self.skip_load_element(self.PREALOADER)
        logger.info("Клик выбора региона")
        self.find_clicable(self.MY_REGION).click()
        select_region = self.find_clicable(self.SELECT_REGION)
        region_name = select_region.get_attribute('title')
        region_num = self.find_visibility(self.NUM_REGION).text[:2]
   
        try :
            select_region.click()
            self.skip_load_element(self.REGION_PANEL, timeout=3)
        except TimeoutException as e:
            logger.warning(f"Панель выбора регионов не закрылась, регион не выбран  — повторяем клик.")
            select_region.click()
            self.skip_load_element(self.REGION_PANEL)

        logger.info(f"Выбран регион: {region_name}, его код: {region_num}")
        return region_name, region_num
        
        
    