from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if __name__ == "__main__":
    driver = webdriver.Chrome() 

    try:
        driver.get("https://luic.github.io/WebGL-Performance-Benchmark/benchmark/cubes.html")
        print("Webpage opened. Waiting for 1 minute...")
        time.sleep(60)

    finally:
        driver.quit()
        print("Browser closed.")