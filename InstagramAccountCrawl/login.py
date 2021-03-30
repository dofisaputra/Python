import json
import re
import requests
import sys
from datetime import datetime
from account import username,password

class InstagramLogin():
    link = "https://www.instagram.com/accounts/login/"
    login_url = "https://www.instagram.com/accounts/login/ajax/"
    time = int(datetime.now().timestamp())
    csrf = ""
    with requests.Session() as req:
        x = req.get(url=link, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
        csrf = re.findall(r"csrf_token\":\"(.*?)\"", x.text)[0]
    payload = {
        "username": username,
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{time}:"+password,
        "queryParams": {},
        "optIntoOneTap": "false"
    }
    login_header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf
    }
    def Login(self):
        req = requests.Session()
        s = req.post(url=self.login_url, data=self.payload, headers=self.login_header)
        response = json.loads(s.text)
        if "authenticated" in response:
            if response["authenticated"]:
                print("\n"+"-"*25+"\n|| Login Successful!"+"\n"+"-"*25+"\n")
                return req
            else:
                print("\n"+response+"\n")
                sys.exit()
        else:
            print("\n"+response+"\n")
            sys.exit()