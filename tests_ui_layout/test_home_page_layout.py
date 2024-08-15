from pom.home_page_elements import HomePage
from playwright.sync_api import expect
import pytest


# from utils.secret_config import PASSWORD


@pytest.mark.integration
def test_about_us_section_verbiage(login_set_up) -> None:
    # Assess - Given
    page = login_set_up

    # Assert/Expect the text is visible for correct test
    expect(page.get_by_text(HomePage.celebrating_beauty_header)).to_be_visible()
    expect(page.get_by_text(HomePage.celebrating_beauty_body)).to_be_visible()


@pytest.mark.integration
def test_about_us_section_verbiage_login_setup(login_set_up) -> None:
    # Assess - Given
    page = login_set_up

    # Assert/Expect the text is visible for correct test
    expect(page.get_by_text(HomePage.celebrating_beauty_header)).to_be_visible()
    expect(page.get_by_text(HomePage.celebrating_beauty_body)).to_be_visible()


@pytest.mark.xfail(reason="The texts should be visible...")
def test_about_us_section_verbiage_2(login_set_up) -> None:
    # Assess - Given
    page = login_set_up

    # Assert/Expect the text is hidden for xfail test
    expect(page.get_by_text(HomePage.celebrating_beauty_header)).to_be_hidden()
    expect(page.get_by_text(HomePage.celebrating_beauty_body)).to_be_hidden()
