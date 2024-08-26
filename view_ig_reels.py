from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json

def view_ig_reels(num_windows:int, target_ig_reels_url:str, *args, **kwargs):
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    browsers = []

    for _ in range(num_windows):
        # cookie免帳號登入
        with open('cookies_ig.json') as f:
            cookies = json.load(f)
        browser = webdriver.Chrome(chrome_options)
        browser.get('https://www.instagram.com/')

        for cookie in cookies:
            browser.add_cookie(cookie)
        browser.refresh()
        browser.get(target_ig_reels_url)

        browsers.append(browser)

    return browsers

if __name__ == "__main__":
    number_of_windows = 5
    target_ig_reels_url = "https://www.instagram.com/reel/XXXXXX"
    browsers = view_ig_reels(number_of_windows, target_ig_reels_url)
    input("按下任何按鍵關閉所有視窗")  


    for browser in browsers:
        browser.quit()  #完整關閉需要時間，請耐心等候