# Тесты Opencart
## Описание
Домашние задания по тестам Opencart с помощью Selenium.
## Установка
Для работы требуется установить [Docker](https://www.docker.com/get-started) и [Docker-compose](https://docs.docker.com/compose/install/).  
После установки скачать образы последних версий Firefox и Chrome для Selenoid:  
`docker pull selenoid/firefox`  
`docker pull selenoid/chrome`
## Запуск
Для запуска тестов и окружения выполнить команду:  
`docker-compose up -d`  

Команда установит и запустит Opencart, Selenoid, а затем запустит тесты. Allure-отчёт с результатами тестов будет доступен по адресу http://localhost:4040.
