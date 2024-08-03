import phonenumbers
import os
from phonenumbers import geocoder, carrier, timezone
from pystyle import Colorate, Colors

os.system("cls")

def display_ascii_art():
    ascii_art = """
 $$$$$$\\  $$$$$$$\\  $$\\    $$\\  $$$$$$\\  $$\\   $$\\  $$$$$$\\  $$$$$$$$\\ $$$$$$$\\        $$\\       $$$$$$\\   $$$$$$\\  $$\\   $$\\ $$\\   $$\\ $$$$$$$\\  
$$  __$$\\ $$  __$$\\ $$ |   $$ |$$  __$$\\ $$$\\  $$ |$$  __$$\\ $$  _____|$$  __$$\\       $$ |     $$  __$$\\ $$  __$$\\ $$ | $$  |$$ |  $$ |$$  __$$\\ 
$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ /  $$ |$$$$\\ $$ |$$ /  \\__|$$ |      $$ |  $$ |      $$ |     $$ /  $$ |$$ /  $$ |$$ |$$  / $$ |  $$ |$$ |  $$ |
$$$$$$$$ |$$ |  $$ |\\$$\\  $$  |$$$$$$$$ |$$ $$\\$$ |$$ |      $$$$$\\    $$ |  $$ |      $$ |     $$ |  $$ |$$ |  $$ |$$$$$  /  $$ |  $$ |$$$$$$$  |
$$  __$$ |$$ |  $$ | \\$$\\$$  / $$  __$$ |$$ \\$$$$ |$$ |      $$  __|   $$ |  $$ |      $$ |     $$ |  $$ |$$ |  $$ |$$  $$<   $$ |  $$ |$$  ____/ 
$$ |  $$ |$$ |  $$ |  \\$$$  /  $$ |  $$ |$$ |\\$$$ |$$ |  $$\\ $$ |      $$ |  $$ |      $$ |     $$ |  $$ |$$ |  $$ |$$ |\\$$\\  $$ |  $$ |$$ |      
$$ |  $$ |$$$$$$$  |   \\$  /   $$ |  $$ |$$ | \\$$ |\\$$$$$$  |$$$$$$$$\\ $$$$$$$  |      $$$$$$$$\\ $$$$$$  | $$$$$$  |$$ | \\$$\\ \\$$$$$$  |$$ |      
\\__|  \\__|\\_______/     \\_/    \\__|  \\__|\\__|  \\__| \\______/ \\________|\\_______/       \\________|\\______/  \\______/ \\__|  \\__| \\______/ \\__|          
"""
    colored_ascii_art = Colorate.Horizontal(Colors.blue_to_red, ascii_art)
    print(colored_ascii_art)

def main():
    display_ascii_art()

    try:
        while True:
            phone_number = input(Colorate.Horizontal(Colors.blue_to_red, "\nNuméro de téléphone -> "))
            print(Colorate.Horizontal(Colors.blue_to_red, "Information en cours..."))

            try:
                parsed_number = phonenumbers.parse(phone_number, None)
                if phonenumbers.is_valid_number(parsed_number):
                    if phone_number.startswith("+"):
                        country_code = "+" + phone_number[1:3]
                    else:
                        country_code = "None"
                    operator = carrier.name_for_number(parsed_number, "fr")
                    type_number = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixe"
                    timezones = timezone.time_zones_for_number(parsed_number)
                    timezone_info = timezones[0] if timezones else "None"
                    country = phonenumbers.region_code_for_number(parsed_number)
                    region = geocoder.description_for_number(parsed_number, "fr")
                    status = "Valid"
                    
                    print(Colorate.Horizontal(Colors.blue_to_red, f"""
Téléphone                    : {phone_number}
Code du Pays                 : {country_code}
Pays                         : {country}
Région                       : {region}
Timezone                     : {timezone_info}
Opérateur                    : {operator}
Type de numéro de téléphone  : {type_number}
                
                """))
                    
                else:
                    print(Colorate.Horizontal(Colors.blue_to_red, " Format invalide ! [Ex: +442012345678 or +33623456789]"))

            except Exception as e:
                print(Colorate.Horizontal(Colors.blue_to_red, f" Exception en cours: {e}"))

            choice = input(Colorate.Horizontal(Colors.blue_to_red,"Voulez-vous continuer? (y/n): ").strip().lower())
            if choice != 'y':
                break

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
