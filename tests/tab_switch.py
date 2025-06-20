from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
   return str(math.log(abs(12*(math.sin(int(x))))))

link = 'http://suninjuly.github.io/redirect_accept.html'

browser = webdriver.Chrome()
browser.get(link)



#button click to open new tab
btnClick = browser.find_element(By.CLASS_NAME,  'btn-primary')
btnClick.click()

#switch to the new tab
newWindow = browser.window_handles[1]
browser.switch_to.window(newWindow)

#solve the captcha
getValue = browser.find_element(By.ID, 'input_value')
x = calc(getValue.text)
answer = browser.find_element(By.ID, 'answer')
answer.send_keys(x)
btnSubmit = browser.find_element(By.CLASS_NAME,  'btn-primary')
btnSubmit.click()
alert = browser.switch_to.alert
alertText = alert.text
print(alertText.split(': ')[-1])


#close browser
time.sleep(4)
browser.quit()





#tab  switch
#browser.switch_to.window(window_name)

#window_handles[] return array of all open tabs. two in this case
#for new tab
#new_window = browser.window_handles[1]
#for the current tab
#first_window = browser.window_handles[0]
# or
#current_window = browser.current_window_handle


