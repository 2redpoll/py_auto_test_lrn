from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

#Заполнить текстовые поля: имя, фамилия, email
input1 = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
input1.send_keys('Vlad')

input2 = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
input2.send_keys('Petrov')

input3 = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
input3.send_keys('test@gmail.com')

#Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'testfile.txt')       # добавляем к этому пути имя файла
input_file = browser.find_element(By.ID, 'file')      # поиск кнопки загрузки файла
input_file.send_keys(file_path)                             # загрузка файла

print(os.path.abspath(__file__))
print(os.path.dirname(__file__))

#Нажать кнопку "Submit"
browser.find_element(By.TAG_NAME, 'button').click()

time.sleep(10)
browser.quit()