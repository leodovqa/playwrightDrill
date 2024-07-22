import requests


def send_telegram_message(bot_token, chat_id, title, body):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    message = f"*{title}*\n{body}"  # Format the message with title and body using Markdown
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown'  # Use Markdown to format the title as bold
    }
    response = requests.post(url, json=payload)
    return response


def main():
    bot_token = '7452695873:AAEjbCmm1bR23b_rDu3Mqvpaz0vrF1q-Nqg'
    chat_id = '986947104'

    # Get user input for title and body
    title = input("Enter the title of the message: ")
    print("Enter the body of the message with each point on a new line. Type 'done' to finish:")

    body_lines = []
    while True:
        line = input()
        if line.lower() == 'done':
            break
        body_lines.append(f"- {line}")  # Prepend each line with a bullet point

    body = "\n".join(body_lines)

    send_telegram_message(bot_token, chat_id, title, body)
    '''response = send_telegram_message(bot_token, chat_id, title, body)
    print(response.json())'''


if __name__ == "__main__":
    main()
