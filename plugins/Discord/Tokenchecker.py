import json
import os
import requests
import time
import threading
import ctypes
import concurrent.futures
from pathlib import Path
from pystyle import Colors, Colorate
import random

def print_text_slowly(text, delay=0.1):
    """Affiche le texte lentement, ligne par ligne."""
    lines = text.splitlines()
    for line in lines:
        print(Colorate.Horizontal(Colors.white_to_black, line))
        time.sleep(delay)
    print()

def load_proxies():
    """Charge les proxies depuis le fichier proxies.txt."""
    proxies_file_path = current_path.parent.parent / 'proxies.txt'
    if proxies_file_path.exists():
        with open(proxies_file_path, 'r') as f:
            proxies = [line.strip() for line in f if line.strip()]
        print(f"Loaded proxies: {proxies}")  # Debug message
        return proxies
    print("Proxies file not found.")  # Debug message
    return []

def get_random_proxy(proxies):
    """Retourne un proxy aléatoire à partir de la liste des proxies."""
    return random.choice(proxies) if proxies else None

def cls():
    """Nettoie l'écran."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Définir le chemin du répertoire de travail (deux niveaux au-dessus du répertoire actuel)
current_path = Path(__file__).resolve().parent
tokens_file_path = current_path.parent.parent / 'tokens.txt'
config_file = current_path / 'config.js'

# Définir le dossier de sortie
OUTPUT_FOLDER = f'{current_path.parent.parent}/output/{time.strftime("%Y-%m-%d_%H-%M-%S")}'
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Configuration
CONFIG = {
    "threads": 10
}
SETTINGS = {
    "nitro": True,
    "age": True,
    "type": True,
    "flagged": True
}

# Lire le fichier de configuration
def load_config():
    if not config_file.is_file():
        print(f"Configuration file {config_file} is missing.")
        exit(1)

    with open(config_file, 'r') as f:
        config_data = json.load(f)

    expected_config = {
        "github": "Github Yozoxir/TraceEye",
        "discord": "discord.gg/traceye"
    }

    if config_data != expected_config:
        print("Configuration file does not match the expected format.")
        exit(1)

load_config()

# Nettoyer l'écran au début
cls()

# Affichage introductif
intro_text = """\
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
print_text_slowly(intro_text)

# Lire les tokens
if not tokens_file_path.exists():
    raise FileNotFoundError(f"Token file not found at {tokens_file_path}")

with open(tokens_file_path, 'r') as f:
    tokens = f.readlines()
tokens = list(set([token.strip() for token in tokens]))

# Demander si les proxies doivent être utilisés
use_proxies = input("Use proxies? (yes/no) -> ").strip().lower() == 'yes'
proxies = load_proxies() if use_proxies else []

valid = 0
invalid = 0
locked = 0
nitro = 0
flagged = 0
total = len(tokens)
current = 0
done = False

def check_token(token):
    global current, valid, invalid, locked, nitro, flagged
    headers = {
        "Authorization": token
    }
    
    proxy = get_random_proxy(proxies) if use_proxies else None
    proxy_dict = {"http": f"http://{proxy}", "https": f"https://{proxy}"} if proxy else None
    if proxy_dict:
        print(f"Using proxy: {proxy}")  # Debug message

    try:
        response = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers, proxies=proxy_dict)
        if response.status_code == 429:
            print(f"Rate limited: {token}")
            return

        current += 1
        if response.status_code == 401:
            invalid += 1
            with open(f"{OUTPUT_FOLDER}/invalid.txt", "a") as f:
                f.write(token + "\n")
            print(f"[/] [Token: {token}] Age: N/A Billing: N/A Nitro: N/A Flagged: N/A Valid: Invalid", end='\r')
            return

        if response.status_code == 403:
            locked += 1
            with open(f"{OUTPUT_FOLDER}/locked.txt", "a") as f:
                f.write(token + "\n")
            print(f"[/] [Token: {token}] Age: N/A Billing: N/A Nitro: N/A Flagged: N/A Valid: Locked", end='\r')
            return

        if response.status_code == 200:
            # Get user details
            user_response = requests.get("https://discord.com/api/v9/users/@me", headers=headers, proxies=proxy_dict)
            user_data = user_response.json()

            user_id = user_data["id"]
            user_email = user_data.get("email")
            user_phone = user_data.get("phone")
            user_flags = user_data.get("flags", 0)

            account_type = "unclaimed"
            if user_email:
                account_type = "email verified"
            if user_phone:
                if account_type == "email verified":
                    account_type = "fully verified"
                else:
                    account_type = "phone verified"

            # Save valid token
            valid += 1
            with open(f"{OUTPUT_FOLDER}/valid.txt", "a") as f:
                f.write(token + "\n")

            # Check Nitro subscription
            billing = False
            if SETTINGS["nitro"]:
                billing_response = requests.get("https://discord.com/api/v9/users/@me/billing/subscriptions", headers=headers, proxies=proxy_dict)
                if billing_response.status_code == 200:
                    subscriptions = billing_response.json()
                    if subscriptions:
                        billing = True
                        with open(f"{OUTPUT_FOLDER}/billing.txt", "a") as f:
                            f.write(token + "\n")

            # Check account age
            age = "Unknown"
            if SETTINGS["age"]:
                created_at = ((int(user_id) >> 22) + 1420070400000) / 1000
                age_days = (time.time() - created_at) / 86400
                age_months = age_days / 30
                age = f"{age_months:.0f} months" if age_months < 12 else f"{age_months / 12:.0f} years"
                age_folder = f"{OUTPUT_FOLDER}/age/{age}"
                os.makedirs(age_folder, exist_ok=True)
                with open(f"{age_folder}/{account_type}.txt", "a") as f:
                    f.write(token + "\n")

            # Check account flags
            flagged_status = "No"
            if SETTINGS["flagged"] and user_flags & 1048576 == 1048576:
                flagged += 1
                flagged_status = "Yes"
                with open(f"{OUTPUT_FOLDER}/flagged.txt", "a") as f:
                    f.write(token + "\n")

            # Print result
            validity = "Valid" if response.status_code == 200 else "Invalid"
            color = Colors.green if validity == "Valid" else Colors.red
            print(f"[/] [Token: {token}] Age: {age} Billing: {'Yes' if billing else 'No'} Nitro: {'Yes' if billing else 'No'} Flagged: {flagged_status} Valid: {Colorate.Vertical(color, validity)}", end='\r')

        # Ajouter un délai pour éviter les problèmes de rate limiting
        time.sleep(1)

    except Exception as e:
        print(f"Error checking token {token}: {e}")

def update_title():
    global done, current, total
    try:
        while not done:
            time.sleep(0.1)
            percentage = (current / total * 100) if total != 0 else 0
            title = f"Token Checker | Valid: {valid} | Invalid: {invalid} | Locked: {locked} | Remaining: {len(tokens)} | Checked: {percentage:.2f}%"
            ctypes.windll.kernel32.SetConsoleTitleW(title)
    except ZeroDivisionError:
        print("Error: No tokens to check.")

def main():
    global done
    update = threading.Thread(target=update_title)
    update.start()

    with concurrent.futures.ThreadPoolExecutor(max_workers=CONFIG["threads"]) as executor:
        executor.map(check_token, tokens)

    done = True
    update.join()
    print(f"Checked {current} tokens")
    print(f"Valid tokens: {valid}")
    print(f"Invalid tokens: {invalid}")
    print(f"Locked tokens: {locked}")
    print(f"Tokens with Nitro: {nitro}")
    print(f"Flagged tokens: {flagged}")

if __name__ == "__main__":
    main()
