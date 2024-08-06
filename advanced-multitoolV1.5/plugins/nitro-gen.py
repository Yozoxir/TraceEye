import random
import string
import json
import requests
import threading
from pystyle import Colorate, Colors

username_webhook = "Nitro Checker"
avatar_webhook = "https://static.wikia.nocookie.net/discord/images/b/b8/Nitro_badge.png/revision/latest?cb=20200615092656"
color_webhook = Colors.blue  

def ErrorModule(e):
    print(f"{Colorate.Horizontal(Colors.blue_to_cyan, '[ERROR]')} {e}")

def Title(title):
    print(f"{Colorate.Horizontal(Colors.blue_to_cyan, title)}")

def CheckWebhook(webhook_url):
    pass

def ErrorNumber():
    print(f"{Colorate.Horizontal(Colors.blue_to_cyan, '[ERROR]')} Nombre de thread invalide.")

def send_webhook(embed_content, webhook_url):
    payload = {
        'embeds': [embed_content],
        'username': username_webhook,
        'avatar_url': avatar_webhook
    }

    headers = {
        'Content-Type': 'application/json'
    }

    requests.post(webhook_url, data=json.dumps(payload), headers=headers)

def generate_nitro_code():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return code

def nitro_check(webhook_enabled, webhook_url):
    code_nitro = generate_nitro_code()
    url_nitro = f'https://discord.gift/{code_nitro}'
    try:
        response = requests.get(f'https://discordapp.com/api/v9/entitlements/gift-codes/{code_nitro}?with_application=false&with_subscription_plan=true', timeout=1)
        if response.status_code == 200:
            if webhook_enabled:
                embed_content = {
                    'title': f'Nitro Valid !',
                    'description': f"**__Nitro:__**\n```{url_nitro}```",
                    'color': color_webhook,
                    'footer': {
                        "text": username_webhook,
                        "icon_url": avatar_webhook,
                    }
                }
                send_webhook(embed_content, webhook_url)
                print(Colorate.Horizontal(Colors.green_to_blue, f"'GEN_VALID') Status:  Valid | Nitro: {url_nitro}"))
            else:
                print(Colorate.Horizontal(Colors.green_to_blue, f"'GEN_VALID') Status:  Valid  | Nitro: {url_nitro}"))
        else:
            print(Colorate.Horizontal(Colors.red_to_black, f"'GEN_INVALID') Status: Invalid | Nitro: {url_nitro}"))
    except requests.exceptions.RequestException as e:
        print(Colorate.Horizontal(Colors.blue_to_cyan, f" 'GEN_ERROR') Status: {Colors.red}Error - {e}"))

def request(threads_number, webhook_enabled, webhook_url):
    threads = []
    try:
        for _ in range(threads_number):
            t = threading.Thread(target=nitro_check, args=(webhook_enabled, webhook_url))
            t.start()
            threads.append(t)
    except ValueError:
        ErrorNumber()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    try:
        Title("Discord Nitro Generator")

        webhook_enabled = False
        webhook_input = input(f"{Colorate.Horizontal(Colors.blue_to_cyan, 'Webhook notification ? (y/n) -> ')}").strip().lower()
        if webhook_input in ['y', 'yes']:
            webhook_enabled = True
            webhook_url = input(f"{Colorate.Horizontal(Colors.blue_to_cyan, 'Entré l url du webhook -> ')}").strip()
            CheckWebhook(webhook_url)

        threads_number = int(input(f"{Colorate.Horizontal(Colors.blue_to_cyan, 'Nombre de thread -> ')}"))

        while True:
            request(threads_number, webhook_enabled, webhook_url)

    except Exception as e:
        ErrorModule(e)
