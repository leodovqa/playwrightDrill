from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    # Add slow_mo=xxx (After the headless=False argument) only when debugging/fixing/testing/etc...
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.pause()


with sync_playwright() as playwright:
    run(playwright)
