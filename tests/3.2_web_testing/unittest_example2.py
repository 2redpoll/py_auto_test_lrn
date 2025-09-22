from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestReg(unittest.TestCase):
    def test_reg1(self):
        link = "https://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link)

        # Code to fill the fields
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_class input[required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.second_class input[required]")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "div.third_class input[required]")
        input3.send_keys("test@gmail.com")

        # Submit form
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Message check")

    def test_reg2(self):
        link = "https://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)

        # Code to fill the fields
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_class input[required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.second_class input[required]")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "div.third_class input[required]")
        input3.send_keys("test@gmail.com")

        # Submit form
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Message check")



if __name__ == "__main__":
    unittest.main()