from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

class ProfileManager:
    def __init__(self, driver, username):
        """
        Initialize ProfileManager with WebDriver and username

        Args:
            driver: Selenium WebDriver instance
            username (str): Twitter/X username
        """
        self.driver = driver
        self.username = username

    def update_bio(self, new_bio=None):
        """
        Update Twitter/X profile bio

        Args:
            new_bio (str, optional): New bio text.
                                     If None, generates a timestamp-based bio.

        Returns:
            bool: True if bio updated successfully, False otherwise
        """
        try:
            # Generate default bio if no text provided
            if new_bio is None:
                new_bio = f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"

            # Navigate to profile edit page
            self.driver.get(f"https://x.com/{self.username}/profile")

            # Wait for edit profile button
            edit_profile = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, f"//a[@href='/{self.username}/edit']"))
            )
            edit_profile.click()

            # Wait for bio textarea
            bio_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//textarea[@name='description']"))
            )
            bio_field.clear()
            bio_field.send_keys(new_bio)

            # Save changes
            save_button = self.driver.find_element(By.XPATH, "//button[@data-testid='Profile Edit Save']")
            save_button.click()

            print(f"Bio updated: {new_bio}")
            time.sleep(3)
            return True
        except Exception as e:
            print(f"Error updating bio: {e}")
            return False
