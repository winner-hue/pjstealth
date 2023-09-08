# pjstealth

支持浏览器特征抹除，及浏览器指纹随机化；当前仅支持playwright自动化工具，后续会考虑增加selenium接口

# install

```python
pip install pjstealth
```

# usage

```python
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
    proxy=proxy)
stealth_sync(page)

page.goto("https://web.uutool.cn/")
time.sleep(10000)

```

# 效果

自行体验😁

# 微信赞赏

![image-20230908133417504](https://github.com/winner-hue/pjstealth/blob/main/image-20230908133417504.png)