import subprocess
import requests
import socket
import platform
import concurrent.futures
import re
from pystyle import Colors, Colorate, Center
import whois
import os

os.system("cls")

def ping_ip(ip_address):
    try:
        result = subprocess.run(['ping', ip_address], capture_output=True, text=True, timeout=10)
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"\n{'=' * 60}\nPINGING {ip_address}\n{'=' * 60}"))
        print(result.stdout)
    except subprocess.TimeoutExpired:
        print(Colorate.Horizontal(Colors.blue_to_cyan, "Timeout expired. No response received."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"An error occurred: {e}"))

def get_ip_information(ip_address):
    try:
        api_key = 'bf609e0ae94346a69905706a764efce5'
        response = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}").json()
        
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"\n{'=' * 60}\nIP Information\n{'=' * 60}"))

        ip_info = {
            "IP Address": response.get("ip"),
            "Continent": f"{response.get('continent_name')} ({response.get('continent_code')})",
            "Country": f"{response.get('country_name')} ({response.get('country_code3')})",
            "Region": response.get("state_prov"),
            "City": response.get("city"),
            "Postal Code": response.get("zipcode") if response.get("zipcode") else "Not available",
            "Latitude": response.get("latitude"),
            "Longitude": response.get("longitude"),
            "Time Zone": format_timezone(response.get('time_zone')),
            "ISP": response.get("isp"),
            "Organization": response.get("organization"),
            "Domain": response.get("domain") if response.get("domain") else "Not available",
            "ASN": response.get("asn"),
            "Altitude": response.get("altitude") if response.get("altitude") else "Not available",
            "Threat Level": response.get("threat").get("is_tor") if response.get("threat") else "Not available"
        }

        for key, value in ip_info.items():
            if value:
                print(Colorate.Horizontal(Colors.blue_to_cyan, f"{key}: {value}"))

    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"Une erreur s'est produite: {e}"))

def format_timezone(timezone_info):
    if timezone_info:
        return f"{timezone_info.get('name')} (UTC{timezone_info.get('offset')})"
    else:
        return ""

def traceroute_ip(ip_address, max_hops=30, timeout=5):
    try:
        if platform.system().lower() == "windows":
            command = ['tracert', '-h', str(max_hops), '-w', str(timeout * 1000), ip_address]
        else:
            command = ['traceroute', '-m', str(max_hops), '-w', str(timeout), ip_address]
        
        result = subprocess.run(command, capture_output=True, text=True)

        print(Colorate.Horizontal(Colors.blue_to_cyan, f"\n{'=' * 60}\nTRACEROUTE {ip_address}\n{'=' * 60}"))
        print(result.stdout)

    except subprocess.CalledProcessError as cpe:
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"La commande a échoué avec l'erreur: {cpe}"))
    except FileNotFoundError:
        print(Colorate.Horizontal(Colors.blue_to_cyan, "Commande Traceroute introuvable. Veuillez vous assurer qu'il est installé sur votre système."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"Une erreur s'est produite: {e}"))

def reverse_dns_lookup(ip_address, dns_server=None):
    try:
        command = ['nslookup', ip_address]
        if dns_server:
            command.append(dns_server)
        
        result = subprocess.run(command, capture_output=True, text=True)

        print(Colorate.Horizontal(Colors.blue_to_cyan, f"\n{'=' * 60}\RECHERCHE DNS INVERSÉE {ip_address}\n{'=' * 60}"))
        print(result.stdout)

    except subprocess.CalledProcessError as cpe:
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"La commande a échoué avec l'erreur: {cpe}"))
    except FileNotFoundError:
        print(Colorate.Horizontal(Colors.blue_to_cyan, "Commande nslookup introuvable. Veuillez vous assurer qu'il est installé sur votre système."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"Une erreur s'est produite: {e}"))

def scan_port(ip_address, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip_address, port))
        sock.close()
        return port if result == 0 else None
    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"Erreur d'analyse du port {port}: {e}"))
        return None

def port_scan(ip_address, start_port=1, end_port=1024, timeout=1, max_workers=100):
    open_ports = []
    print(Colorate.Horizontal(Colors.blue_to_cyan, f"Analyse des ports sur {ip_address} depuis {start_port} vers {end_port}... Cela peut prendre un peu de temps."))
    
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(scan_port, ip_address, port, timeout): port for port in range(start_port, end_port + 1)}
            for future in concurrent.futures.as_completed(futures):
                port = futures[future]
                if future.result():
                    open_ports.append(port)
                    print(Colorate.Horizontal(Colors.blue_to_cyan, f"Le port {port} est ouvert"))
        
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"\n{'=' * 60}\nPORTS OUVERTS SUR {ip_address}\n{'=' * 60}"))
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"Ports ouverts: {open_ports}"))
    
    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"Une erreur s'est produite lors de l'analyse des ports: {e}"))


