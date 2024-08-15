from playwright.sync_api import Playwright, sync_playwright, expect

headless_bool = True
# url = 'https://www.chat-avenue.com/general'
url = 'https://symonstorozhenko.wixsite.com/website-1'


def run(playwright: Playwright) -> None:
    # Add slow_mo=xxx (After the headless=False argument) only when debugging/fixing/testing/etc...
    browser = playwright.chromium.launch(headless=headless_bool)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    page.pause()


with sync_playwright() as playwright:
    run(playwright)
