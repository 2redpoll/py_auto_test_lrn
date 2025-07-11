from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"


browser = webdriver.Chrome()
browser.get(link)



x = browser.find_element(By.ID, 'input_value')
answer = calc(x.text)

browser.find_element(By.ID, 'answer').send_keys(answer)

browser.find_element(By.ID, 'robotCheckbox').click()

button = browser.find_element(By.TAG_NAME, 'button')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

browser.find_element(By.ID, 'robotsRule').click()

time.sleep(1)

button = browser.find_element(By.TAG_NAME, 'button')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(15)
browser.quit()