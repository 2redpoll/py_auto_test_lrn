from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")


#waiting for price value 100 befor button click
buttonWait = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
)
button = browser.find_element(By.ID, "book")
button.click()

numberx = browser.find_element(By.ID, 'input_value')
x = calc(numberx.text)
answer = browser.find_element(By.ID, 'answer')
answer.send_keys(x)

submitBtn = browser.find_element(By.ID, 'solve')
submitBtn.click()

alert = browser.switch_to.alert
alertText = alert.text
print(alertText.split(": ")[-1])

time.sleep(4)
browser.quit()