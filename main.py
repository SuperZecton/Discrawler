import requests
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

URL = "https://disboard.org"


def is_ready(browser):
    return browser.execute_script(r"""
        return document.readyState === 'complete'
    """)


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    browser = webdriver.Chrome(options=options)
    browser.get(URL)
    WebDriverWait(browser, 30).until(is_ready)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    WebDriverWait(browser, 30).until(is_ready)
    elements = browser.find_elements(By.CLASS_NAME, "server-name")
    for elem in elements:
        print(elem.text)
    print("Exiting code")
    browser.close()
