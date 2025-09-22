from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    #
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked == "true", "People radio is not selected by default"
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

    time.sleep(10)

    button_disabled = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_dis = button_disabled.get_attribute("Disabled")
    print("value of dutton_dis: ", button_dis)
    assert button_dis == "true"
    #

    """
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    input2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    input2.click()

    input3 = browser.find_element(By.CSS_SELECTOR, "label[for='robotsRule']")
    input3.click()


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    """

    #

    #



finally:
    time.sleep(15)
    browser.quit()