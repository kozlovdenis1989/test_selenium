from pages.saby_main import SabyMainPage
from pages.saby_contacts import SabyContactsPage
from pages.tensor_main import TensorMainPage
from pages.tensor_about import TensorAboutPage
from pages.saby_download import SabyDownloadPage
from utils.logger import logger
import os
import time


def test_1(browser):
    logger.info("Старт 'Тест 1'")
    logger.info("Перейти на https://sbis.ru/ в раздел 'Контакты'")

    url = "https://sbis.ru/"
    main = SabyMainPage(browser)
    main.open("https://sbis.ru/")
    main.go_to_contacts()
    logger.info(f'Текущий url: {browser.current_url}')
    
    logger.info("Найти баннер 'Тензор', кликнуть по нему. Перейти на https://tensor.ru/")
    contacts = SabyContactsPage(browser)
    contacts.click_tensor_banner()

    logger.info("Проверить, что есть блок 'Сила в людях'")
    tensor_main = TensorMainPage(browser)
    assert tensor_main.sila_v_lyudyakh_block_exists()

    logger.info("Перейти в этом блоке в 'Подробнее' и убедиться, что открывается /about")
    tensor_main.go_to_about()
    assert "tensor.ru/about" in browser.current_url

    logger.info("Проверяем фото хронологии")  
    tensor_about = TensorAboutPage(browser)
    sizes = tensor_about.get_history_img_sizes()
    heights = {sz['height'] for sz in sizes}
    widths = {sz['width'] for sz in sizes}
    assert len(heights) == 1 and len(widths) == 1, "Размеры фото отличаются: {}x{}".format(heights, widths)

    logger.info("'Тест 1' завершен успешно")

def test_2(browser):
    logger.info("Старт 'Тест 2'")
    MY_REGION = 'москва'

    logger.info('Перейти на https://sbis.ru/ в раздел "Контакты"')
    main = SabyMainPage(browser)
    main.open("https://sbis.ru/")
    main.go_to_contacts()
    logger.info(f'Текущий url: {browser.current_url}')

    logger.info('Проверить, что определился ваш регион (в нашем примере Ярославская обл.) и есть список партнеров.')
    contacts = SabyContactsPage(browser)
    my_region, list_of_partners = contacts.my_region_and_list_partners()
    # Эта строка закомментирована так как у вас может быть другой регион. Сейчас проверяется наличие текста.
    # Раскомментируйте сроку и выберите MY_REGION.
    # assert MY_REGION in  my_region.lower() 
    assert my_region
    assert 1 <= len(list_of_partners)
    partner_old = list_of_partners[0]

    logger.info('Изменить регион на "Камчатский край"')
    select_region, num_region = contacts.select_region()
    
    logger.info('Проверить, что подставился выбранный регион, список партнеров изменился, url и title содержат информацию выбранного региона')
    my_region, list_of_partners_new = contacts.my_region_and_list_partners()
    browser_url = browser.current_url
    browser_title = browser.title
    logger.info(f'Текущий url: {browser_url}, текущий title: {browser_title}')
    assert select_region == my_region
    assert 1 <= len(list_of_partners_new)
    assert partner_old != list_of_partners_new[0]
    assert num_region in browser_url
    assert my_region in browser_title

    logger.info('"Тест 2" завершен успешно')
    
def test_3(browser):
    logger.info('Старт тест 3')

    logger.info('Перейти на https://sbis.ru/') 
    main = SabyMainPage(browser)
    main.open("https://sbis.ru/")

    logger.info('В Footere найти и перейти "Скачать локальные версии"')
    main.download_locals_versions()
    
    logger.info('Скачать "СБИС Плагин для вашей для windows", веб-установщик в папку с данным тестом')
    download = SabyDownloadPage(browser)
    file_size, file_name = download.download_plagin()
    
    logger.info('Убедиться, что плагин скачался')
    current_dir = os.path.dirname(os.path.abspath(__file__))
    selenium_test_dir = os.path.dirname(current_dir)
    file_path = os.path.join(selenium_test_dir, file_name)
    
    timeout = 30
    elapsed = 0
    while (not os.path.isfile(file_path) or file_path.endswith(('.crdownload', '.part'))) and elapsed < timeout:
        time.sleep(0.5)
        elapsed += 0.5
    if not os.path.isfile(file_path):
        logger.info('Плагин не скачан')
        assert False
    logger.info('Плагин скачан')
    time.sleep(5)

    logger.info('Сравнить размер скачанного файла в мегабайтах. Он должен совпадать с указанным на сайте.')
    filesize_bytes = os.path.getsize(file_path)
    filesize_mb = round(filesize_bytes / (1024 * 1024), 2) 
    logger.info(f'Размер скачаного файла {filesize_mb}')
    assert file_size == filesize_mb

    logger.info('Тест 3 завершен успешно')