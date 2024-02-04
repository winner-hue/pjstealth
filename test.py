# import asyncio
# import time
#
# from playwright.sync_api import sync_playwright
# # from pjstealth import stealth_sync, stealth_async
# # from playwright.async_api import async_playwright
# from playwright_stealth import stealth_sync
#
# p = sync_playwright().start()
# proxy = {
#     "server": "127.0.0.1:7890"
# }
# browser = p.chromium.launch(headless=False,
#                             args=['--no-sandbox', '--no-default-browser-check',
#                                   '--disable-suggestions-ui', '--no-first-run', '--disable-infobars',
#                                   '--disable-popup-blocking', '--disable-popup-blocking'])
#
# context = browser.new_context(
#     user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5005.61 Safari/537.36',
#     # proxy=proxy,
#     # locale="zh-CN",
#     # timezone_id="Asia/Shanghai",
#     # screen={"height": 1080, "width": 1920},z
#     # viewport={"height": 1000, "width": 1230})
# )
# page = context.new_page()
#
# stealth_sync(page)
#
# page.goto("https://shopee.co.id/", timeout=800000)
#
# time.sleep(100000)
import os
# import time
#
# import undetected_chromedriver as uc
#
# chrome = uc.Chrome()
# chrome.get("https://shopee.co.id/")
# time.sleep(1000000)
#

