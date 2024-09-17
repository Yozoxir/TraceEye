import requests
import json
import time
from pystyle import Colors, Colorate, Center
import os

os.system ('cls')

# Fonction pour afficher le texte lentement
def print_text_slowly(text, delay=0.1):
    """Affiche le texte lentement, ligne par ligne."""
    lines = text.splitlines()
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

def change_username(token, new_username):
    url = 'https://discord.com/api/v9/users/@me'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    data = {
        'username': new_username
    }

    try:
        response = requests.patch(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        print_text_slowly(f"Nom d'utilisateur changé en {new_username}")
    except requests.exceptions.HTTPError as err:
        print_text_slowly(f"Erreur lors du changement du nom d'utilisateur -> {err}")
    except Exception as e:
        print_text_slowly(f"Erreur : {e}")

if __name__ == "__main__":
    print_text_slowly(ascii_art)

    token = input(Colorate.Horizontal(Colors.white_to_black, "Entrez le token du compte Discord -> "))
    new_username = input(Colorate.Horizontal(Colors.white_to_black, "Entrez le nouveau nom d'utilisateur -> "))

    change_username(token, new_username)
