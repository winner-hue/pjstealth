import time

from playwright.sync_api import sync_playwright
from pjstealth import stealth_sync

p = sync_playwright().start()
proxy = {
    "server": "127.0.0.1:7890"
}
browser = p.chromium.launch(headless=False)

context = browser.new_context(
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    proxy=proxy,
    locale="en-US, en",
    timezone_id="Europe/London",
    screen={"height": 1080, "width": 1920},
    viewport={"height": 1000, "width": 1230})
page = context.new_page()

stealth_sync(page)

page.goto("https://www.ip77.net/")


time.sleep(100000)

