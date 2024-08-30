from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
import threading

class ViewIGReels(threading.Thread):
    def __init__(self, url, time_period=60): 
        threading.Thread.__init__(self) 
        self.url = url 
        self.browser = None
        self.stop_flag = False
        self.time_period = time_period
  
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
            time.sleep(self.time_period)
            if self.stop_flag:
                print("[INFO] 收到關閉指令!")
                break
            self.browser.refresh()

        self.browser.quit()
        print("[INFO] 視窗已關閉")
    def stop(self):
        self.stop_flag = True

if __name__ == "__main__":
    number_of_windows = 4 # windows count 視窗數
    target_ig_reels_url = "https://www.instagram.com/reel/XXX/" # target url
    refresh_period_time = 60 # refresh period time 頁面重整週期(sec)

    threads = []
    urls = [target_ig_reels_url for _ in range(number_of_windows)]

    for url in urls: 
        t = ViewIGReels(url, time_period=refresh_period_time)
        t.start() # run()
        threads.append(t)
        
    input("\n\n\n[INFO] 輸入按任何鍵結束工作")
    print("[INFO] 請耐心等候，當視窗跑完該時間週期，視窗將會自動關閉!")
    for t in threads:
        t.stop()

        