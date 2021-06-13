from urllib.parse import quote
from requests.api import request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json
import random
import string
import sys

s_v_web_id = "verify_kptzi8io_WP4o6YuC_L0Xe_46FC_Ao4b_EL1QHYBiNlMo"
did = "".join([random.choice(string.digits) for num in range(19)])

def get_verify():
    global s_v_web_id
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path='C:\webdriver\chromedriver.exe', options=chrome_options)
        driver.get('https://www.tiktok.com/@officialtrans7?lang=en')

        s_v_web_id = json.loads(json.dumps(driver.get_cookie(name="s_v_web_id")))['value']

        driver.quit()
        return None
    except:
        driver.quit()
        sys.exit()

def get_cookie():
    cookie = {
        "tt_webid_v2": did,
        "tt_webid": did,
        "s_v_web_id": s_v_web_id
    }
    return cookie

def get_user(username):
    cookie = get_cookie()
    r = requests.get(
        "https://tiktok.com/@{}?lang=en".format(quote(username)),
        headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "authority": "www.tiktok.com",
            "path": "/@{}".format(quote(username)),
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Host": "www.tiktok.com",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        }, cookies=cookie
    )
    html = r.text
    nonce_start = '<head nonce="'
    nonce_end = '">'
    nonce = html.split(nonce_start)[1].split(nonce_end)[0]
    j_raw = html.split(
        '<script id="__NEXT_DATA__" type="application/json" nonce="%s" crossorigin="anonymous">'
        % nonce
    )[1].split("</script>")[0]
    user = json.loads(j_raw)["props"]["pageProps"]["userInfo"]["user"]
    
    return user

def get_post(client, secUid, count, cursor):
    params = {
        "aid": "1988",
        "app_name": "tiktok_web",
        "device_platform": "web_mobile",
        "device_id": did,
        "region": "ID",
        "priority_region": "ID",
        "os": "android",
        "referer": "",
        "root_referer": "https://www.tiktok.com/",
        "cookie_enabled": "true",
        "screen_width": "400",
        "screen_height": "538",
        "browser_language": "en-US",
        "browser_platform": "Win32",
        "browser_name": "Mozilla",
        "browser_version": "5.0+(Linux;+Android+6.0;+Nexus+5+Build/MRA58N)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/91.0.4472.77+Mobile+Safari/537.36",
        "browser_online": "true",
        "verifyFp": s_v_web_id,
        "app_language": "en",
        "timezone_name": "Asia/Jakarta",
        "is_page_visible": "true",
        "focus_state": "true",
        "is_fullscreen": "false",
        "history_len": "7",
        "battery_info": "1",
        "secUid": secUid,
        "count": count,
        "cursor": cursor,
        "language": "en",
        "_signature": "_02B4Z6wo00f01mh1.-gAAIDAtDGCmUC1phZoZftAAProe8"
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'Host': 't.tiktok.com',
        'Origin': 'https:/www.tiktok.com',
        'Referer': 'https:/www.tiktok.com/',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36'
    }

    result = json.loads(client.get(
        url='https://t.tiktok.com/api/post/item_list/',
        params=params,
        headers=headers,
        cookies=get_cookie()
    ).text)

    return result

lompat = []
if __name__ == "__main__":
    percobaan = 0
    targets = ["republikaonline","tvonenews","antvnews","radioelshinta","kemdikbud.ri","narasi","kemkominfo","kemenkesri","kementerianesdm","kemensosri","kkp.go.id","kemenristekdikti","kemenpppa","kemenpupr","kemenparekraf","kemenkeuri","kemenpora_ri","kemenkomarves","kementerianesdm","mata.najwa"]
    for target in targets:
        user = get_user(target)
        # percobaan = 0
        postke = 0
        posts = []
        try:
            hasMore = True
            count = 30
            cursor = 0
            while hasMore:
                # with requests.Session() as client:
                result = get_post(client=requests ,secUid=user['secUid'], count=count, cursor=cursor)
                for item in result['itemList']:
                    posts.append(item)
                    postke += 1
                    print('\npost ke --> '+str(postke)+'\npercobaan ke --> '+str(percobaan)+'\n')

                hasMore = result['hasMore']
                cursor = result['cursor']
                percobaan += 1
        except:
            print('berhenti setelah percobaan ke-' + str(percobaan))
            print(target)
            # lompat.append(target)
            # continue
            sys.exit()

        if len(posts) != 0: 
            with open('tiktok_'+target+'.json', 'w') as save_as:
                save_as.write(json.dumps({
                    "tiktok_"+target: posts
                }))
            print("\n"+"-"*50+"\n|| Successfully Saved Data To 'tiktok_"+target+".json'"+"\n"+"-"*50+"\n")
        else:
            sys.exit()
    print(lompat)