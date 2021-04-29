from selenium import webdriver
import time
import unittest

class TestLessons(unittest.TestCase):
    def test_lessons1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

    # Ваш код, который заполняет обязательные поля
        first_name=browser.find_element_by_css_selector("input[placeholder='Input your first name']")
        first_name.send_keys("First_name")
    
        first_name=browser.find_element_by_css_selector("input[placeholder='Input your last name']")
        first_name.send_keys("LastName")
    
        first_name=browser.find_element_by_css_selector("input[placeholder='Input your email']")
        first_name.send_keys("test@test.com")

    # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
        time.sleep(1)

    # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Регистрация ошибочна")

    def test_lessons2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

    # Ваш код, который заполняет обязательные поля
        first_name=browser.find_element_by_css_selector("input[placeholder='Input your first name']")
        first_name.send_keys("First_name")
    
        first_name=browser.find_element_by_css_selector("input[placeholder='Input your last name']")
        first_name.send_keys("LastName")
    
        first_name=browser.find_element_by_css_selector("input[placeholder='Input your email']")
        first_name.send_keys("test@test.com")

    # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
        time.sleep(1)

    # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Регистрация ошибочна")

if __name__ == "__main__":
    unittest.main()

