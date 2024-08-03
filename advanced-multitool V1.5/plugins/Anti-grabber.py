import os
import re
from pystyle import Colors, Colorate, System

os.system("cls")

WEBHOOK_PATTERN = re.compile(r'https://discord(app)?\.com/api/webhooks/\d+/[a-zA-Z0-9_-]+')
found = False
GRABBER_PATTERNS = {
    re.compile(r'import http.client'): 'Importation de la bibliothèque http.client, utilisée pour les requêtes HTTP.',
    re.compile(r'socket.socket'): 'Utilisation de sockets réseau, peut être utilisé pour la communication réseau.',
    re.compile(r'os.system'): 'Exécution de commandes système via os.system.',
    re.compile(r'os.environ'): 'Accès aux variables d\'environnement via os.environ.',
    re.compile(r'os.popen'): 'Exécution de commandes système via os.popen.',
    re.compile(r'subprocess.run'): 'Exécution de commandes système via subprocess.run.',
    re.compile(r'subprocess.Popen'): 'Exécution de commandes système via subprocess.Popen.',
    re.compile(r'base64.b64decode'): 'Décodage de données en base64, souvent utilisé pour encoder des données sensibles.',
    re.compile(r'str.encode\("base64"\)'): 'Encodage de chaînes en base64.',
    re.compile(r'json.dumps\('): 'Sérialisation de données en JSON.',
    re.compile(r'json.loads\('): 'Désérialisation de données JSON.',
    re.compile(r'platform.system\('): 'Récupération d\'informations sur le système d\'exploitation.',
    re.compile(r'platform.release\('): 'Récupération d\'informations sur la version du système d\'exploitation.',
    re.compile(r'shutil.copyfile\('): 'Copie de fichiers via shutil.copyfile.',
    re.compile(r'open\('): 'Ouverture de fichiers, potentiellement pour la lecture/écriture de données sensibles.',
    re.compile(r'os.getenv\(') :'Lecture de variable système, potentiellement pour accéder au Appdata.',
    re.compile(r'exec\('): 'Execution de code via une variable, potentiellement pour cacher un grabber.',
    re.compile(r'\[\\w-]\{24}\\.\[\\w-]\{6}\\.\[\\w-]\{25,110}'): 'Regular expression de token discord, pour trouver des tokens dans des fichiers.',
    re.compile(r'taskkill') : 'Mot clé : "taskkill", utiliser pour fermer des applications par la console.'
}

def scan_content(content):
    findings = []
    lines = content.splitlines()
    for line_number, line in enumerate(lines, start=1):
        if WEBHOOK_PATTERN.search(line):
            findings.append((line_number, 'Discord webhook'))
        for pattern, description in GRABBER_PATTERNS.items():
            if pattern.search(line):
                findings.append((line_number, f'Grabber pattern: {description}'))
    return findings

def scan_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return scan_content(content)

def scan_directory(directory):
    global found
    report = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                findings = scan_file(file_path)
                if findings:
                    report[file_path] = findings
                    found = True
    return report

def generate_report(scan_results, output_file=None):
    webhook_found = False
    grabber_found = False
    report_lines = []

    for file_path, findings in scan_results.items():
        report_lines.append(Colorate.Horizontal(Colors.blue_to_cyan, f"File: {file_path}"))
        for line_number, finding in findings:
            color = Colors.red_to_yellow if 'Discord webhook' in finding else Colors.white_to_blue
            report_lines.append(Colorate.Horizontal(color, f"  Line {line_number}: {finding}"))
            if 'Discord webhook' in finding:
                webhook_found = True
            if 'Grabber pattern' in finding:
                grabber_found = True

    if webhook_found or grabber_found:
        if webhook_found:
            report_lines.append(Colorate.Horizontal(Colors.red_to_yellow, "Un webhook Discord a été trouvé."))
        if grabber_found:
            report_lines.append(Colorate.Horizontal(Colors.red_to_yellow, "Un grabber a été trouvé."))
    else:
        report_lines.append(Colorate.Horizontal(Colors.green_to_blue, "Aucun grabber ni webhook trouvé."))
    
    report = "\n".join(report_lines)
    
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(Colorate.Horizontal(Colors.blue_to_green, f"Rapport sauvegardé dans le fichier {output_file}"))
    else:
        print(report)