def whois_lookup(ip_address):

    try:
        if not re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip_address):
            print(Colorate.Horizontal(Colors.blue_to_cyan, "Format de l'adresse IP invalide."))
            return

        result = whois.whois(ip_address)

        print(Colorate.Horizontal(Colors.blue_to_cyan, f"\n{'=' * 60}\nWHOIS LOOKUP {ip_address}\n{'=' * 60}"))
        
        if result:
            for key, value in result.items():
                if value:
                    if isinstance(value, list):
                        for item in value:
                            print(Colorate.Horizontal(Colors.blue_to_cyan, f"{key}: {item}"))
                    else:
                        print(Colorate.Horizontal(Colors.blue_to_cyan, f"{key}: {value}"))
        else:
            print(Colorate.Horizontal(Colors.blue_to_cyan, "Aucune information WHOIS trouvée pour l'adresse IP."))

    except whois.parser.PywhoisError as e:
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"La recherche WHOIS a échoué: {e}"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"Une erreur s'est produite: {e}"))

def blacklist_check(ip_address):
    try:
        response = requests.get(f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip_address}", headers={
            'Key': '173b1074344847a7968aeee29091c3bea4db13e52eeb78e9f921ba1fe043468bf9d965d63666d411', 
            'Accept': 'application/json'
        }).json()
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"\n{'=' * 60}\nVÉRIFICATION DE LA BLACKLIST {ip_address}\n{'=' * 60}"))
        print(Colorate.Horizontal(Colors.blue_to_cyan, str(response)))
    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"Une erreur s'est produite: {e}"))

def dns_records(ip_address):
    try:
        import dns.resolver
        record_types = ['A', 'MX', 'NS', 'TXT']
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"\n{'=' * 60}\nENREGISTREMENTS DNS {ip_address}\n{'=' * 60}"))

        for record_type in record_types:
            try:
                answers = dns.resolver.resolve(ip_address, record_type)
                for rdata in answers:
                    print(Colorate.Horizontal(Colors.blue_to_cyan, f"{record_type} enregistrement: {rdata}"))
            except dns.resolver.NoAnswer:
                print(Colorate.Horizontal(Colors.blue_to_cyan, f"Aucun enregistrement {record_type} trouvé pour {ip_address}"))
            except dns.resolver.NXDOMAIN:
                print(Colorate.Horizontal(Colors.blue_to_cyan, f"{ip_address} n'existe pas."))
                break
            except Exception as e:
                print(Colorate.Horizontal(Colors.blue_to_cyan, f"Une erreur s'est produite: {e}"))

    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"Une erreur s'est produite: {e}"))

def asn_info(ip_address):
    """
    Obtient des informations sur le système autonome (ASN) associé à une adresse IP donnée.
    
    Args:
        ip_address (str): L'adresse IP cible.
    """
    try:
        response = requests.get(f"https://api.iptoasn.com/v1/as/ip/{ip_address}").json()

        print(Colorate.Horizontal(Colors.blue_to_cyan, f"\n{'=' * 60}\nINFORMATION ASN {ip_address}\n{'=' * 60}"))
        asn_info_to_display = {
            "IP Range": response.get("announced"),
            "ASN": response.get("as_number"),
            "ASN Organization": response.get("as_description"),
            "Country": response.get("country_code"),
            "Created": response.get("allocated") if response.get("allocated") else "Unknown",
            "Last Updated": response.get("updated") if response.get("updated") else "Unknown",
        }

        for key, value in asn_info_to_display.items():
            print(Colorate.Horizontal(Colors.blue_to_cyan, f"{key}: {value}"))

    except requests.RequestException as e:
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"Erreur lors de la récupération des informations ASN: {e}"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"Une erreur s'est produite: {e}"))

