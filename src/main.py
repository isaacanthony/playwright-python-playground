from datetime import datetime
from playwright import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.firefox.launch()
    page = browser.newPage()

    page.goto("https://funhtml5games.com/helicopter/index.html")
    page.waitForSelector("canvas")

    start = datetime.now()
    page.click("canvas", delay=1000)
    end = datetime.now()
    score = (end - start).seconds

    page.querySelector("canvas").screenshot(path="/img/helicopter.png")
    browser.close()
