*** Settings ***
Library    libs/LoginLibrary.py

*** Test Cases ***
Вход в админку
    Открыть браузер
    Войти в админку    user    bitnami1
    Заголовок должен быть    Dashboard

Вход пользователя
    Открыть браузер
    Войти в аккаунт пользователя    test@hotmail.com    testpass
    Заголовок должен быть    My Account
