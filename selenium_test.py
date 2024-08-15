"""Импорт драйвера и создание подключения к браузеру"""
import unittest
import time
from selenium import webdriver
from unittest import TestCase

"""Подключение к браузеру. Если порт 9222 занят - выберите любой другой свободный"""
driver_options = webdriver.ChromeOptions()
driver_options.debugger_address = 'localhost:9222'
driver = webdriver.Chrome(options=driver_options)

"""Настройка браузера:
В ярлыке в поле 'объект' укажите --remote-debugging-port=9222 --user-data-dir=remote-profile
Пример: 
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir=remote-profile
Внимание!
Запуск браузера обязательно от Администратора"""

"""Все тестируемые элементы"""
link_ya = ["xpath", "//*[@aria-label='Яндекс']"]
button_mail = ["xpath", "//*[text()='Почта']/.."]
button_telephone = ["xpath", "//*[text()='Телефон']/.."]
login_zone = ["xpath", "//*[@name='login']"]
input_telephone = ["xpath", "//*[@class='Textinput-Box']/../input"]
button_enter = ["xpath", "//*[text()='Войти']/.."]
button_face = ["xpath", "//*[contains(text(), 'лицу')]//ancestor::button"]
button_create_id = ["xpath", "(//*[contains(text(), 'ID')]//ancestor::a)[2]"]
button_qr = ["xpath", "//*[contains(text(), 'QR')]//ancestor::button"]
button_more = ["xpath", "//*[text()='Ещё']//ancestor::button"]
link_more = ["xpath", "//*[text()='Узнать больше']"]
link_lang = ["xpath", "//*[text()='Ru']"]
link_help = ["xpath", "//*[contains(text(), 'Справка')]"]
link_ya_text = ["xpath", "//*[text()='Яндекс']"]
link_incognito = ["xpath", "//*[contains(text(), 'инкогнито')]"]

"""Тестирование ссылок 'А' 
    1. link_incognito
    2. link_help 
    3. link_ya
    4. link_more
    5. link_ya_text
    6. button_qr
    7. button_more
"""

result_links_test = ["https://yandex.ru/support2/common/ru/browsers-settings/incognito.html",
                     "https://yandex.ru/support/id/",
                     "https://ya.ru/",
                     "https://yandex.ru/id/about",
                     "https://ya.ru/",
                     "https://passport.yandex.ru/auth/magic",
                     "https://passport.yandex.ru/auth/social-restricted"]

links_test = [link_incognito,
              link_help,
              link_ya,
              link_more,
              link_ya_text,
              button_qr,
              button_more]

"""https://passport.yandex.ru/auth/"""


class Test_link(TestCase):
    """Описание теста
    1. Нажимаем на ссылку 'Используйте режим инкогнито на чужом компьютере'
    2. Получаем список открытых окон в браузере
    3. Переходим на новую вкладку
    4. Получаем адрес ссылки и сравниваем с заранее известным Верным результатом
    5. Закрываем новую вкладку
    6. Возвращаемся на стартовый экран
    """

    def test_link_a(self):
        """100%"""
        for i, expected in enumerate(result_links_test[:2]):
            with self.subTest(i):
                driver.find_element(*links_test[i]).click()
                web_list = driver.window_handles
                driver.switch_to.window(web_list[1])
                result = driver.current_url
                driver.close()
                driver.switch_to.window(web_list[0])
                self.assertEqual(expected, result, msg="Тестирование ссылки: "
                                                       "Используйте режим инкогнито на чужом компьютере")

    def test_link_ya(self):
        """100%"""
        for i, link in enumerate(links_test[2:7], start=2):
            with self.subTest(i):
                driver.find_element(*link).click()
                result = driver.current_url
                driver.back()
                time.sleep(1)
                self.assertEqual(result_links_test[i], result, msg="Тестирование ссылок: "
                                                                   "YA.RU")


"""Тестирование кнопок
    1. button_telephone
    2. button_mail
    3. button_enter
    4. button_create_id
"""
all_button = [button_telephone, button_mail, button_enter, button_create_id]
button_ok = ["button:default", "button:default", "true", "true"]
attribute = ['data-t', 'aria-disabled', 'aria-expanded']


class Test_value(TestCase):
    """Описание теста
    1. Нажимаем на ссылку
    2. Запрашиваем значения атрибутов
    3. Сверяем атрибуты с ожидаемыми Верными значениями
    """

    def test_button_value(self):
        """100%"""
        for i, button in enumerate(all_button):
            with self.subTest(i):
                driver.find_element(*button).click()
            if i < 2:
                result = driver.find_element(*button).get_attribute(attribute[0])
            elif i == 2:
                result = driver.find_element(*button).get_attribute(attribute[1])
            elif i == 3:
                result = driver.find_element(*button).get_attribute(attribute[2])
            self.assertEqual(button_ok[i], result, msg="Тестирование кнопок")


"""Тестирование ввода
    1. login_zone
    2. input_telephone
"""

zone_test = [login_zone, input_telephone]
value_test = ["Инкогнито", "+7 (999) 999-99-99999"]


class Test_input(TestCase):
    """Описание теста
    1. Вводим заранее заготовленные значения
    2. Запрашиваем значения атрибутов
    3. Сверяем атрибуты с ожидаемыми Верными значениями
    """

    def test_button_value(self):
        """100%"""
        for i, test_in in enumerate(zone_test):
            with self.subTest(i):
                if i == 0:
                    driver.find_element(*test_in).send_keys(value_test[i])
                    result = driver.find_element(*test_in).get_attribute('value')
                else:
                    driver.find_element(*button_telephone).click()
                    driver.find_element(*test_in).clear()
                    driver.find_element(*test_in).send_keys(value_test[i])
                    result = driver.find_element(*test_in).get_attribute('value')
                self.assertEqual(value_test[i], result, msg="Тестирование кнопок")

if __name__ == "__main__":
    unittest.main()