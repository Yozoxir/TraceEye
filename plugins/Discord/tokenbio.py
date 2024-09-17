import requests
import json
import time
from pystyle import Colors, Colorate, Center

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
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░▒▓████████▓▒░  ░▒▓█▓▒░   ░▒▓████████▓▒░

                                ┏━━━━━━━━━━━━━━━━━━━━━┓
                                ┃Github :  Yozoxir    ┃
                                ┃Discord: .gg/TraceEye┃
                                ┗━━━━━━━━━━━━━━━━━━━━━┛
"""

def change_bio(token, new_bio):
    url = 'https://discord.com/api/v9/users/@me'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    data = {
        'bio': new_bio
    }

    try:
        response = requests.patch(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        print_text_slowly("Bio mise à jour avec succès !")
    except requests.exceptions.HTTPError as err:
        print_text_slowly(f"Erreur lors de la mise à jour de la bio : {err}")
    except Exception as e:
        print_text_slowly(f"Erreur : {e}")

if __name__ == "__main__":
    print_text_slowly(ascii_art)

    token = input(Colorate.Horizontal(Colors.white_to_black, "Entrez le token du compte Discord -> "))
    new_bio = input(Colorate.Horizontal(Colors.white_to_black, "Entrez la nouvelle bio -> "))

    change_bio(token, new_bio)
