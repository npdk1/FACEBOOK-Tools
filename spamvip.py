import requests, sys
from time import sleep
from datetime import datetime, timedelta
import os

try:
    import requests, colorama, prettytable
except:
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install prettytable")

# Colors
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'

def banner():
    banner = '''
\033[1;35m██████╗ ░█████╗ ███╗░░██╗░██████╗      ██████╗ ██╗░░██╗ ██████╗ ░█████╗
\033[1;36m██╔══██╗██╔══██╗████╗░██║██╔════╝     ██╔═══██╗██║░░██║██╔════╝██╔══██╗
\033[1;34m██║░░██║███████║██╔██╗██║██║░░███╗    ██║░░░██║███████║██║░░░░░███████║
\033[1;37m██║░░██║██╔══██║██║╚████║██║░░░██║    ██║░░░██║██╔══██║██║░░░░░██╔══██║
\033[1;33m██████╔╝██║░░██║██║░╚███║╚██████╔╝    ╚██████╔╝██║░░██║╚██████╗██║░░██║
\033[1;32m╚═════╝ ╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝      ╚═════╝ ╚═╝░░╚═╝ ╚═════╝╚═╝░░╚═╝
'''
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00125)

os.system("cls" if os.name == "nt" else "clear")
banner()

print("- \033[1;37m - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print(" \033[1;37m╔═════════════════════════════════════════════════════════════")
print("\033[1;32m ║ ➣Chức Năng [1] \033[1;36mNhây Có Dấu")
print(" \033[1;37m║═════════════════════════════════════════════════════════════")   
print("\033[1;32m ║ ➢Chức năng [2] \033[1;36mNhây Không Dấu")
print(" \033[1;37m║═════════════════════════════════════════════════════════════")                                                          
print("\033[1;32m ║ ➣Chức năng [3] \033[1;36mNhây Réo Tên")
print(" \033[1;37m║═════════════════════════════════════════════════════════════")
print("\033[1;32m ║ ➢Chức năng [4] \033[1;36mTreo Spam Messenger | để 10s hoặc 20s |")
print("\033[1;37m ║═════════════════════════════════════════════════════════════")
print("\033[1;32m ║ ➣Chức năng [5] \033[1;36mNhây Code Lag")                               
print(" \033[1;37m║═════════════════════════════════════════════════════════════")                                                          
print("\033[1;32m ║ ➢Chức năng [6] \033[1;36mTreo Sớ")
print(" \033[1;37m║═════════════════════════════════════════════════════════════")   
print("\033[1;32m ║ ➣Chức năng [7] \033[1;36mNhây Discord")
print(" \033[1;37m╚═════════════════════════════════════════════════════════════")

chon = int(input('\033[1;31m[\033[1;37m[=.=]\033[1;31m] \033[1;37m=> \033[1;32mChọn chức năng \033[1;37m: \033[1;33m'))

if chon == 1:
    exec(requests.get('https://taokey567.c25tool.net/war/war1.php').text)
elif chon == 2:
    exec(requests.get('https://taokey567.c25tool.net/war/war2.php').text)
elif chon == 3:
    exec(requests.get('https://taokey567.c25tool.net/war/war3.php').text)
elif chon == 4:
    exec(requests.get('https://taokey567.c25tool.net/war/war4.php').text)
elif chon == 5:
    exec(requests.get('https://taokey567.c25tool.net/war/war5.php').text)
elif chon == 6:
    exec(requests.get('https://taokey567.c25tool.net/war/war6.php').text)
elif chon == 7:
    exec(requests.get('https://taokey567.c25tool.net/war/war7.php').text)
else:
    print(" Sai Lựa Chọn ")
    exit()