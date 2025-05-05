## Автотест sbis/ru

### Структура:
selenium_test/  
│  
├── pages/  
│   ├── __init__.py  
│   ├── base_page.py  
│   ├── saby_main.py  
│   ├── saby_contacts.py  
│   ├── saby_download.py  
│   ├── tensor_main.py  
│   ├── tensor_about.py  
│    
│
├── tests/  
│   ├── __init__.py  
│   ├── test_sbis.py  
│     
│  
├── utils/  
│   ├── __init__.py  
│   ├── logger.py  
│── logs/  
│       └── selenium_tests.log  
├── conftest.py        
├── requirements.txt    
├── README.md 


 ### Запуск тестов:
    
    - Установить зависимости requirements.txt
    - Выполнить команду pytest в корне проекта
  

 ### Логи:

   Файл логов находится в папке **utils/logs**

 ### Стек:
   - pytest
   - selenium
   - webdriver-manager
   - logging
