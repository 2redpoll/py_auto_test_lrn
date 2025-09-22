from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

buttonFirst = browser.find_element(By.CLASS_NAME, 'btn-primary')
buttonFirst.click()


alert = browser.switch_to.alert
alert.accept()


#calculate x and send result
numberx = browser.find_element(By.ID, 'input_value')
x = calc(numberx.text)
answer = browser.find_element(By.ID, 'answer')
answer.send_keys(x)

submitBtn = browser.find_element(By.CLASS_NAME, 'btn-primary')
submitBtn.click()

#get text from alert
alert_text = alert.text
print(alert_text.split(': ')[-1])

time.sleep(6)
browser.quit()