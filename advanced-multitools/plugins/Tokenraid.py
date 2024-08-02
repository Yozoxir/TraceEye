import random
import threading
import requests
import os
from pystyle import Colorate, Colors
import time
os.system("cls")
ascii_art = """
 $$$$$$\  $$$$$$$\  $$\    $$\  $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$$\ $$$$$$$\        $$$$$$$$\  $$$$$$\  $$\   $$\ $$$$$$$$\ $$\   $$\       $$$$$$$\   $$$$$$\  $$$$$$\ $$$$$$$\  $$$$$$$$\ $$$$$$$\  
$$  __$$\ $$  __$$\ $$ |   $$ |$$  __$$\ $$$\  $$ |$$  __$$\ $$  _____|$$  __$$\       \__$$  __|$$  __$$\ $$ | $$  |$$  _____|$$$\  $$ |      $$  __$$\ $$  __$$\ \_$$  _|$$  __$$\ $$  _____|$$  __$$\ 
$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|$$ |      $$ |  $$ |         $$ |   $$ /  $$ |$$ |$$  / $$ |      $$$$\ $$ |      $$ |  $$ |$$ /  $$ |  $$ |  $$ |  $$ |$$ |      $$ |  $$ |
$$$$$$$$ |$$ |  $$ |\$$\  $$  |$$$$$$$$ |$$ $$\$$ |$$ |      $$$$$\    $$ |  $$ |         $$ |   $$ |  $$ |$$$$$  /  $$$$$\    $$ $$\$$ |      $$$$$$$  |$$$$$$$$ |  $$ |  $$ |  $$ |$$$$$\    $$$$$$$  |
$$  __$$ |$$ |  $$ | \$$\$$  / $$  __$$ |$$ \$$$$ |$$ |      $$  __|   $$ |  $$ |         $$ |   $$ |  $$ |$$  $$<   $$  __|   $$ \$$$$ |      $$  __$$< $$  __$$ |  $$ |  $$ |  $$ |$$  __|   $$  __$$< 
$$ |  $$ |$$ |  $$ |  \$$$  /  $$ |  $$ |$$ |\$$$ |$$ |  $$\ $$ |      $$ |  $$ |         $$ |   $$ |  $$ |$$ |\$$\  $$ |      $$ |\$$$ |      $$ |  $$ |$$ |  $$ |  $$ |  $$ |  $$ |$$ |      $$ |  $$ |
$$ |  $$ |$$$$$$$  |   \$  /   $$ |  $$ |$$ | \$$ |\$$$$$$  |$$$$$$$$\ $$$$$$$  |         $$ |    $$$$$$  |$$ | \$$\ $$$$$$$$\ $$ | \$$ |      $$ |  $$ |$$ |  $$ |$$$$$$\ $$$$$$$  |$$$$$$$$\ $$ |  $$ |
\__|  \__|\_______/     \_/    \__|  \__|\__|  \__| \______/ \________|\_______/          \__|    \______/ \__|  \__|\________|\__|  \__|      \__|  \__|\__|  \__|\______|\_______/ \________|\__|  \__| 
"""

def ErrorModule(e):
    print(Colorate.Horizontal(Colors.red_to_yellow, f"[ERREUR] Erreur de module: {e}"))

def log_result(result):
    with open("raid_log.txt", "a") as log_file:
        log_file.write(result + "\n")

try:
    print(Colorate.Horizontal(Colors.cyan_to_blue, ascii_art))

    token_discord = input(Colorate.Horizontal(Colors.green_to_blue, "Discord token -> ")).strip()
    channel_id = input(Colorate.Horizontal(Colors.green_to_blue, "Entrer l'id du channel -> ")).strip()
    raid_type = input(Colorate.Horizontal(Colors.green_to_blue, "Choisissez le mode de raid (message/mention/joinleave) -> ")).strip().lower()
    
    if raid_type not in ["message", "mention", "joinleave"]:
        print(Colorate.Horizontal(Colors.red_to_yellow, "Erreur: type de raid invalide."))
        exit(1)

    message = input(Colorate.Horizontal(Colors.green_to_blue, "Message a spam -> ")).strip()
    message_sensur = message[:10] + "..." if len(message) > 10 else message

    threads_number = 0
    while True:
        try:
            threads_number = int(input(Colorate.Horizontal(Colors.green_to_blue, "Nombre de thread (recommender: 2, 4) -> ")))
            break
        except ValueError:
            print(Colorate.Horizontal(Colors.red_to_yellow, "Erreur: Nombre de threads invalide."))

    delay = float(input(Colorate.Horizontal(Colors.green_to_blue, "Delai entre les messages (secondes) -> ")).strip())

    def get_all_members(server_id):
        headers = {
            'Authorization': token_discord
        }
        members = []
        after = None

        while True:
            url = f"https://discord.com/api/v9/guilds/{server_id}/members?limit=1000"
            if after:
                url += f"&after={after}"
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            members.extend(data)
            if len(data) < 1000:
                break
            after = data[-1]['user']['id']

        return [member['user']['id'] for member in members]

    def raid_message():
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                'Authorization': token_discord
            }
            response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages",
                                     json={'content': message},
                                     headers=headers)
            response.raise_for_status()
            result = f"Message: {message_sensur} | Channel: {channel_id} | Statut: Envoyer"
            print(Colorate.Horizontal(Colors.green_to_blue, result))
            log_result(result)
        except requests.exceptions.RequestException as e:
            result = f"Message: {message_sensur} | Channel: {channel_id} | Statut: Erreur {e}"
            print(Colorate.Horizontal(Colors.red_to_yellow, result))
            log_result(result)

    def raid_mention():
        try:
            server_id = channel_id  # Assuming channel_id is the same as server_id
            member_ids = get_all_members(server_id)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                'Authorization': token_discord
            }

            for member_id in member_ids:
                mention_message = f"<@{member_id}> {message}"
                response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages",
                                         json={'content': mention_message},
                                         headers=headers)
                response.raise_for_status()
                result = f"Mention Message: {mention_message[:10]}... | Channel: {channel_id} | Status: Envoyer"
                print(Colorate.Horizontal(Colors.green_to_blue, result))
                log_result(result)
                time.sleep(delay)
        except requests.exceptions.RequestException as e:
            result = f"Mention Message: {mention_message[:10]}... | Channel: {channel_id} | Status: Erreur {e}"
            print(Colorate.Horizontal(Colors.red_to_yellow, result))
            log_result(result)

 

    def request():
        threads = []
        try:
            for _ in range(threads_number):
                if raid_type == "message":
                    t = threading.Thread(target=raid_message)
                elif raid_type == "mention":
                    t = threading.Thread(target=raid_mention)
                t.start()
                threads.append(t)
                time.sleep(delay)
        except ValueError:
            print(Colorate.Horizontal(Colors.red_to_yellow, "Erreur: Nombre de threads Invalide."))

        for thread in threads:
            thread.join()

    while True:
        request()

except Exception as e:
    ErrorModule(e)
