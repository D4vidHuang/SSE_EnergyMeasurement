from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def play_youtube_video(duration_seconds=45):
    driver = webdriver.Chrome(options = options)  # Ensure geckodriver is in PATH

    try:
        driver.get("https://www.youtube.com/shorts/Mjr-kj46q7I")
        wait = WebDriverWait(driver, 5)
        try:
            accept_all_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='VfPpkd-vQzf8d' and contains(text(), 'Accept all')]")))
            accept_all_button.click()
            time.sleep(5)
        except TimeoutException:
            print("Accept all not found")
        time.sleep(duration_seconds)

    finally:
        driver.quit()

if __name__ == "__main__":
    play_youtube_video()