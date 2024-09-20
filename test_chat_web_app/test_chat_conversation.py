from playwright.sync_api import expect


def test_private_chat_message_was_delivered_successfully(login_set_up_for_chat):
    sender_page, receiver_page = login_set_up_for_chat

    try:
        # User 1: Send a message
        sender_page.get_by_title("Friend list").click()
        sender_page.locator("#container_friends div").filter(has_text="leotest1").nth(2).click()
        sender_page.locator("#avcontent").get_by_text("Private").click()
        sender_page.locator("#message_content").click()
        sender_page.locator("#message_content").fill("Testing chat with a friend!")
        sender_page.locator("#private_send").click()

        # User 2: Verify message delivery
        receiver_page.locator("#get_private i").click()
        receiver_page.locator("#private_menu_content").get_by_text("leotest2").click()
        receiver_page.wait_for_load_state("networkidle")

        # Wait for the message to appear using a more specific selector
        message_locator = receiver_page.get_by_text("Testing chat with a friend!")
        receiver_page.wait_for_selector(message_locator, timeout=5000)

        # Verify message visibility
        expect(message_locator).to_be_visible()

    except Exception as e:
        # Handle exceptions and provide informative error messages
        print(f"Test failed: {e}")
        raise


'''def test_private_chat_message_was_delivered_successfully(login_set_up_for_chat):
    page1, page2 = login_set_up_for_chat
    # User 1: Send a message
    page1.get_by_title("Friend list").click()
    page1.locator("#container_friends div").filter(has_text="leotest1").nth(2).click()
    page1.locator("#avcontent").get_by_text("Private").click()
    page1.locator("#message_content").click()
    page1.locator("#message_content").fill("Testing chat with a friend!")
    page1.locator("#private_send").click()

    # User 2: Verify message delivery
    page2.locator("#get_private i").click()
    page2.locator("#private_menu_content").get_by_text("leotest2").click()
    page2.wait_for_load_state("networkidle")

    # Wait for the message to appear in the private chat
    page2.wait_for_timeout(2000)  # Increase the wait time if needed

    # Check if the chat message is visible
    messages = page2.locator("text=Testing chat with a friend!")

    for i in range(messages.count()):
        expect(messages.nth(i)).to_be_visible()

    # Check if the chat message is visible
    # expect(page2.get_by_text("Testing chat with a friend")).to_be_visible()

    # Alternative: More robust way to wait for the specific element
    message_locator = page2.locator("text=Testing chat with a friend!")
    page2.wait_for_selector(message_locator, timeout=5000)  # Adjust timeout as needed
    expect(message_locator).to_be_visible()'''
