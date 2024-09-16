import requests
import json
import time
from pystyle import Colors, Colorate, Center
import os 

os.system('cls')

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

def change_hypesquad_badge(token, badge_id):
    url = 'https://discord.com/api/v9/users/@me/hypesquad/online'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    data = {
        'house': badge_id
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        print_text_slowly(f"Badge HypeSquad changé en ID {badge_id}")
    except requests.exceptions.HTTPError as err:
        print_text_slowly(f"Erreur lors du changement du badge HypeSquad : {err}")
    except Exception as e:
        print_text_slowly(f"Erreur : {e}")

if __name__ == "__main__":
    print_text_slowly(ascii_art)

    token = input(Colorate.Horizontal(Colors.white_to_black, "Entrez le token du compte Discord -> "))
    badge_id = input(Colorate.Horizontal(Colors.white_to_black, "Entrez l'ID du badge HypeSquad (1: Bravery, 2: Brilliance, 3: Balance) -> "))

    if badge_id not in ['1', '2', '3']:
        print_text_slowly("ID de badge HypeSquad invalide. Veuillez entrer 1, 2 ou 3.")
    else:
        change_hypesquad_badge(token, badge_id)