def print_ascii_art():
    ascii_art = r"""
 $$$$$$\  $$$$$$$\  $$\    $$\  $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$$\ $$$$$$$\         $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$\        $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$$\  $$$$$$$\  $$$$$$$$\ $$$$$$$\  
$$  __$$\ $$  __$$\ $$ |   $$ |$$  __$$\ $$$\  $$ |$$  __$$\ $$  _____|$$  __$$\       $$  __$$\ $$$\  $$ |\__$$  __|\_$$  _|      $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  _____|$$  __$$\ 
$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|$$ |      $$ |  $$ |      $$ /  $$ |$$$$\ $$ |   $$ |     $$ |        $$ /  \__|$$ |  $$ |$$ /  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |
$$$$$$$$ |$$ |  $$ |\$$\  $$  |$$$$$$$$ |$$ $$\$$ |$$ |      $$$$$\    $$ |  $$ |      $$$$$$$$ |$$ $$\$$ |   $$ |     $$ |        $$ |$$$$\ $$$$$$$  |$$$$$$$$ |$$$$$$$\ |$$$$$$$\ |$$$$$\    $$$$$$$  |
$$  __$$ |$$ |  $$ | \$$\$$  / $$  __$$ |$$ \$$$$ |$$ |      $$  __|   $$ |  $$ |      $$  __$$ |$$ \$$$$ |   $$ |     $$ |        $$ |\_$$ |$$  __$$< $$  __$$ |$$  __$$\ $$  __$$\ $$  __|   $$  __$$< 
$$ |  $$ |$$ |  $$ |  \$$$  /  $$ |  $$ |$$ |\$$$ |$$ |  $$\ $$ |      $$ |  $$ |      $$ |  $$ |$$ |\$$$ |   $$ |     $$ |        $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |
$$ |  $$ |$$$$$$$  |   \$  /   $$ |  $$ |$$ | \$$ |\$$$$$$  |$$$$$$$$\ $$$$$$$  |      $$ |  $$ |$$ | \$$ |   $$ |   $$$$$$\       \$$$$$$  |$$ |  $$ |$$ |  $$ |$$$$$$$  |$$$$$$$  |$$$$$$$$\ $$ |  $$ |
\__|  \__|\_______/     \_/    \__|  \__|\__|  \__| \______/ \________|\_______/       \__|  \__|\__|  \__|   \__|   \______|       \______/ \__|  \__|\__|  \__|\_______/ \_______/ \________|\__|  \__|
                                                     
    """
    System.Clear()
    print(Colorate.Vertical(Colors.blue_to_cyan, ascii_art))

def print_loading_animation(message, duration):
    import time
    from itertools import cycle

    for frame in cycle(['.  ', '.. ', '...']):
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"\r{message}{frame}"), end="")
        time.sleep(0.5)
        duration -= 0.5
        if duration <= 0:
            break
    print()

def main():
    print_ascii_art()
    directory_to_scan = input(Colorate.Horizontal(Colors.blue_to_cyan, "Veuillez entrer le chemin du répertoire à scanner : "))
    if os.path.isdir(directory_to_scan):
        scan_results = scan_directory(directory_to_scan)
        output_file = input(Colorate.Horizontal(Colors.blue_to_cyan, "Entrez le chemin du fichier pour sauvegarder le rapport (ou appuyez sur Entrée pour l'afficher à l'écran) : "))
        System.Clear()
        generate_report(scan_results, output_file if output_file else None)
    else:
        print(Colorate.Horizontal(Colors.red_to_yellow, "Le répertoire spécifié n'existe pas."))
    input(f"\nPress ENTER to exit...")


if __name__ == "__main__":
    main()
