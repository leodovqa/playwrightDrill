import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    # Add slow_mo=xxx (After the headless=False argument) only when debugging/fixing/testing/etc...
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://jsonplaceholder.typicode.com/")
    # Wait for the network to fully load page
    page.wait_for_load_state("networkidle")
    page.get_by_role("link", name="Blog").click()
    page.get_by_role("link", name="Posts").click()
    page.get_by_role("link", name="Husky 5").click()
    page.locator("img").click()
    # .nth(0) - means the first element, like [0] = index=0... nth(1) = index=1 [1], etc...
    expect(page.get_by_role("link", name="https://github.com/typicode/").nth(0)).to_be_visible()
    print("Done...")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
