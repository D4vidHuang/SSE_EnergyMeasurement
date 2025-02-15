from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.binary_location = "/Applications/Firefox.app/Contents/MacOS/firefox"

if __name__ == "__main__":
    driver = webdriver.Firefox(options=options)

    try:
        driver.get("https://dacris.github.io/jsmark/WebGLDemo.html")
        print("Webpage opened. Waiting for 1 minute...")
        time.sleep(60)

    finally:
        driver.quit()
        print("Browser closed.")
