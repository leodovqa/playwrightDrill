import pytest

url = "https://www.chat-avenue.com/general"
headless_bool = True


@pytest.fixture(scope='session')
def context1(playwright):
    # Assess - Given
    slowmo_value = 1000
    browser = playwright.chromium.launch(headless=headless_bool, slow_mo=2000)
    context = browser.new_context()
    # # Open new page
    page = context.new_page()
    page.goto(url)
    page.set_default_timeout(300)

    # Ensure the "Log In" button is visible and enabled before clicking
    login_button = page.get_by_role("button", name=" Login")
    login_button.wait_for(state="visible", timeout=slowmo_value)
    login_button.click()

    # Continue with the login process
    try:
        email_field = page.get_by_placeholder("Username/Email")
        email_field.wait_for(state="visible")
        email_field.click()
        email_field.fill("leoqatester@gmail.com")
    except Exception as e:
        print("Email field not found or not visible:", e)
        return

    try:
        password_field = page.get_by_placeholder("Password")
        password_field.wait_for(state="visible")
        password_field.click()
        password_field.fill('leotest2')
    except Exception as e:
        print("Password field not found or not visible:", e)
        return

    try:
        submit_button = page.get_by_role("button", name=" Login")
        submit_button.wait_for(state="visible", timeout=slowmo_value)
        submit_button.click()
    except Exception as e:
        print("Submit button not found or not visible:", e)
        return
    page.wait_for_load_state(timeout=10000)
    # time.sleep(2)

    yield context


@pytest.fixture(scope='session')
def context2(playwright):
    # Assess - Given
    slowmo_value = 1000
    browser = playwright.chromium.launch(headless=headless_bool, slow_mo=2000)
    context = browser.new_context()
    # # Open new page
    page = context.new_page()
    page.goto(url)
    page.set_default_timeout(300)

    # Ensure the "Log In" button is visible and enabled before clicking
    login_button = page.get_by_role("button", name=" Login")
    login_button.wait_for(state="visible", timeout=slowmo_value)
    login_button.click()

    # Continue with the login process
    try:
        email_field = page.get_by_placeholder("Username/Email")
        email_field.wait_for(state="visible")
        email_field.click()
        email_field.fill("dovforjunk@gmail.com")
    except Exception as e:
        print("Email field not found or not visible:", e)
        return

    try:
        password_field = page.get_by_placeholder("Password")
        password_field.wait_for(state="visible")
        password_field.click()
        password_field.fill('leotest1')
    except Exception as e:
        print("Password field not found or not visible:", e)
        return

    try:
        submit_button = page.get_by_role("button", name=" Login")
        submit_button.wait_for(state="visible", timeout=slowmo_value)
        submit_button.click()
    except Exception as e:
        print("Submit button not found or not visible:", e)
        return
    page.wait_for_load_state(timeout=10000)
    # time.sleep(2)

    yield context


@pytest.fixture()
def login_set_up_for_chat(context1, context2, browser):
    page1 = context1.new_page()
    page2 = context2.new_page()
    page1.goto(url)
    page2.goto(url)
    page1.set_default_timeout(5000)
    page2.set_default_timeout(5000)

    yield page1, page2
    page1.close()
    page2.close()
