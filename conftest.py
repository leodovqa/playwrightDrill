import os
import time
import pytest

PASSWORD = os.environ['PASSWORD']

headless_bool = True
slowmo_value = 3500

'''try:
    PASSWORD = os.environ['PASSWORD']
except KeyError:
    import utils.secret_config
    PASSWORD = utils.secret_config.PASSWORD
    headless_bool = False
    slowmo_value = 300'''


@pytest.fixture()
def set_up(page):
    # Assess - Given
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # # Open new page
    # page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    yield page
    page.close()


@pytest.fixture(scope='session')
def context_creation(playwright):
    # Assess - Given
    browser = playwright.chromium.launch(headless=headless_bool, slow_mo=slowmo_value)
    context = browser.new_context()
    # # Open new page
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    login_issue = True
    while login_issue:
        if not page.is_visible("[data-testid=\"signUp.switchToSignUp\"]"):
            page.click("button:has-text(\"Log In\")")
        else:
            login_issue = False
        time.sleep(0.1)
    # Click [data-testid="signUp.switchToSignUp"]
    page.click("[data-testid=\"signUp.switchToSignUp\"]", timeout=2000)
    # page.click(":nth-match(:text('Log In'), 2)", timeout=2000)
    page.click("[data-testid='switchToEmailLink'] >> [data-testid='buttonElement']")
    # page.click("[data-testid='siteMembers.container'] input[type='email']")
    # page.fill("[data-testid='siteMembers.container'] input[type='email']", "symon.storozhenko@gmail.com")
    page.fill('input:below(:text("Email"))', "symon.storozhenko@gmail.com")
    page.press("[data-testid='siteMembers.container'] >> input[type='email']", "Tab")
    # remove the # sign in the next row when PASSWORD will be available in the 8~14 rows.
    # page.fill("input[type='password']", PASSWORD)
    page.click("[data-testid='submit'] >> [data-testid='buttonElement']")

    # Save storage state into the file.
    storage = context.storage_state(path="state.json")

    # Create a new context with the saved storage state.

    yield context
    # time.sleep(5)


@pytest.fixture(scope='session')
def test_user_can_login(playwright):
    # Assess - Given
    headless_bool = True
    slowmo_value = 2000
    browser = playwright.chromium.launch(headless=headless_bool, slow_mo=2000)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(300)

    # Ensure the "Log In" button is visible and enabled before clicking
    login_button = page.get_by_role("button", name="Log In")
    login_button.wait_for(state="visible", timeout=3000)  # Increased timeout to 3000ms
    login_button.click()

    # Debugging - Check if the sign up switch button exists and is visible
    sign_up_switch = page.get_by_test_id("signUp.switchToSignUp")
    try:
        sign_up_switch.wait_for(state="attached", timeout=slowmo_value)
        print("Sign Up switch is attached")
    except Exception as e:
        print("Sign Up switch is not attached:", e)
        return

    try:
        sign_up_switch.wait_for(state="visible", timeout=slowmo_value)
        print("Sign Up switch is visible")
    except Exception as e:
        print("Sign Up switch is not visible:", e)
        return

    sign_up_switch.click()

    # Continue with the login process
    try:
        email_button = page.get_by_role("button", name="Log in with Email")
        email_button.wait_for(state="visible", timeout=slowmo_value)
        email_button.click()
    except Exception as e:
        print("Log in with Email button not found or not visible:", e)
        return

    try:
        email_field = page.get_by_test_id("emailAuth").get_by_label("Email")
        email_field.wait_for(state="visible")
        email_field.click()
        email_field.fill("symon.storozhenko@gmail.com")
    except Exception as e:
        print("Email field not found or not visible:", e)
        return

    try:
        password_field = page.get_by_label("Password")
        password_field.wait_for(state="visible")
        password_field.click()
        password_field.fill(PASSWORD)
    except Exception as e:
        print("Password field not found or not visible:", e)
        return

    try:
        submit_button = page.get_by_test_id("submit").get_by_test_id("buttonElement")
        submit_button.wait_for(state="visible", timeout=slowmo_value)
        submit_button.click()
    except Exception as e:
        print("Submit button not found or not visible:", e)
        return

    yield page


@pytest.fixture()
def login_set_up(context_creation, browser):
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    yield page
    page.close()


@pytest.fixture
def go_to_new_collection_page(page):
    # Assess - Given
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # # Open new page
    # page = context.new_page()
    page.goto("/new-collection")
    page.set_default_timeout(3000)

    yield page
