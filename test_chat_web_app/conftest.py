import pytest

url = "https://www.chat-avenue.com/general"
headless_bool = False


@pytest.fixture(scope='session')
def context1(playwright):
    slowmo_value = 1000
    browser = playwright.chromium.launch(headless=headless_bool, slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    page.set_default_timeout(10000)

    try:
        login_button = page.locator("xpath=/html/body/div[1]/div[1]/div/div/div[3]/button[1]")
        print("Login button found:", login_button)
        login_button.click()
    except Exception as e:
        print("Failed to locate or click the login button:", e)
        return

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
        # Using XPath for the submit button
        # submit_button = page.locator("//*[@id='login_form_box']/div[3]/button")
        submit_button = page.locator("xpath=/html/body/div[3]/div/div[2]/div/div[3]/button")

        submit_button.wait_for(state="visible", timeout=slowmo_value)
        submit_button.click()
    except Exception as e:
        print("Submit button not found or not visible:", e)
        return

    page.wait_for_load_state(timeout=10000)
    yield context


@pytest.fixture(scope='session')
def context2(playwright):
    slowmo_value = 1000
    browser = playwright.chromium.launch(headless=headless_bool, slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    page.set_default_timeout(10000)

    try:
        login_button = page.locator("xpath=/html/body/div[1]/div[1]/div/div/div[3]/button[1]")
        login_button.wait_for(state="visible", timeout=slowmo_value)
        login_button.click()
    except Exception as e:
        print("Failed to locate or click the login button:", e)
        return

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
        # Using XPath for the submit button
        # submit_button = page.locator("//*[@id='login_form_box']/div[3]/button")
        submit_button = page.locator("xpath=/html/body/div[3]/div/div[2]/div/div[3]/button")

        submit_button.wait_for(state="visible", timeout=slowmo_value)
        submit_button.click()
    except Exception as e:
        print("Submit button not found or not visible:", e)
        return

    page.wait_for_load_state(timeout=10000)
    yield context


@pytest.fixture()
def login_set_up_for_chat(context1, context2):
    page1 = context1.new_page()
    page2 = context2.new_page()
    page1.goto(url)
    page2.goto(url)
    page1.set_default_timeout(5000)
    page2.set_default_timeout(5000)

    yield page1, page2
    page1.close()
    page2.close()
