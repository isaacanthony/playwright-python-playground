"""Main entrypoint"""
from datetime import datetime
from io import BytesIO

import numpy as np
from PIL import Image
from playwright import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.firefox.launch()
    page = browser.newPage()

    page.goto("https://funhtml5games.com/helicopter/index.html")
    page.waitForSelector("canvas")
    start = datetime.now()

    for _ in range(10):
        page.click("canvas", delay=100)

        img = np.array(
            Image.open(BytesIO(page.querySelector("canvas").screenshot()))
        )

        print(img)

    end = datetime.now()
    score = (end - start).seconds
    print(score)

    browser.close()
