from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def browse_reddit(duration_seconds=60):
    driver = webdriver.Firefox()  # geckodriver is assumed to be in PATH

    try:
        driver.get("https://www.reddit.com")

        time.sleep(5)  # Initial wait

        start_time = time.time()
        while time.time() - start_time < duration_seconds:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait briefly between scrolls

    finally:
        driver.quit()

def browse_facebook(duration_seconds=60):
    driver = webdriver.Firefox()  # geckodriver is assumed to be in PATH

    try:
        driver.get("https://www.facebook.com")
        time.sleep(5)

        start_time = time.time()
        while time.time() - start_time < duration_seconds:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

    finally:
        driver.quit()


if __name__ == "__main__":
    browse_reddit()
    # browse_facebook()  #facebook option