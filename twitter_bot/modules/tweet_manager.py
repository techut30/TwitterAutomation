from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

class TweetManager:
    def __init__(self, driver):
        """
        Initialize TweetManager with WebDriver

        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver

    def post_tweet(self, tweet_text=None):
        """
        Post a tweet on Twitter/X

        Args:
            tweet_text (str, optional): Text to tweet.
                                        If None, generates a default daily update.

        Returns:
            bool: True if tweet posted successfully, False otherwise
        """
        try:
            # Generate default tweet if no text provided
            if tweet_text is None:
                tweet_text = f"Daily update on {datetime.now().strftime('%Y-%m-%d')}"

            # Navigate to tweet compose area
            tweet_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
            )
            tweet_input.clear()
            tweet_input.send_keys(tweet_text)

            # Find and click post button
            post_button = self.driver.find_element(By.XPATH, "//button[@data-testid='tweetButtonInline']")
            post_button.click()

            print(f"Tweet posted: {tweet_text}")
            time.sleep(3)
            return True
        except Exception as e:
            print(f"Error posting tweet: {e}")
            return False
