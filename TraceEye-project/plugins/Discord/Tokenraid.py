import os
import json
import threading
import requests
from pystyle import Colorate, Colors
import time

# Nettoyage de l'écran
os.system('cls')  # Utilisez 'clear' pour Linux/Mac

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

def print_text_slowly(text, delay=0.1):
    lines = text.splitlines()
    for line in lines:
        print(Colorate.Horizontal(Colors.white_to_black, line))
        time.sleep(delay)

def ErrorModule(e):
    print(Colorate.Horizontal(Colors.white_to_black, f"[ERROR] Module Error: {e}"))

def log_result(result):
    with open("raid_log.txt", "a") as log_file:
        log_file.write(result + "\n")

def main():
    # Affiche l'art ASCII ligne par ligne avec effet white_to_black
    print_text_slowly(ascii_art)

    token_discord = input(Colorate.Horizontal(Colors.white_to_black, "Enter your Discord token -> ")).strip()
    channel_id = input(Colorate.Horizontal(Colors.white_to_black, "Enter the Discord channel ID -> ")).strip()
    raid_type = input(Colorate.Horizontal(Colors.white_to_black, "Choose the raid type (message/mention/joinleave) -> ")).strip().lower()
    
    if raid_type not in ["message", "mention", "joinleave"]:
        print(Colorate.Horizontal(Colors.white_to_black, "Error: Invalid raid type."))
        exit(1)

    message = input(Colorate.Horizontal(Colors.white_to_black, "Spam Message -> ")).strip()
    message_sensur = message[:10] + "..." if len(message) > 10 else message

    threads_number = 0
    while True:
        try:
            threads_number = int(input(Colorate.Horizontal(Colors.white_to_black, "Threads Number (recommended: 2, 4) -> ")))
            break
        except ValueError:
            print(Colorate.Horizontal(Colors.white_to_black, "Error: Invalid input for number of threads."))

    delay = float(input(Colorate.Horizontal(Colors.white_to_black, "Delay between messages (seconds) -> ")).strip())

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
            result = f"Message: {message_sensur} | Channel: {channel_id} | Status: Send"
            print(Colorate.Horizontal(Colors.white_to_black, result))
            log_result(result)
        except requests.exceptions.RequestException as e:
            result = f"Message: {message_sensur} | Channel: {channel_id} | Status: Error {e}"
            print(Colorate.Horizontal(Colors.white_to_black, result))
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
                result = f"Mention Message: {mention_message[:10]}... | Channel: {channel_id} | Status: Send"
                print(Colorate.Horizontal(Colors.white_to_black, result))
                log_result(result)
                time.sleep(delay)
        except requests.exceptions.RequestException as e:
            result = f"Mention Message: {mention_message[:10]}... | Channel: {channel_id} | Status: Error {e}"
            print(Colorate.Horizontal(Colors.white_to_black, result))
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
            print(Colorate.Horizontal(Colors.white_to_black, "Error: Invalid input for number of threads."))

        for thread in threads:
            thread.join()

    while True:
        request()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        ErrorModule(e)
