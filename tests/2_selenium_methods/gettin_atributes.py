from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # получение значения valuex из атрибута
    image_get = browser.find_element(By.ID, "treasure")
    x = image_get.get_attribute("valuex")
    y = calc(x)

    # ввод значения в поле
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    # Отметить checkbox "I'm the robot".
    checkbox_find = browser.find_element(By.ID, "robotCheckbox")
    checkbox_find.click()

    # Выбрать radiobutton "Robots rule!".
    radio_find = browser.find_element(By.ID, "robotsRule")
    radio_find.click()

    # Нажать на кнопку "Submit".
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()