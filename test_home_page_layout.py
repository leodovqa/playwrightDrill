from playwright.sync_api import Playwright, sync_playwright, expect
from pom.shop_women_elements import ShopWomen
import pytest


def test_about_us_section_verbiage(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=5000)
    page = browser.new_page()
    page.goto('https://symonstorozhenko.wixsite.com/website-1')
    shop_women = ShopWomen(page)

    expect(shop_women.celebrating_beauty_header).to_be_visible()
    expect(shop_women.celebrating_beauty_body).to_be_visible()

    page.close()
    browser.close()


@pytest.mark.xfail(reason='url not ready')
def test_about_us_section_verbiage_2(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=5000)
    page = browser.new_page()
    page.goto('https://symonstorozhenko.wixsite.com/website-1fail')
    shop_women = ShopWomen(page)

    expect(page.is_visible(shop_women.celebrating_beauty_header))
    expect(page.is_visible(shop_women.celebrating_beauty_body))

    page.close()
    browser.close()
