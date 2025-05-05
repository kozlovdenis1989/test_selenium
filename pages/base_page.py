from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from utils.logger import logger

class BasePage:
    PREALOADER = (By.CLASS_NAME, "preload-overlay")

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        logger.info(f"Открытие страницы: {url}")
        self.driver.get(url)

    def find(self, locator, timeout=10):
        logger.debug(f"Поиск элемента: {locator}")
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def finds(self, locator, timeout=10):
        logger.debug(f"Поиск всех элементов: {locator}")
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def finds_visibility(self, locator, timeout=10):
        logger.debug(f"Поиск всех видимых элементов: {locator}")
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def find_visibility(self, locator, timeout=10):
        logger.debug(f"Поиск видимого элемента: {locator}")
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def find_clicable(self, locator, timeout=10):
        logger.debug(f"Ожидание кликабельности элемента: {locator}")
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def skip_load_element(self, locator, timeout=10):
        logger.debug(f"Ожидание исчезновения элемента загрузки: {locator}")
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def click_and_switch_to_new_tab(self, element, timeout=10):
        logger.info("Клик по элементу и переход на новую вкладку")
        old_tabs = self.driver.window_handles
        element.click()
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > len(old_tabs))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.current_url != "about:blank" and d.current_url != ""
            )
        except TimeoutException:
            logger.warning("URL вкладки остался about:blank — страница не загрузилась?")
        logger.info(f"Текущий адрес вкладки: {self.driver.current_url}")
        return self.driver.current_url

    def scroll_to_element(self, element):
        logger.debug("Скролл к элементу на странице")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    