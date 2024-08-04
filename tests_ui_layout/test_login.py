import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_login(set_up) -> None:
    page = set_up


@pytest.mark.smoke
@pytest.mark.regression
def test_logged_user_can_view_my_orders_menu(set_up) -> None:
    # Assess - Given
    page = set_up

    # Act - When/And
    page.click("[aria-label='symon.storozhenko account menu']")

    # Assert - Then
    assert page.is_visible("text=My Orders")


