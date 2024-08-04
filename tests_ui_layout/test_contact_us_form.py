import time
from playwright.sync_api import Playwright, sync_playwright, expect

# from pom.contact_us_page import ContactUsPage
if __package__ is None:
    import sys
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from pom.contact_us_page import ContactUsPage
else:
    from pom.contact_us_page import ContactUsPage


def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    contact_us = ContactUsPage(page)
    contact_us.navigate()
    contact_us.submit_form("leo", "123 Main", "leotest@gmail.com", "123-345-5678", "test subject", "test message")


with sync_playwright() as playwright:
    test_submit_form(playwright)
    time.sleep(10)
