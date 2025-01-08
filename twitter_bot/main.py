# main.py
import schedule
import time
from modules.driver_manager import DriverManager
from modules.login_handler import LoginHandler
from modules.tweet_manager import TweetManager
from modules.profile_manager import ProfileManager
from config import Config

def run_daily_tasks(driver, username):
    """
    Execute daily Twitter/X automation tasks

    Args:
        driver: Selenium WebDriver instance
        username (str): Twitter/X username
    """
    try:
        # Refresh driver to prevent timeout
        driver.refresh()

        # Initialize task managers
        tweet_manager = TweetManager(driver)
        profile_manager = ProfileManager(driver, username)

        # Execute daily tasks
        tweet_manager.post_tweet()
        profile_manager.update_bio()
    except Exception as e:
        print(f"Daily task error: {e}")

def main():
    # Initialize driver manager
    driver_manager = DriverManager()

    try:
        # Setup WebDriver
        driver = driver_manager.setup_safari_driver()
        if not driver:
            print("Failed to initialize WebDriver")
            return

        # Login handler
        login_handler = LoginHandler(driver)
        login_success = login_handler.login(Config.USERNAME, Config.PASSWORD)

        if not login_success:
            print("Login failed. Exiting...")
            driver_manager.quit_driver(driver)
            return

        # Schedule daily tasks
        schedule.every().day.at(Config.TWEET_TIME).do(
            run_daily_tasks, driver, Config.USERNAME
        )
        schedule.every().day.at(Config.BIO_UPDATE_TIME).do(
            run_daily_tasks, driver, Config.USERNAME
        )

        # Keep script running
        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            print("Automation stopped by user")

    except Exception as e:
        print(f"Unexpected error: {e}")

    finally:
        # Ensure driver is closed
        driver_manager.quit_driver(driver)

if __name__ == "__main__":
    main()
