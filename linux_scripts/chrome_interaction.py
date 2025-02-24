from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def browse_reddit_chrome(duration_seconds=60):
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
        
def play_youtube_video(duration_seconds=60):
    driver = webdriver.Firefox()  # Ensure geckodriver is in PATH

    try:
        driver.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        wait = WebDriverWait(driver, 5)
        try:
            #<button class="yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m" aria-disabled="false" aria-label="Accept the use of cookies and other data for the purposes described" title="" style=""><div class="yt-spec-button-shape-next__button-text-content"><span class="yt-core-attributed-string yt-core-attributed-string--white-space-no-wrap" role="text">Accept all</span></div><yt-touch-feedback-shape style="border-radius: inherit;"><div class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response-inverse" aria-hidden="true"><div class="yt-spec-touch-feedback-shape__stroke" style=""></div><div class="yt-spec-touch-feedback-shape__fill" style=""></div></div></yt-touch-feedback-shape></button>
            accept_all_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Accept all')]]")))
            accept_all_button.click()
            time.sleep(5)
        except TimeoutException:
            print("Accept all not found")
        # time.sleep(duration_seconds)
        try:
            play_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ytp-large-play-button')]")))
            play_button.click()
            print("Clicked Play button.")
        except:
            print("Play button not found or already playing.")
        time.sleep(duration_seconds)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    # browse_reddit_chrome()
    # browse_facebook_chrome()  # Uncomment to browse Facebook as well
    play_youtube_video()  # Uncomment to play a YouTube video as well