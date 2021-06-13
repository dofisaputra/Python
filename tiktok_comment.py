import requests
import json
import random
import string

s_v_web_id = "verify_a51a833bd51eabc17a45fd3b14f9356d"
sessionid_ss = "6c8b1089aeac46ce1c1a2422a09e3a2f"
did = "".join([random.choice(string.digits) for num in range(19)])

def get_comments(username, aweme_id, cursor, count):
    cookies = {
        "tt_webid_v2": did,
        "tt_webid": did,
        "sessionid_ss": sessionid_ss
    }

    headers = {
        'authority': 'www.tiktok.com',
        'accept': 'application/json, text/plain, */*',
        'referer': 'https://www.tiktok.com/@{}/video/{}?is_copy_url=1&is_from_webapp=v1'.format(username, aweme_id),
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36'
    }

    params = {
        "aid": "1988",
        "app_name": "tiktok_web",
        "device_platform": "web_mobile",
        "device_id": did,
        "verifyFp": s_v_web_id,
        "aweme_id": aweme_id,
        "cursor": cursor,
        "count": count
    }
    
    response = requests.get(url='https://www.tiktok.com/api/comment/list/', params=params, headers=headers, cookies=cookies)
    return json.loads(response.text)

cursor = 0
comment_count = 0
while cursor < 200:
    comments = get_comments(username='cowcowofficial', aweme_id='6941679739094519041', cursor=cursor, count=50)
    print(comments)
    cursor = comments['cursor']
    comment_count += len(comments['comments'])
    print(cursor)
print(comment_count)