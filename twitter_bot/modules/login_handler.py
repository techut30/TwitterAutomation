from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginHandler:
    def __init__(self, driver):
        """
        Initialize LoginHandler with WebDriver

        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver

    def login(self, username, password):
        """
        Perform login to Twitter/X

        Args:
            username (str): Twitter/X username
            password (str): Twitter/X password

        Returns:
            bool: True if login successful, False otherwise
        """
        try:
            # Navigate to login page
            self.driver.get("https://x.com/login")

            # Wait for username field and enter username
            username_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "text"))
            )
            username_field.send_keys(username)
            username_field.send_keys(Keys.RETURN)

            # Wait for password field and enter password
            password_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_field.send_keys(password)
            password_field.send_keys(Keys.RETURN)

            # Wait to ensure login
            WebDriverWait(self.driver, 20).until(
                EC.url_contains("home")
            )

            print("Login successful!")
            return True
        except Exception as e:
            print(f"Login failed: {e}")
            return False
