import random
import requests
import socket
import time,pyfiglet
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
E = "\033[0;90m" #رمادي
lo=pyfiglet.figlet_format('H S O')
print(B+lo)
print(X+'*'*60)

ID = input(B+' 2083203755 : '+F)
token= input(B+' 6806056786:AAHaiz8hqzcikvbx-Ry-i2iEotEcwV4rfAw : '+F)
print('\n')
na = 'QWERTYUIOPLKJHGFDSAMNBVCXZ'

def check_user(username):
    try:
         url = requests.get(f'https://t.me/{username}').text
         if 'tgme_username_link' in url:
         	print(f'\033[1;32m good user -->: {username}')
         	tlg = f'''
تم صيد يوزر جديد
usrrname = @{username}
________________________
HSO = @MM3_g +@termuxpp	
انضم هنا ياعزيزي سوف نشر المزيد
         	'''
         	
         	requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))
         else:
         	print(f'\033[1;31m erorr user -->: {username}')
    except (requests.exceptions.RequestException, socket.timeout):
            print(f'\033[1;33m فصل النت انتضر خمس ثواني ')
            time.sleep(5)
            check_user(username)

while True:
    u = str(''.join(random.choice(na) for i in range(1)))
    us = str(''.join(random.choice(na) for i in range(1)))
    
    user = u+u+us+u+u    
    
    
    
    
    
    
    
    
    check_user(user)