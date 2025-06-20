from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://"

#open browser with the link
browser = webdriver.Chrome()
browser.get(link)


#accept cookies and remove banner
time.sleep(3)
button = browser.find_element(By.CLASS_NAME, 'ch2-allow-all-btn')
button.click()
time.sleep(3)

#scroll button into wiev
#buttonSrch = browser.find_element(By.TAG_NAME, 'search-box-mob-store')
#browser.execute_script("return arguments[0].scrollIntoView(true);", buttonSrch)


#find search field, input text
inputSearchText = browser.find_element(By.ID, 'search-box-mob-store')
inputSearchText.send_keys('battersea')
time.sleep(4)

#click on search button
button = browser.find_element(By.ID, 'c-search-btn-mob-store')
button.click()

#add assertion to check card item
linkText = browser.find_element(By.LINK_TEXT, "Battersea Park")
print(linkText.text)
assert "Battersea Park" in linkText.text

#wait, close browser
time.sleep(12)
browser.quit()