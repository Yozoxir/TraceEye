import requests
from pystyle import Colorate, Colors, Write

def Continue():
    input("\nAppuyez sur Entrée pour continuer...")

def Reset():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def Error(e):
    Write.Print(f"Une erreur est survenue : {e}\n", Colors.red, interval=0.01)

def ErrorId():
    Write.Print("ID utilisateur invalide ou impossible de récupérer les informations.\n", Colors.red, interval=0.01)

ascii_art = """ 
 $$$$$$\  $$$$$$$\  $$\    $$\  $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$$\ $$$$$$$\        $$$$$$\ $$$$$$$\        $$$$$$\ $$\   $$\ $$$$$$$$\  $$$$$$\  
$$  __$$\ $$  __$$\ $$ |   $$ |$$  __$$\ $$$\  $$ |$$  __$$\ $$  _____|$$  __$$\       \_$$  _|$$  __$$\       \_$$  _|$$$\  $$ |$$  _____|$$  __$$\ 
$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|$$ |      $$ |  $$ |        $$ |  $$ |  $$ |        $$ |  $$$$\ $$ |$$ |      $$ /  $$ |
$$$$$$$$ |$$ |  $$ |\$$\  $$  |$$$$$$$$ |$$ $$\$$ |$$ |      $$$$$\    $$ |  $$ |$$$$$$\ $$ |  $$ |  $$ |$$$$$$\ $$ |  $$ $$\$$ |$$$$$\    $$ |  $$ |
$$  __$$ |$$ |  $$ | \$$\$$  / $$  __$$ |$$ \$$$$ |$$ |      $$  __|   $$ |  $$ |\______|$$ |  $$ |  $$ |\______|$$ |  $$ \$$$$ |$$  __|   $$ |  $$ |
$$ |  $$ |$$ |  $$ |  \$$$  /  $$ |  $$ |$$ |\$$$ |$$ |  $$\ $$ |      $$ |  $$ |        $$ |  $$ |  $$ |        $$ |  $$ |\$$$ |$$ |      $$ |  $$ |
$$ |  $$ |$$$$$$$  |   \$  /   $$ |  $$ |$$ | \$$ |\$$$$$$  |$$$$$$$$\ $$$$$$$  |      $$$$$$\ $$$$$$$  |      $$$$$$\ $$ | \$$ |$$ |       $$$$$$  |
\__|  \__|\_______/     \_/    \__|  \__|\__|  \__| \______/ \________|\_______/       \______|\_______/       \______|\__|  \__|\__|       \______/
 """

print(Colorate.Horizontal(Colors.blue_to_cyan, ascii_art))

def format_value(value, default="Inconnu"):
    if value is None:
        return default
    elif isinstance(value, bool):
        return "Oui" if value else "Non"
    return value

try:
    user_id = input(Colorate.Horizontal(Colors.blue_to_cyan, f"\nEntrer l'ID -> "))
    Write.Print(f"Récupération des informations...\n", Colors.blue_to_cyan, interval=0.01)

    try:
        user_info_response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
        user_info = user_info_response.json()

        if user_info_response.status_code != 200:
            ErrorId()
        else:
            userid = format_value(user_info.get('id'))
            display_name = format_value(user_info.get('displayName'))
            username = format_value(user_info.get('name'))
            description = format_value(user_info.get('description'), "Non disponible")
            created_at = format_value(user_info.get('created'))
            is_banned = format_value(user_info.get('isBanned'))
            external_app_display_name = format_value(user_info.get('externalAppDisplayName'), "Non disponible")
            has_verified_badge = format_value(user_info.get('hasVerifiedBadge'))
            join_date = format_value(user_info.get('created'))

            groups_response = requests.get(f"https://groups.roblox.com/v2/users/{user_id}/groups/roles")
            groups_info = groups_response.json().get('data', [])
            groups = ", ".join([group['group']['name'] for group in groups_info]) or "Aucun groupe"

            favorites_response = requests.get(f"https://games.roblox.com/v2/users/{user_id}/favorite/games")
            favorites_info = favorites_response.json().get('data', [])
            favorite_games = ", ".join([game['name'] for game in favorites_info]) or "Aucun jeu favori"

            info_text = f"""
Username            : {username}
Id                  : {userid}
Display Name        : {display_name}
Description         : {description}
Created             : {created_at}
Banned              : {is_banned}
External Name       : {external_app_display_name}
Verified Badge      : {has_verified_badge}
Join Date           : {join_date}
Groups              : {groups}
Favorite Games      : {favorite_games}
"""

            Write.Print(info_text, Colors.blue_to_cyan, interval=0.01)
            Continue()
            Reset()
    except Exception as e:
        Error(e)
except Exception as e:
    Error(e)
