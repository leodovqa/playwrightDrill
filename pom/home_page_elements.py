from playwright.sync_api import Page, Locator


class HomePage:
    def __init__(self, page):
        # Define locators using appropriate selectors (e.g., text, CSS, XPath)
        self.celebrating_beauty_header: Locator = page.locator("text='Celebrating Beauty and Style'")
        self.celebrating_beauty_body: Locator = page.locator(
            "text='playwright-practice was founded by a group of like-minded fashion devotees, dete'")
        self.shop_shoes: Locator = page.locator("text='Shoes'")
        self.cart_icon: Locator = page.locator("[data-hook='svg-icon-9']")


'''class HomePage:
    celebrating_beauty_header = "Celebrating Beauty and Style"
    celebrating_beauty_body = "playwright-practice was founded by a group of like-minded fashion devotees, dete"
'''
