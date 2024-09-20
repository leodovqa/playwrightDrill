from pom.home_page_elements import HomePage
from playwright.sync_api import expect
import pytest


# from utils.secret_config import PASSWORD


@pytest.mark.integration
def test_about_us_section_verbiage(login_set_up) -> None:
    # Assess - Given
    page = login_set_up
    # Instantiate the HomePage class with the current page
    homepage = HomePage(page)

    # Verify that elements are visible
    expect(homepage.celebrating_beauty_header).to_be_visible()
    expect(homepage.celebrating_beauty_body).to_be_visible()

    # Assert/Expect the text is visible for correct test
    '''expect(page.get_by_text(HomePage.celebrating_beauty_header)).to_be_visible()
    expect(page.get_by_text(HomePage.celebrating_beauty_body)).to_be_visible()'''


@pytest.mark.integration
def test_about_us_section_verbiage_login_setup(login_set_up) -> None:
    # Assess - Given
    page = login_set_up
    homepage = HomePage(page)

    # Verify that elements are visible
    expect(homepage.celebrating_beauty_header).to_be_visible()
    expect(homepage.celebrating_beauty_body).to_be_visible()

    # Assert/Expect the text is visible for correct test
    '''expect(page.get_by_text(HomePage.celebrating_beauty_header)).to_be_visible()
    expect(page.get_by_text(HomePage.celebrating_beauty_body)).to_be_visible()'''


@pytest.mark.xfail(reason="The texts should be visible...")
def test_about_us_section_verbiage_2(login_set_up) -> None:
    # Assess - Given
    page = login_set_up
    homepage = HomePage(page)

    # Verify that elements are visible
    expect(homepage.celebrating_beauty_header).to_be_hidden()
    expect(homepage.celebrating_beauty_body).to_be_hidden()

    # Assert/Expect the text is visible for correct test
    '''expect(page.get_by_text(HomePage.celebrating_beauty_header)).to_be_visible()
    expect(page.get_by_text(HomePage.celebrating_beauty_body)).to_be_visible()'''
