import pytest


@pytest.mark.smoke
@pytest.mark.skip
@pytest.mark.regression
def test_login(set_up) -> None:
    page = set_up


@pytest.mark.smoke
@pytest.mark.regression
def test_logged_user_can_view_my_orders_menu(test_user_can_login) -> None:
    # Assess - Given
    page = test_user_can_login

    # Act - When/And
    page.click("[aria-label='symon.storozhenko account menu']")

    # Assert - Then
    assert page.is_visible("text=My Orders")


