from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def browse_reddit_firefox(duration_seconds=45):
    driver = webdriver.Firefox()

    try:
        driver.get("https://www.reddit.com")
        time.sleep(5)

        start_time = time.time()
        while time.time() - start_time < duration_seconds:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
    finally:
        driver.quit()

def play_youtube_firefox(duration_seconds=40):
    driver = webdriver.Firefox()

    try:
        driver.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        wait = WebDriverWait(driver, 5)
        try:
            accept_all_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Accept all')]]"))
            )
            accept_all_button.click()
            time.sleep(5)
        except TimeoutException:
            print("Accept all not found")

        try:
            play_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ytp-large-play-button')]"))
            )
            play_button.click()
            print("Clicked Play button.")
        except:
            print("Play button not found or already playing.")

        time.sleep(duration_seconds)

    finally:
        driver.quit()


if __name__ == "__main__":
    # browse_reddit_firefox()
    play_youtube_firefox()
