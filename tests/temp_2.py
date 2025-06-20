from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#import math

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.first")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.second")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.third")
    email.send_keys("Test@email.ru")



    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)

    browser.quit()