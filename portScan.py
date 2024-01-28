import socket
from colorama import Fore,Style

banner = Fore.LIGHTMAGENTA_EX+"""

 ▄▄▄·      ▄▄▄  ▄▄▄▄▄    .▄▄ ·  ▄▄·  ▄▄▄·  ▐ ▄  ▐ ▄ ▄▄▄ .▄▄▄  
▐█ ▄█▪     ▀▄ █·•██      ▐█ ▀. ▐█ ▌▪▐█ ▀█ •█▌▐█•█▌▐█▀▄.▀·▀▄ █·
 ██▀· ▄█▀▄ ▐▀▀▄  ▐█.▪    ▄▀▀▀█▄██ ▄▄▄█▀▀█ ▐█▐▐▌▐█▐▐▌▐▀▀▪▄▐▀▀▄ 
▐█▪·•▐█▌.▐▌▐█•█▌ ▐█▌·    ▐█▄▪▐█▐███▌▐█ ▪▐▌██▐█▌██▐█▌▐█▄▄▌▐█•█▌
.▀    ▀█▄▀▪.▀  ▀ ▀▀▀      ▀▀▀▀ ·▀▀▀  ▀  ▀ ▀▀ █▪▀▀ █▪ ▀▀▀ .▀  ▀
                                          
                                          Coded by: BaverTorun
                                          Github: github.com/bavertorun
"""
print(banner)

def tcpScan(ip, startPort, endPort):
    for port in range(startPort, endPort + 1):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if not tcp.connect_ex((ip, port)):
                print(Fore.LIGHTCYAN_EX+f"[+] {ip}:{port}/TCP Open")
                tcp.close()
        except Exception:
            pass


def scanHost(ip, startPort, endPort):
    print(Fore.LIGHTBLACK_EX+f"[*] Starting TCP port scan on host {ip}")
    # Begin TCP scan on host
    tcpScan(ip, startPort, endPort)
    print(Fore.LIGHTBLACK_EX+f"[*] TCP scan on host {ip} complete"+ Style.RESET_ALL)



def main():
    socket.setdefaulttimeout(0.01)
    ip = input(Fore.LIGHTMAGENTA_EX+'Enter ip adress -> ')
    startPort = int(input(Fore.LIGHTMAGENTA_EX+'Enter Start Port ->'))
    endPort = int(input(Fore.LIGHTMAGENTA_EX+'Enter End Port ->'))
    scanHost(ip,startPort,endPort)


main()
