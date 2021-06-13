import requests
from requests.api import options
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time

BASE_URL = 'https://www.tiktok.com'

def scroll_down(driver, count):
    post_count = 30
    print('\n|| post estimate --> {}-{}\n'.format(post_count-30, post_count))
    last_height = driver.execute_script("return document.body.scrollHeight")
    if count == 0:
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            post_count += 30
            print('\n|| post estimate --> {}-{}\n'.format(post_count-30, post_count))

    else:
        repeat = 30
        while count > repeat:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            repeat += 30
            post_count += 30
            print('\n|| post count --> {}\n'.format(post_count-30, post_count))


def get_request(value, count):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--log-level=3")
        driver = webdriver.Chrome(executable_path='C:\webdriver\chromedriver.exe', options=chrome_options)
        print('\n'+'-'*29+'\n|| Lets Start Scraping! :D ||\n'+'-'*29+'\n')

        url = ""
        api_url = ""
        if '#' in value:
            url = BASE_URL+'/tag/{}'.format(value.replace('#', ''))
            api_url = 'https://t.tiktok.com/api/challenge/item_list/?aid'
        else:
            url = BASE_URL+'/@{}?lang=en'.format(value)
            api_url = 'https://t.tiktok.com/api/post/item_list/?aid'

        driver.get(url=url)
        scroll_down(driver=driver, count=count)
        list_request = []
        for x in driver.requests:
            if api_url in str(x):
                request = {
                    "api_url": x.url,
                    "headers": {
                        "User-Agent": x.headers['User-Agent'],
                        "x-secsdk-csrf-token": x.headers['x-secsdk-csrf-token']
                    }
                }
                list_request.append(request)

        driver.quit()
        return list_request

    except:
        driver.quit()
        print('failed to load selenium')
    
def get_post(target, count=0):
    list_request = get_request(value=target, count=count)
    list_post = []
    for request in list_request:
        response = requests.get(url=request['api_url'], headers=request['headers'])
        for post in json.loads(response.text)['itemList']:
            print(post)
            list_post.append(post)
    
    return list_post
        
targets = ["detikcom"]
for target in targets:
    print(len(get_post(target=target)))

    break
