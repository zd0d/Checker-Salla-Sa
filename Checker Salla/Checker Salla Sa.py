import os

os.system('cls' if os.name == 'nt' else 'clear')

import requests
import time

ban = '''
[!] Follow Me In Instagram : @680068
   _____         _      _                  _____         
  / ____|  /\   | |    | |        /\      / ____|  /\    
 | (___   /  \  | |    | |       /  \    | (___   /  \   
  \___ \ / /\ \ | |    | |      / /\ \    \___ \ / /\ \  
  ____) / ____ \| |____| |____ / ____ \   ____) / ____ \ 
 |_____/_/    \_\______|______/_/    \_\ |_____/_/    \_\
    

              Coded by | @680068                                    
'''


print(ban)



ban2 = '''
   _____         _      _                  _____         
  / ____|  /\   | |    | |        /\      / ____|  /\    
 | (___   /  \  | |    | |       /  \    | (___   /  \   
  \___ \ / /\ \ | |    | |      / /\ \    \___ \ / /\ \  
  ____) / ____ \| |____| |____ / ____ \   ____) / ____ \ 
 |_____/_/    \_\______|______/_/    \_\ |_____/_/    \_\
 
                                               
'''

time.sleep(1)

print(" ")


input("- Press Enter To Start ...")

time.sleep(1)

username = 'user.txt'

use = username

file = open(username, "r")

headers = {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'cookie': '__cfduid=dea4e021f08a1641b9d2279676ade6aff1611767846; __cf_bm=3537e7c7b4b8234655d050a157427d0c8ffde99f-1611767862-1800-AUB5XSeMgBltyt6QrjGmnsY62zngGs69eczQoLy7mtKAgzn6sqSYp+PP9hqYgZC532lTkUaky6q3PK9E1BpEqptar0dPpMvyeNWPZ/7chujykk1zxAv3Op7+CRRG1+Xplw==; XSRF-TOKEN=eyJpdiI6IjZ0aENUdW1HTVFGY2xzV3BJam1iblE9PSIsInZhbHVlIjoibCtLSjlDRXBuNmhzMGF2K1pqSFdjWG9Ua2lQeElyTVdQcjlWT1RQZFpIYUREWFN2ekhsendud2haOTJDN01NcCIsIm1hYyI6IjIwYjViODlhMzJlNmQ2ZTE4MWRiYzI0NjI1Mjk4ZmE0MmFmZjk0ODczOGUwN2NhOTJlZDdjZjEyNDc2MjhjMzQifQ%3D%3D; sss=eyJpdiI6IlNjY3JpTlVtM2piVDlvRW13c2V0anc9PSIsInZhbHVlIjoiUGhLZUEwMjI2djRKcFpGZ0h1Y3l3a3B1S3VmOStmaXBCRzFaRkF2YmJsR29KZ2ZuRVZmTlhWQTBTcE0yWng5cSIsIm1hYyI6ImFlZDkzNWQwNzk2OWVkYmQ0NDUxNjdhNmJjNWNjMzgwMGI0Y2Y5MTA0NDMzODU1NjhiZmM1MDFlNDg1NTg0NDIifQ%3D%3D',
'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not\\A\"Brand";v="99"',
'sec-ch-ua-mobile': '?1',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Mobile Safari/537.36',
}

file = open(username, "r")

av = 0
tk = 0
while True:
  user = file.readline().split('\n')[0]
  url = f'https://salla.sa/{user}'
  rq = requests.get(url, headers=headers)
  if (user == ""):
    print("")
    input("- Done, Press Enter To Close Program ...")
    exit(0)


  if rq.status_code == 200:
      tk +=1
      os.system('cls' if os.name == 'nt' else 'clear')
      print(f'{ban2}\n- Starting Checker By @berlin.py -\n\n=============================\n\n[+] Available User : [   ]\n\n[-] Avilable : {av}\n\n[-] Taken : {tk}\n\n[+] Taken User : [{user}]\n\n=============================')


  else:
      av +=1
      os.system('cls' if os.name == 'nt' else 'clear')
      print(f'{ban2}\n- Starting Checker By @berlin.py -\n\n=============================\n\n[+] Available User : [{user}]\n\n[-] Avilable : {av}\n\n[-] Taken : {tk}\n\n[+] Taken User : [   ]\n\n=============================')
      with open('userfound.txt', 'a') as x:
                x.write(user + '\n')