def main():
    ascii_art = """
 $$$$$$\\  $$$$$$$\\  $$\\    $$\\  $$$$$$\\  $$\\   $$\\  $$$$$$\\  $$$$$$$$\\ $$$$$$$\\        $$$$$$\\ $$$$$$$\\        $$$$$$$$\\  $$$$$$\\   $$$$$$\\  $$\\        $$$$$$\\ 
$$  __$$\\ $$  __$$\\ $$ |   $$ |$$  __$$\\ $$$\\  $$ |$$  __$$\\ $$  _____|$$  __$$\\       \\_$$  _|$$  __$$\\       \\__$$  __|$$  __$$\\ $$  __$$\\ $$ |      $$  __$$\\ 
$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ /  $$ |$$$$\\ $$ |$$ /  \\__|$$ |      $$ |  $$ |        $$ |  $$ |  $$ |         $$ |   $$ /  $$ |$$ /  $$ |$$ |      $$ /  \\__|
$$$$$$$$ |$$ |  $$ |\\$$\\  $$  |$$$$$$$$ |$$ $$\\$$ |$$ |      $$$$$\\    $$ |  $$ |        $$ |  $$$$$$$  |         $$ |   $$ |  $$ |$$ |  $$ |$$ |      \\$$$$$$\\  
$$  __$$ |$$ |  $$ | \\$$\\$$  / $$  __$$ |$$ \\$$$$ |$$ |      $$  __|   $$ |  $$ |        $$ |  $$  ____/          $$ |   $$ |  $$ |$$ |  $$ |$$ |       \\____$$\\ 
$$ |  $$ |$$ |  $$ |  \\$$$  /  $$ |  $$ |$$ |\\$$$ |$$ |  $$\\ $$ |      $$ |  $$ |        $$ |  $$ |               $$ |   $$ |  $$ |$$ |  $$ |$$ |      $$\\   $$ |
$$ |  $$ |$$$$$$$  |   \\$  /   $$ |  $$ |$$ | \\$$ |\\$$$$$$  |$$$$$$$$\\ $$$$$$$  |      $$$$$$\\ $$ |               $$ |    $$$$$$  | $$$$$$  |$$$$$$$$\\ \\$$$$$$  |
\\__|  \\__|\\_______/     \\_/    \\__|  \\__|\\__|  \\__| \\______/ \\________|\\_______/       \\______|\\__|               \\__|    \\______/  \\______/ \\________| \\______/

        1) Ping IP                  6) Whois Lookup
        2) IP Information           7) Blacklist Check
        3) Traceroute               8) DNS Records
        4) Reverse DNS Lookup       9) ASN Information
        5) Port Scan                10) Exit

    """
    colored_ascii = Colorate.Horizontal(Colors.blue_to_cyan, ascii_art)
    print(Center.XCenter(colored_ascii))
    
    while True:
        option = input(Colorate.Horizontal(Colors.blue_to_cyan, "\nEntrez votre choix: "))

        if option == "1":
            ip_address = input(Colorate.Horizontal(Colors.blue_to_cyan, "Entrez l'adresse IP à ping: "))
            ping_ip(ip_address)
        elif option == "2":
            ip_address = input(Colorate.Horizontal(Colors.blue_to_cyan, "Entrez l'adresse IP pour obtenir des informations: "))
            get_ip_information(ip_address)
        elif option == "3":
            ip_address = input(Colorate.Horizontal(Colors.blue_to_cyan, "Entrez l'adresse IP pour traceroute: "))
            traceroute_ip(ip_address)
        elif option == "4":
            ip_address = input(Colorate.Horizontal(Colors.blue_to_cyan, "Entrez l'adresse IP pour la recherche DNS inversée: "))
            reverse_dns_lookup(ip_address)
        elif option == "5":
            ip_address = input(Colorate.Horizontal(Colors.blue_to_cyan, "Entrez l'adresse IP pour l'analyse des ports: "))
            port_scan(ip_address)
        elif option == "6":
            ip_address = input(Colorate.Horizontal(Colors.blue_to_cyan, "Entrez l'adresse IP pour la recherche whois: "))
            whois_lookup(ip_address)
        elif option == "7":
            ip_address = input(Colorate.Horizontal(Colors.blue_to_cyan, "Entrez l'adresse IP pour la vérification de la blacklist: "))
            blacklist_check(ip_address)
        elif option == "8":
            ip_address = input(Colorate.Horizontal(Colors.blue_to_cyan, "Entrez l'adresse IP pour les enregistrements DNS: "))
            dns_records(ip_address)
        elif option == "9":
            ip_address = input(Colorate.Horizontal(Colors.blue_to_cyan, "Entrez l'adresse IP pour les informations ASN: "))
            asn_info(ip_address)
        elif option == "10":
            print(Colorate.Horizontal(Colors.blue_to_cyan, "Quitter le programme..."))
            break
        else:
            print(Colorate.Horizontal(Colors.blue_to_cyan, "Option invalide. Veuillez choisir un nombre de 1 à 10."))

if __name__ == "__main__":
    main()