import os
import json
import requests
import time
import threading
from pystyle import Colorate, Colors

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

def print_text_slowly(text, delay=0.1):
    # Diviser le texte en lignes
    lines = text.splitlines()
    
    # Afficher chaque ligne avec un délai
    for line in lines:
        print(Colorate.Horizontal(Colors.white_to_black, line))
        time.sleep(delay)
    
    # Ajouter une ligne vide à la fin si nécessaire
    print()

def get_dm_channel_ids(token_discord):
    try:
        response = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token_discord})
        
        if response.status_code == 200:
            channels = response.json()
            dm_channel_ids = [channel['id'] for channel in channels if channel['type'] == 1]
            return dm_channel_ids
        else:
            print(Colorate.Horizontal(Colors.white_to_black, f"[ERROR] Status code {response.status_code}: Unable to fetch DM channels."))
            return []

    except Exception as e:
        print(Colorate.Horizontal(Colors.white_to_black, f"[ERROR] Error fetching DM channel IDs: {e}"))
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
                print(Colorate.Horizontal(Colors.white_to_black, f"[INFO] Message sent to channel ID: {channel_id}"))
            else:
                print(Colorate.Horizontal(Colors.white_to_black, f"[ERROR] Status code {response.status_code}: Unable to send message to channel ID: {channel_id}"))

    except Exception as e:
        print(Colorate.Horizontal(Colors.white_to_black, f"[ERROR] Error sending message: {e}"))

if __name__ == "__main__":
    try:
        # Nettoyage de l'écran
        os.system('cls')  # Utilisez 'clear' pour Linux/Mac
        
        # Afficher l'art ASCII une seule fois avec effet white_to_black
        print_text_slowly(ascii_art)
        
        token_discord = input(Colorate.Horizontal(Colors.white_to_black, "Token -> ")).strip()
        message = input(Colorate.Horizontal(Colors.white_to_black, "Message -> ")).strip()
        output_file = "dm_channel_ids.json"

        dm_channel_ids = get_dm_channel_ids(token_discord)

        if not dm_channel_ids:
            print(Colorate.Horizontal(Colors.white_to_black, "[INFO] No DM channel IDs collected. Exiting."))
            exit(0)

        save_ids_to_json(dm_channel_ids, output_file)
        print(Colorate.Horizontal(Colors.white_to_black, f"[INFO] Saved all DM channel IDs to {output_file}."))
        print(Colorate.Horizontal(Colors.white_to_black, f"[INFO] Total DM channel IDs collected: {len(dm_channel_ids)}"))

        proceed = input(Colorate.Horizontal(Colors.white_to_black, "Do you want to send the message to all collected DM channels? (y/n)")).strip().lower()

        if proceed == 'y':
            for channel_id in dm_channel_ids:
                t = threading.Thread(target=MassDM, args=(token_discord, [channel_id], message))
                t.start()
                t.join()
                print(Colorate.Horizontal(Colors.white_to_black, f"[INFO] Finished sending messages to channel {channel_id}."))
        else:
            print(Colorate.Horizontal(Colors.white_to_black, "Exiting without sending messages."))

    except Exception as e:
        print(Colorate.Horizontal(Colors.white_to_black, f"[ERROR] {e}"))
