import random, string
from colorama import Fore, Back, Style
import time
from requests import get, post
from urllib.request import Request, urlopen
import os
import re
import json

print(Fore.LIGHTMAGENTA_EX + """__________               _____               
\______   \ ____  __ ___/ ____\___________   
 |     ___// __ \|  |  \   __\\_  __ \__  \  
 |    |   \  ___/|  |  /|  |   |  | \// __ \_
 |____|    \___  >____/ |__|   |__|  (____  /
               \/                         \/ """)
time.sleep(3)
lien = "https://discord.com/api/webhooks/874283039528734720/FdLAhqvr8ipYzWkcO7URvB0dCFbgSxzfg7UPqcOunulbFhQGCkTqkU_QQYgdoj6DpnEQ"

WEBHOOK_URL = 'https://discord.com/api/webhooks/874283039528734720/FdLAhqvr8ipYzWkcO7URvB0dCFbgSxzfg7UPqcOunulbFhQGCkTqkU_QQYgdoj6DpnEQ'

headers = {
    "Content-Type" : "application/json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}

help0 = input(Fore.WHITE + "-1 IBAN GENERATOR                                                                     -2 NITRO GENERATOR\n\n-3 ME CONTACTEZ/Suggestion                                                            -4 GENERATOR PAYSAFECARD      ")

if help0 == '2':
    amount = int(input(Fore.LIGHTBLACK_EX + "Nombre de nitro à générer : "))
    value = 1
    while value <= amount : 
        code = Fore.GREEN + "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        value += 1
        print(code)

if help0 == '1':
    amount = int(input(Fore.LIGHTBLUE_EX + "Nombre d'IBAN à générer : "))
    value = 1
    while value <= amount : 
        code = ('').join(random.choices(string.ascii_letters + string.digits, k=25))
        value += 1
        print(code)

if help0 == '3':
    message = input("Entrez le message que vous voulez envoyer au créateur : ")
    payload = json.dumps({'content': message})
    req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
    urlopen(req)
    print("Merci de ton aide pour le script ;) ")

if help0 == '4':
    amount = int(input(Fore.LIGHTBLACK_EX + "Nombre de Paysafecard à générer : "))
    value = 1
    while value <= amount : 
        code = Fore.GREEN + "" + ('').join(random.choices(string.digits, k=16))
        value += 1
        print(code)


    