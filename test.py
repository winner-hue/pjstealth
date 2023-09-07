import time

from playwright.sync_api import sync_playwright
from pjstealth import stealth_sync

p = sync_playwright().start()
proxy = {
    "server": "127.0.0.1:7890"
}
browser = p.chromium.launch(headless=False)

page = browser.new_page(
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    proxy=proxy,
    locale="en-US, en",
    timezone_id="Europe/London")
stealth_sync(page)

page.goto("https://web.uutool.cn/")
time.sleep(10000)
