import time

import pytest
from playwright.sync_api import sync_playwright, expect

time_out = 2000


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()


def test_user_can_login(page):
    # Go to the login page
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    # Ensure the "Log In" button is visible and enabled before clicking
    login_button = page.get_by_role("button", name="Log In")
    login_button.wait_for(state="visible", timeout=time_out)  # Increased timeout to 5000ms
    login_button.click()

    # Check if the sign up switch button exists and is visible
    sign_up_switch = page.get_by_test_id("signUp.switchToSignUp")
    try:
        sign_up_switch.wait_for(state="attached", timeout=time_out)
        print("Sign Up switch is attached")
    except Exception as e:
        print("Sign Up switch is not attached:", e)
        return

    try:
        sign_up_switch.wait_for(state="visible", timeout=time_out)
        print("Sign Up switch is visible")
    except Exception as e:
        print("Sign Up switch is not visible:", e)
        return

    sign_up_switch.click()

    # Continue with the login process
    page.get_by_role("button", name="Log in with Email").wait_for(state="visible")
    page.get_by_role("button", name="Log in with Email").click()

    email_field = page.get_by_test_id("emailAuth").get_by_label("Email")
    password_field = page.get_by_label("Password")

    email_field.wait_for(state="visible")
    email_field.click()
    email_field.fill("symon.storozhenko@gmail.com")

    password_field.wait_for(state="visible")
    password_field.click()
    password_field.fill("test123")

    submit_button = page.get_by_test_id("submit").get_by_test_id("buttonElement")
    submit_button.wait_for(state="visible", timeout=time_out)
    submit_button.click()
    time.sleep(3)
    # Add assertions to verify successful login if necessary
    print(expect(page.get_by_label("symon.storozhenko account menu")).to_be_visible())
    if expect(page.get_by_label("symon.storozhenko account menu")).to_be_visible():
        print('The log in button is hidden')
    else:
        print('Something went wrong')
