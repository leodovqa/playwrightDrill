from playwright.sync_api import Page, Locator


class HomePage:
    def __init__(self, page):
        # Define locators using appropriate selectors (e.g., text, CSS, XPath)
        self.celebrating_beauty_header: Locator = page.get_by_text("Celebrating Beauty and Style")
        self.celebrating_beauty_body: Locator = page.get_by_text("playwright-practice was")
        self.shop_shoes: Locator = page.get_by_text("Shoes")
        self.cart_icon: Locator = page.locator("[data-hook='svg-icon-9']")


'''class HomePage:
    celebrating_beauty_header = "Celebrating Beauty and Style"
    celebrating_beauty_body = "playwright-practice was founded by a group of like-minded fashion devotees, dete"
'''
