from selenium import webdriver
from selenium.webdriver.safari.service import Service
from selenium.webdriver.safari.options import Options

class DriverManager:
    @staticmethod
    def setup_safari_driver():
        """
        Set up and configure Safari WebDriver

        Returns:
            webdriver.Safari: Configured Safari WebDriver instance
        """
        try:
            # Safari-specific configuration
            safari_options = Options()

            # Initialize WebDriver
            driver = webdriver.Safari()

            # Set common driver configurations
            driver.implicitly_wait(10)  # Wait up to 10 seconds for elements
            driver.set_page_load_timeout(30)  # Set page load timeout

            return driver
        except Exception as e:
            print(f"Error setting up Safari WebDriver: {e}")
            return None

    def quit_driver(self, driver):
        """
        Safely quit the WebDriver

        Args:
            driver: WebDriver instance to quit
        """
        if driver:
            try:
                driver.quit()
                print("WebDriver closed successfully")
            except Exception as e:
                print(f"Error closing WebDriver: {e}")
