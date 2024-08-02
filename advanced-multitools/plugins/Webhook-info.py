from pystyle import Colors, Colorate, Center
import requests

ascii_art = """
 $$$$$$\\  $$$$$$$\\  $$\\    $$\\  $$$$$$\\  $$\\   $$\\  $$$$$$\\  $$$$$$$$\\ $$$$$$$\\        $$\\      $$\\ $$$$$$$$\\ $$$$$$$\\  $$\\   $$\\  $$$$$$\\   $$$$$$\\  $$\\   $$\\       $$$$$$\\ $$\\   $$\\ $$$$$$$$\\  $$$$$$\\  
$$  __$$\\ $$  __$$\\ $$ |   $$ |$$  __$$\\ $$$\\  $$ |$$  __$$\\ $$  _____|$$  __$$\\       $$ | $\\  $$ |$$  _____|$$  __$$\\ $$ |  $$ |$$  __$$\\ $$  __$$\\ $$ | $$  |      \\_$$  _|$$$\\  $$ |$$  _____|$$  __$$\\ 
$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ /  $$ |$$$$\\ $$ |$$ /  \\__|$$ |      $$ |  $$ |      $$ |$$\\$ $$ |$$ |      $$ |  $$ |$$ |  $$ |$$ /  $$ |$$ /  $$ |$$ |$$  /         $$ |  $$$$\\ $$ |$$ |      $$ /  $$ |
$$$$$$$$ |$$ |  $$ |\\$$\\  $$  |$$$$$$$$ |$$ $$\\$$ |$$ |      $$$$$\\    $$ |  $$ |      $$ $$ $$\\$$ |$$$$$\\    $$$$$$$\\ |$$$$$$$$ |$$ |  $$ |$$ |  $$ |$$$$$  /          $$ |  $$ $$\\$$ |$$$$$\\    $$ |  $$ |
$$  __$$ |$$ |  $$ | \\$$\\$$  / $$  __$$ |$$ \\$$$$ |$$ |      $$  __|   $$ |  $$ |      $$$$  _$$$$ |$$  __|   $$  __$$\\ $$  __$$ |$$ |  $$ |$$ |  $$ |$$  $$<           $$ |  $$ \\$$$$ |$$  __|   $$ |  $$ |
$$ |  $$ |$$ |  $$ |  \\$$$  /  $$ |  $$ |$$ |\\$$$ |$$ |  $$\\ $$ |      $$ |  $$ |      $$$  / \\$$$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\\$$\\          $$ |  $$ |\\$$$ |$$ |      $$ |  $$ |
$$ |  $$ |$$$$$$$  |   \\$  /   $$ |  $$ |$$ | \\$$ |\\$$$$$$  |$$$$$$$$\\ $$$$$$$  |      $$  /   \\$$ |$$$$$$$$\\ $$$$$$$  |$$ |  $$ | $$$$$$  | $$$$$$  |$$ | \\$$\\       $$$$$$\\ $$ | \\$$ |$$ |       $$$$$$  |
\\__|  \\__|\\_______/     \\_/    \\__|  \\__|\\__|  \\__| \\______/ \\________|\\_______/       \\__/     \\__|\\________|\\_______/ \\__|  \\__| \\______/  \\______/ \\__|  \\__|      \\______|\\__|  \\__|\\__|       \\______/                                
"""

def Title(text):
    print(Colorate.Horizontal(Colors.red_to_yellow, Center.XCenter(text)))

def info_webhook(webhook_url):
    headers = {
        'Content-Type': 'application/json',
    }

    try:
        response = requests.get(webhook_url, headers=headers)
        response.raise_for_status() 
        webhook_info = response.json()
        print(Colorate.Horizontal(Colors.red_to_yellow, "\nInformation Webhook:"))

        print(Colorate.Horizontal(Colors.red_to_yellow, f"ID      : {webhook_info['id']}"))
        print(Colorate.Horizontal(Colors.red_to_yellow, f"Token   : {webhook_info['token']}"))
        print(Colorate.Horizontal(Colors.red_to_yellow, f"Name    : {webhook_info['name']}"))
        print(Colorate.Horizontal(Colors.red_to_yellow, f"Avatar  : {webhook_info['avatar']}"))
        print(Colorate.Horizontal(Colors.red_to_yellow, f"Type    : {'bot' if webhook_info['type'] == 1 else 'webhook utilisateur'}"))
        print(Colorate.Horizontal(Colors.red_to_yellow, f"Channel ID : {webhook_info['channel_id']}"))
        print(Colorate.Horizontal(Colors.red_to_yellow, f"Server ID  : {webhook_info['guild_id']}"))

        print(Colorate.Horizontal(Colors.red_to_yellow, "\nUser information associated with the Webhook:"))
        if 'user' in webhook_info and webhook_info['user']:
            user_info = webhook_info['user']
            print(Colorate.Horizontal(Colors.red_to_yellow, f"ID          : {user_info['id']}"))
            print(Colorate.Horizontal(Colors.red_to_yellow, f"Name        : {user_info['username']}"))
            print(Colorate.Horizontal(Colors.red_to_yellow, f"DisplayName : {user_info['global_name']}"))
            print(Colorate.Horizontal(Colors.red_to_yellow, f"Number      : {user_info['discriminator']}"))
            print(Colorate.Horizontal(Colors.red_to_yellow, f"Avatar      : {user_info['avatar']}"))
            print(Colorate.Horizontal(Colors.red_to_yellow, f"Flags       : {user_info['flags']} Publique: {user_info['public_flags']}"))
            print(Colorate.Horizontal(Colors.red_to_yellow, f"Color       : {user_info['accent_color']}"))
            print(Colorate.Horizontal(Colors.red_to_yellow, f"Decoration  : {user_info['avatar_decoration_data']}"))
            print(Colorate.Horizontal(Colors.red_to_yellow, f"Banner      : {user_info['banner_color']}"))
            print("")
        else:
            print(Colorate.Horizontal(Colors.red_to_yellow, "\nNo user information associated with the Webhook."))

    except requests.exceptions.RequestException as e:
        Error(e)

def Error(e):
    print(Colorate.Horizontal(Colors.red_to_yellow, f"[ERROR] {e}"))

if __name__ == "__main__":
    print(Colorate.Horizontal(Colors.red_to_yellow, ascii_art))

    try:
        webhook_url = input(Colorate.Horizontal(Colors.red_to_yellow, "\nWebhook URL -> "))
        info_webhook(webhook_url)
        input(f"\nPress ENTER to exit...")

    except Exception as e:
        Error(e)
