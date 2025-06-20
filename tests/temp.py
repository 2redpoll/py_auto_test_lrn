from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_registration(link):
    try:
        # Инициализация драйвера
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполнение обязательных полей
        first_name_input = browser.find_element(By.CSS_SELECTOR, "input.first:required")
        first_name_input.send_keys("Ivan")

        last_name_input = browser.find_element(By.CSS_SELECTOR, "input.second:required")
        last_name_input.send_keys("Petrov")

        email_input = browser.find_element(By.CSS_SELECTOR, "input.third:required")
        email_input.send_keys("ivan@example.com")

        # Отправка формы
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверка сообщения об успешной регистрации
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        # Убедимся, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text, "Test failed"

    finally:
        # Закрытие браузера
        time.sleep(2)
        browser.quit()


# Тест для первой страницы (должен пройти успешно)
test_registration("http://suninjuly.github.io/registration1.html")

# Тест для второй страницы (должен упасть с ошибкой NoSuchElementException)
try:
    test_registration("http://suninjuly.github.io/registration2.html")
except Exception as e:
    print(f"Test failed with exception: {e}")