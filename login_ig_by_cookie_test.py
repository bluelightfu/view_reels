from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import json

if __name__ == '__main__':
    options = Options()
    options.add_experimental_option("detach", True)
    with open('cookies_ig.json') as f:
        cookies = json.load(f)
    driver = webdriver.Chrome(options)
    driver.get('https://www.instagram.com/')

    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    driver.get("https://www.instagram.com/reel/XXXX")
