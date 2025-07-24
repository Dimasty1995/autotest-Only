from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest

class FooterTest(unittest.TestCase):
    def setUp(self):
        # Запуск браузера Chrome
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
       
        self.driver.get("https://only.digital/")

    def test_footer_elements(self):
        driver = self.driver
        time.sleep(2)

        # Проверка наличия футера
        footer = driver.find_element(By.TAG_NAME, "footer")
        self.assertIsNotNone(footer, "Футер не найден на странице")

        # Проверка наличия логотипа в футере
        logo = footer.find_element(By.XPATH, "//*[@class='Footer_logo__2QEhf']")
        self.assertTrue(logo.is_displayed(), "Логотип в футере не отображается")

        # Проверка наличия кнопки "Начать проект"
        contact = footer.find_element(By.XPATH, "(//button[text()='Начать проект'])[5]")
        self.assertTrue(contact.is_displayed(), "Кнопка (Начать проект) в футере не отображается")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
