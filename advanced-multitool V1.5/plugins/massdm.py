import json
import requests
from pystyle import Colorate, Colors
import threading
import os

os.system("cls")

interface = """
 $$$$$$\\  $$$$$$$\\  $$\\    $$\\  $$$$$$\\  $$\\   $$\\  $$$$$$\\  $$$$$$$$\\ $$$$$$$\\        $$\\      $$\\  $$$$$$\\   $$$$$$\\   $$$$$$\\  $$$$$$$\\  $$\\      $$\\ 
$$  __$$\\ $$  __$$\\ $$ |   $$ |$$  __$$\\ $$$\\  $$ |$$  __$$\\ $$  _____|$$  __$$\\       $$$\\    $$$ |$$  __$$\\ $$  __$$\\ $$  __$$\\ $$  __$$\\ $$$\\    $$$ |
$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ /  $$ |$$$$\\ $$ |$$ /  \\__|$$ |      $$ |  $$ |      $$$$\\  $$$$ |$$ /  $$ |$$ /  \\__|$$ /  \\__|$$ |  $$ |$$$$\\  $$$$ |
$$$$$$$$ |$$ |  $$ |\\$$\\  $$  |$$$$$$$$ |$$ $$\\$$ |$$ |      $$$$$\\    $$ |  $$ |      $$\\$$\\$$ $$ |$$$$$$$$ |\\$$$$$$\\  \\$$$$$$\\  $$ |  $$ |$$\\$$\\$$ $$ |
$$  __$$ |$$ |  $$ | \\$$\\$$  / $$  __$$ |$$ \\$$$$ |$$ |      $$  __|   $$ |  $$ |      $$ \\$$$  $$ |$$  __$$ | \\____$$\\  \\____$$\\ $$ |  $$ |$$ \\$$$  $$ |
$$ |  $$ |$$ |  $$ |  \\$$$  /  $$ |  $$ |$$ |\\$$$ |$$ |  $$\\ $$ |      $$ |  $$ |      $$ |\\$  /$$ |$$ |  $$ |$$\\   $$ |$$\\   $$ |$$ |  $$ |$$ |\\$  /$$ |
$$ |  $$ |$$$$$$$  |   \\$  /   $$ |  $$ |$$ | \\$$ |\\$$$$$$  |$$$$$$$$\\ $$$$$$$  |      $$ | \\_/ $$ |$$ |  $$ |\\$$$$$$  |\\$$$$$$  |$$$$$$$  |$$ | \\_/ $$ |
\\__|  \\__|\\_______/     \\_/    \\__|  \\__|\\__|  \\__| \\______/ \\________|\\_______/       \\__|     \\__|\\__|  \\__| \\______/  \\______/ \\_______/ \\__|     \\__|
"""
ascii_art = Colorate.Horizontal(Colors.blue_to_purple, interface)
def get_dm_channel_ids(token_discord):
    try:
        response = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token_discord})
        
        if response.status_code == 200:
            channels = response.json()
            dm_channel_ids = [channel['id'] for channel in channels if channel['type'] == 1]
            return dm_channel_ids
        else:
            print(Colorate.Horizontal(Colors.blue_to_purple, f"[ERROR] Status code {response.status_code}: Impossible de récupérer vos DM."))
            return []

    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_purple, f"[ERROR] Erreur lors de la récupération des channel IDs des DM: {e}"))
        return []

def save_ids_to_json(dm_channel_ids, filename):
    with open(filename, 'w') as f:
        json.dump(dm_channel_ids, f, indent=4)

def MassDM(token_discord, dm_channel_ids, message):
    try:
        for channel_id in dm_channel_ids:
            response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages",
                                     headers={'Authorization': token_discord, 'Content-Type': 'application/json'},
                                     json={"content": message})
            if response.status_code == 200:
                print(Colorate.Horizontal(Colors.blue_to_purple, f"[INFO] Message envoyé vers channel ID: {channel_id}"))
            else:
                print(Colorate.Horizontal(Colors.blue_to_purple, f"[ERROR] Status code {response.status_code}: Impossible d'envoyer un message au channel ID: {channel_id}"))

    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_purple, f"[ERROR] Erreur lors de l'envoi du message: {e}"))

if __name__ == "__main__":
    try:
        print(ascii_art)
        
        token_discord = input(Colorate.Horizontal(Colors.blue_to_purple, "Token -> ")).strip()
        message = input(Colorate.Horizontal(Colors.blue_to_purple, "Message -> ")).strip()
        output_file = "dm_channel_ids.json"

        dm_channel_ids = get_dm_channel_ids(token_discord)

        if not dm_channel_ids:
            print(Colorate.Horizontal(Colors.blue_to_purple, "[INFO] Pas de channel ID de DM collecté. Sortie."))
            exit(0)

        save_ids_to_json(dm_channel_ids, output_file)
        print(Colorate.Horizontal(Colors.blue_to_purple, f"[INFO] Sauvegarde de tous les channel ID des DM à {output_file}."))
        print(Colorate.Horizontal(Colors.blue_to_purple, f"[INFO] Total de channel ID de DM collecté: {len(dm_channel_ids)}"))

        proceed = input(Colorate.Horizontal(Colors.blue_to_purple, "Voulez-vous envoyer un message à tous les DM collectés ? (y/n)")).strip().lower()

        if proceed == 'y':
            for channel_id in dm_channel_ids:
                t = threading.Thread(target=MassDM, args=(token_discord, [channel_id], message))
                t.start()
                t.join()
                print(Colorate.Horizontal(Colors.blue_to_purple, f"[INFO] Fin de l'envoie de message au channel {channel_id}."))
        else:
            print(Colorate.Horizontal(Colors.blue_to_purple, "Sortie sans avoir envoyé les mesasges."))

    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_purple, f"[ERROR] {e}"))
