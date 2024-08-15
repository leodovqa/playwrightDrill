from playwright.sync_api import Page, expect
from pom.home_page_elements import HomePage


def test_visual_landing(page, assert_snapshot) -> None:
    # Navigate to the page
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    # Instantiate the HomePage class with the current page
    homepage = HomePage(page)

    # Verify that elements are visible
    expect(homepage.celebrating_beauty_header).to_be_visible()

    # Take a screenshot and compare with baseline
    assert_snapshot(page.screenshot(), name="test_visual_landing.png")


# This test contains mask screenshot for a list of locators,
# the screenshot in a full page mode and the name for the screenshot set in the name
def test_visual_landing_shop(page, assert_snapshot) -> None:
    # Navigate to the page
    page.goto("https://symonstorozhenko.wixsite.com/website-1/shop")

    # Instantiate the HomePage class with the current page
    homepage = HomePage(page)

    # Verify that elements are visible
    expect(homepage.shop_shoes).to_be_visible()

    # Take a screenshot and compare with baseline
    assert_snapshot(page.screenshot(full_page=True, mask=[homepage.cart_icon]), name="test_visual_landing_shop.png")
