import json
import os
import requests
import time
from pystyle import Colors, Colorate, Center

# Nettoyer l'écran (fonction pour Windows)
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fonction pour afficher le texte lentement
def print_text_slowly(lines, delay=0.1):
    """Affiche les lignes lentement, une par une."""
    for line in lines:
        print(Colorate.Horizontal(Colors.white_to_black, line))
        time.sleep(delay)
    print()

# ASCII Art
ascii_art = """
░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░  ░▒▓██████▓▒░░▒▓██████▓▒░   
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░▒▓████████▓▒░  ░▒▓█▓▒░   ░▒▓████████▓▒░

                                ┏━━━━━━━━━━━━━━━━━━━━━┓
                                ┃Github :  Yozoxir    ┃
                                ┃Discord: .gg/TraceEye┃
                                ┗━━━━━━━━━━━━━━━━━━━━━┛                             
"""

def Title(text):
    lines = text.splitlines()
    print_text_slowly(lines)

def info_webhook(webhook_url):
    headers = {
        'Content-Type': 'application/json',
    }

    try:
        response = requests.get(webhook_url, headers=headers)
        response.raise_for_status() 
        webhook_info = response.json()
        print_text_slowly(["\nInformation Webhook:"])

        print_text_slowly([f"ID      : {webhook_info['id']}"])
        print_text_slowly([f"Token   : {webhook_info['token']}"])
        print_text_slowly([f"Name    : {webhook_info['name']}"])
        print_text_slowly([f"Avatar  : {webhook_info['avatar']}"])
        print_text_slowly([f"Type    : {'bot' if webhook_info['type'] == 1 else 'webhook utilisateur'}"])
        print_text_slowly([f"Channel ID : {webhook_info['channel_id']}"])
        print_text_slowly([f"Server ID  : {webhook_info['guild_id']}"])

        print_text_slowly(["\nUser information associated with the Webhook:"])
        if 'user' in webhook_info and webhook_info['user']:
            user_info = webhook_info['user']
            print_text_slowly([f"ID          : {user_info['id']}"])
            print_text_slowly([f"Name        : {user_info['username']}"])
            print_text_slowly([f"DisplayName : {user_info['global_name']}"])
            print_text_slowly([f"Number      : {user_info['discriminator']}"])
            print_text_slowly([f"Avatar      : {user_info['avatar']}"])
            print_text_slowly([f"Flags       : {user_info['flags']} Publique: {user_info['public_flags']}"])
            print_text_slowly([f"Color       : {user_info['accent_color']}"])
            print_text_slowly([f"Decoration  : {user_info['avatar_decoration_data']}"])
            print_text_slowly([f"Banner      : {user_info['banner_color']}"])
            print("")
        else:
            print_text_slowly(["\nNo user information associated with the Webhook."])

    except requests.exceptions.RequestException as e:
        Error(e)

def Error(e):
    print_text_slowly([f"[ERROR] {e}"])

if __name__ == "__main__":
    cls()
    Title(ascii_art)

    try:
        webhook_url = input(Colorate.Horizontal(Colors.white_to_black, "\nWebhook URL -> "))
        info_webhook(webhook_url)

    except Exception as e:
        Error(e)
