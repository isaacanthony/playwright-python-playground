"""Main entrypoint"""
from datetime import datetime
from io import BytesIO

import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.firefox.launch()
    page = browser.new_page()

    page.goto("https://funhtml5games.com/helicopter/index.html")
    page.wait_for_selector("canvas")
    start = datetime.now()

    for _ in range(10):
        page.click("canvas", delay=100)

        img = np.array(
            Image.open(BytesIO(page.query_selector("canvas").screenshot()))
        )

        print(img)

    end = datetime.now()
    score = (end - start).seconds
    print(score)

    browser.close()
