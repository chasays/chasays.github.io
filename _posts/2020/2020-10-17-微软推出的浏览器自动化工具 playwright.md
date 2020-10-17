---
layout: post
title: "微软推出的浏览器自动化工具 playwright"
subtitle: '特点是浏览器的控制脚本用 Python 来写'
author: "叉叉敌"
header-style: text
tags:
  - 浏览器
  - playwright
  - 工具
---

[github](https://github.com/microsoft/playwright-python)
[playwright Guide](https://playwright.dev/)


##  API
提供同步（阻塞）API 和异步 API。它们在功能方面是相同的，并且仅在使用 API 的方式上有所不同。

```python
from playwright import sync_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch()
        page = browser.newPage()
        page.goto('http://whatsmyuseragent.org/')
        page.screenshot(path=f'example-{browser_type.name}.png')
        browser.close()
```

async
```python

import asyncio
from playwright import async_playwright

async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch()
            page = await browser.newPage()
            await page.goto('http://whatsmyuseragent.org/')
            await page.screenshot(path=f'example-{browser_type.name}.png')
            await browser.close()

asyncio.get_event_loop().run_until_complete(main())
```


## 自带pytest

```python
def test_playwright_is_visible_on_google(page):
    page.goto("https://www.google.com")
    page.type("input[name=q]", "Playwright GitHub")
    page.click("input[type=submit]")
    page.waitForSelector("text=microsoft/Playwright")
```


## 

>https://playwright.dev/#version=v1.5.1&path=docs%2Fdebug.md&q=visual-studio-code-debugger