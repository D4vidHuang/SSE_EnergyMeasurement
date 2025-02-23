from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service  # For Chrome
from selenium.webdriver.firefox.options import Options
import time

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def browse_reddit_chrome(duration_seconds=50):
    driver = webdriver.Chrome(options = options)  # chromedriver is assumed to be in PATH
    try:
        driver.get("https://www.reddit.com")
        time.sleep(5)

        start_time = time.time()
        while time.time() - start_time < duration_seconds:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)


    finally:
        driver.quit()

def browse_facebook_chrome(duration_seconds=60):
    driver = webdriver.Chrome()  # chromedriver is assumed to be in PATH
    try:
        driver.get("https://www.facebook.com")
        time.sleep(5)

        start_time = time.time()
        while time.time() - start_time < duration_seconds:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            # Add Facebook-specific interaction code here

    finally:
        driver.quit()

if __name__ == "__main__":
    browse_reddit_chrome()
    # browse_facebook_chrome()  # Uncomment to browse Facebook as well