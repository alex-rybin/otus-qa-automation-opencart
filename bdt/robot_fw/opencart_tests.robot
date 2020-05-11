*** Settings ***
Library    SeleniumLibrary
Test Setup    Setup
Test Teardown    Close Browser

*** Variables ***
${SERVER}          otus-qa-automation-opencart_opencart_1
${BROWSER}         Firefox
${USER}            user
${PASSWORD}        bitnami1
${EXECUTOR_URL}    http://localhost:4444/wd/hub


*** Keywords ***
Setup
    ${desiredCapablities}    Create Dictionary    acceptInsecureCerts=${TRUE}
    Open Browser    http://${SERVER}/    ${BROWSER}    remote_url=${EXECUTOR_URL}    desired_capabilities=${desiredCapablities}
    Set Selenium Implicit Wait    5

Открыть админку и войти
    Go To    http://${SERVER}/admin
    Input Text      id:input-username    ${USER}
    Input Text      id:input-password    ${PASSWORD}
    Click Button    css:button[type='submit']

Заголовок должен быть
    [Arguments]    ${title}
    Title Should Be    ${title}

Открыть страницу товаров
    Click Element    id:menu-catalog
    Click Element    link:Products

Ввести текст в фильтр по имени
    [Arguments]    ${name}
    Input Text    id:input-name    ${name}

Нажать кнопку применения фильтров
    Click Button    id:button-filter

Таблица товаров должна содержать
    [Arguments]    ${text}
    Table Should Contain    id:form-product    ${text}

Выйти из админки
    Click Element    xpath://span[text()="Logout"]

Открыть редактирование пользователя
    Click Element    xpath://a[@data-toggle="dropdown"]
    Click Element    xpath://a[text()=" Your Profile"]

Добавить новый продукт
    [Arguments]    ${name}    ${meta}    ${model}
    Click Element    xpath://a[@data-original-title="Add New"]
    Input Text    id:input-name1    ${name}
    Input Text    id:input-meta-title1    ${meta}
    Click Element    xpath://a[@href="#tab-data"]
    Input Text    id:input-model    ${model}
    Click Element    xpath://button[@data-original-title="Save"]

*** Test Cases ***
Админка успешно открывается
    Открыть админку и войти
    Заголовок должен быть    Dashboard


Работает фильтр по товарам
    Открыть админку и войти
    Открыть страницу товаров
    Ввести текст в фильтр по имени    iPhone
    Нажать кнопку применения фильтров
    Таблица товаров должна содержать    iPhone


Работает выход из админки
    Открыть админку и войти
    Выйти из админки
    Заголовок должен быть    Administration


Открываются настройки профиля
    Открыть админку и войти
    Открыть редактирование пользователя
    Заголовок должен быть    Profile


Товар добавляется
    Открыть админку и войти
    Открыть страницу товаров
    Добавить новый продукт    Aaaa    BBBB    CCcc
    Таблица товаров должна содержать    Aaaa
