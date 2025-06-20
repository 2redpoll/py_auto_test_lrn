from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#link = "https://suninjuly.github.io/selects1.html"
link = "https://suninjuly.github.io/selects2.html"


browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.ID, "num1")
num2 = browser.find_element(By.ID, "num2")

#print(num1,  num2, sep='\n')

sum = int(num1.text) + int(num2.text)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(sum))
time.sleep(1)

submit = browser.find_element(By.TAG_NAME, 'button').click()

time.sleep(10)
browser.quit()
