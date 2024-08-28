from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json

def view_ig_reels(num_windows:int, target_ig_reels_url:str, *args, **kwargs):
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--headless")  # Optional : run in the background
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("disable-popup-blocking")
    browsers = []

    for _ in range(num_windows):
        # cookie免帳號登入
        with open('cookies_ig.json') as f:
            cookies = json.load(f)
        browser = webdriver.Chrome(options=chrome_options)
        browser.get('https://www.instagram.com/')

        for cookie in cookies:
            browser.add_cookie(cookie)
        browser.refresh()
        browser.get(target_ig_reels_url)

        browsers.append(browser)

    return browsers

if __name__ == "__main__":
    number_of_windows = 5
    target_ig_reels_url = "https://www.instagram.com/reel/C8YgP_wB9Wn/"
    browsers = view_ig_reels(number_of_windows, target_ig_reels_url)

    try:
        while True:
            time.sleep(90)  # 每 90 秒重整
            for browser in browsers:
                browser.refresh()  # 重整
    except KeyboardInterrupt:
        for browser in browsers:
            browser.quit()  #完整關閉需要時間，請耐心等候