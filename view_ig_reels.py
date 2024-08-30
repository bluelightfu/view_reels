from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
import threading

class ViewIGReels(threading.Thread):
    def __init__(self, url): 
        threading.Thread.__init__(self) 
        self.url = url 
        self.browser = None
        self.stop_flag = False
  
    def run(self): 
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--incognito")
        # chrome_options.add_argument("--headless")  # Optional : run in the background
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("disable-popup-blocking")
        with open('cookies_ig.json') as f:
            cookies = json.load(f)
        self.browser = webdriver.Chrome(options=chrome_options)
        self.browser.get('https://www.instagram.com/')

        for cookie in cookies:
            self.browser.add_cookie(cookie)
        self.browser.refresh()
        self.browser.get(target_ig_reels_url)
        while not self.stop_flag:
            time.sleep(90)
            if self.stop_flag:
                print("[INFO] 收到關閉指令!")
                break
            self.browser.refresh()
        self.browser.quit()
    def stop(self):
        self.stop_flag = True

if __name__ == "__main__":
    number_of_windows = 2
    target_ig_reels_url = "https://www.instagram.com/reel/XXXX" # target url

    threads = []
    urls = [target_ig_reels_url for _ in range(number_of_windows)]
    for url in urls: 
        t = ViewIGReels(url) 
        t.start()
        threads.append(t)
        
    input("[INFO] 輸入按任何鍵結束工作")
    print("[INFO] 請耐心等候，視窗將會關閉")
    for t in threads:
        t.stop()

        