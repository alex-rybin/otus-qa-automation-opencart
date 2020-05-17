Feature: Основной функционал Opencart

  Scenario: Поиск на главной странице
    When открыта главная страница
    And ввожу текст в поле поиска
    And нажимаю кнопку поиска
    Then открылась страница результатов, содержащая только товары с искомым словом в названии

  Scenario: Добавление товара в корзину
    When открыта страница любого товара
    And нажимаю кнопку Add to Cart
    Then появилось сообщение об успехе добавления в корзину

  Scenario: Проверка товара в корзине
    When открыта страница любого товара
    And нажимаю кнопку Add to Cart
    And нажимаю кнопку Shopping Cart
    Then добавленный товар отображается в корзине

  Scenario: Добавление товара в заданном количестве
    When открыта страница любого товара
    And ввожу в поле Qty количество товара большее, чем 1
    And нажимаю кнопку Add to Cart
    And нажимаю кнопку Shopping Cart
    Then добавленный товар отображается в корзине, в поле Quantity указано введённое количество

  Scenario: Уведомление при попытке добавить товар в список желаемого с главной страницы без входа
    When открыта главная страница
    And нажимаю кнопку добавления в список желаемого у любого товара
    Then появилось сообщение о необходимости входа или регистрации