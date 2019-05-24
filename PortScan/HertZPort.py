import socket
import sys, os

menu = r"""
$$\   $$\                      $$\     $$$$$$$$\ $$$$$$$\                       $$\     
$$ |  $$ |                     $$ |    \____$$  |$$  __$$\                      $$ |    
$$ |  $$ | $$$$$$\   $$$$$$\ $$$$$$\       $$  / $$ |  $$ | $$$$$$\   $$$$$$\ $$$$$$\   
$$$$$$$$ |$$  __$$\ $$  __$$\\_$$  _|     $$  /  $$$$$$$  |$$  __$$\ $$  __$$\\_$$  _|  
$$  __$$ |$$$$$$$$ |$$ |  \__| $$ |      $$  /   $$  ____/ $$ /  $$ |$$ |  \__| $$ |    
$$ |  $$ |$$   ____|$$ |       $$ |$$\  $$  /    $$ |      $$ |  $$ |$$ |       $$ |$$\ 
$$ |  $$ |\$$$$$$$\ $$ |       \$$$$  |$$$$$$$$\ $$ |      \$$$$$$  |$$ |       \$$$$  |
\__|  \__| \_______|\__|        \____/ \________|\__|       \______/ \__|        \____/ 
                            
                            Feito Por: HertZ Programmer!


"""

os.system('cls')
os.system('color 4')
def scanner(ip, menu):
    portas_encontradas = []
    print(menu + '[WARNING] - HertZScan Iniciado!\n\n')
    if 'https' or 'http' in ip:
        sobre_ip = ip.strip('https:/')
        ip = socket.gethostbyname(sobre_ip)

    for ports in range(0, 3306):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp                                  
        client.settimeout(0.03)
        code = client.connect_ex((ip, ports))
        if code == 0:
            portas_encontradas.append(ports)
            print("[STATUS] - Porta %s ABERTA!!\n"%ports)
        else:
            pass
    print("[ => ] HertZScan Finalizado!\n\n")
    print("[ ! ] Total Portas [ABERTAS] - %s"%portas_encontradas)

if len(sys.argv) < 2:
    print("Modo De Uso: \npy HertZPort.py 127.0.0.1\n\n#######")
else:

    ip = sys.argv[1]
    scanner(ip, menu)                             