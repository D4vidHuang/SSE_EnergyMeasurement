from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"""
This script demonstrates how to use Selenium to automate chrome to mimic user behavior.
1. Browse Reddit for 1 minute.
2. Browse Facebook for 1 minute. （dispatched right now because you have to be logged in)
3. Play a YouTube video for 1 minute.
"""
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-usb"]) # Disable USB devices
def browse_reddit_chrome(duration_seconds=50):
    driver = webdriver.Chrome()  # chromedriver is assumed to be in PATH
    try:
        driver.get("https://www.reddit.com")
        time.sleep(5)

        start_time = time.time()
        while time.time() - start_time < duration_seconds:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
    finally:
        driver.quit()

# def browse_facebook_chrome(duration_seconds=60):
#     driver = webdriver.Chrome()  # chromedriver is assumed to be in PATH
#     try:
#         driver.get("https://www.facebook.com")
#         time.sleep(5)
#
#         start_time = time.time()
#         while time.time() - start_time < duration_seconds:
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             time.sleep(2)
#     finally:
#         driver.quit()


def play_youtube_chrome(duration_seconds=40):
    driver = webdriver.Chrome()  # Ensure geckodriver is in PATH
    try:
        driver.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        wait = WebDriverWait(driver, 5)
        try:
            accept_all_button = wait.until(
                # EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Accept all')]]")))
                EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), '全部接受')]]")))
            accept_all_button.click()
            time.sleep(5)
        except TimeoutException:
            print("Accept all not found")
        # time.sleep(duration_seconds)
        try:
            play_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ytp-large-play-button')]")))
            play_button.click()
            print("Clicked Play button.")
        except:
            print("Play button not found or already playing.")
        time.sleep(duration_seconds)

    finally:
        driver.quit()


if __name__ == "__main__":
    # browse_reddit_chrome()
    play_youtube_chrome()

