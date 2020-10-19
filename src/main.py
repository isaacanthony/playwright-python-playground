from playwright import sync_playwright

with sync_playwright() as p:
    browser_type = p.firefox
    browser = browser_type.launch()
    page = browser.newPage()
    page.goto("http://whatsmyuseragent.org")
    page.screenshot(path=f"/img/example-{browser_type.name}.png")
    browser.close()
