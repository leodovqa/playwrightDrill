import requests


def get_chat_id(bot_token):
    # Construct the URL to get updates
    url = f'https://api.telegram.org/bot{bot_token}/getUpdates'

    # Send the request and get the response as JSON
    response = requests.get(url)
    data = response.json()

    # Parse the JSON response to get the chat ID
    chat_id = data['result'][0]['message']['chat']['id']

    return chat_id


def main():
    bot_token = '7452695873:AAEjbCmm1bR23b_rDu3Mqvpaz0vrF1q-Nqg'  # Replace with your bot token
    chat_id = get_chat_id(bot_token)
    print(f"Your chat ID is: {chat_id}")


if __name__ == "__main__":
    main()
