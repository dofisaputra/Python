import json
from datetime import datetime
from dateutil import parser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

file = open('/home/ebdesk/Music/username_target.json')
data = json.load(file)

result = []

driver = webdriver.Chrome()

test = 0
try:
    for x in data['hits']['hits']:
        # if test < 10:
        username = x['_source']['username']

        driver.get('https://twitter.com/'+str(username))
        wait = WebDriverWait(driver, 2)
        try:
            try:
                account_suspended = wait.until(lambda driver: driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > div > div > div.css-1dbjc4n.r-14lw9ot.r-mxfbl1.r-1efd50x.r-5kkj8d.r-d9fdf6.r-10x3wzx > div.css-901oao.r-18jsvk2.r-1qd0xha.r-adyw6z.r-b88u0q.r-135wba7.r-6gpygo.r-bcqeeo.r-q4m81j.r-qvutc0 > span"))
                result.append({
                    'username': username,
                    'status': 'suspended',
                    'last_post_link': None,
                    'last_active': None
                })
                print('suspend')

            except:
                try:
                    pinned = wait.until(lambda driver: driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-1gm7m50.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div:nth-child(2) > div > div > div:nth-child(3) > section > div > div > div:nth-child(1) > div > div > article > div > div > div > div:nth-child(1) > div > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox > div > div > div > span"))
                    print(pinned.text)
                    last_post_linkk = wait.until(lambda driver: driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-1gm7m50.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div:nth-child(2) > div > div > div:nth-child(3) > section > div > div > div:nth-child(3) > div > div > article > div > div > div > div.css-1dbjc4n.r-18u37iz > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu > div:nth-child(1) > div > div.css-1dbjc4n.r-k4xj1c.r-18u37iz.r-1wtj0ep > div.css-1dbjc4n.r-1d09ksm.r-18u37iz.r-1wbh5a2 > a")).get_attribute('href')
                    last_activee = wait.until(lambda driver: driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-1gm7m50.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div:nth-child(2) > div > div > div:nth-child(3) > section > div > div > div:nth-child(3) > div > div > article > div > div > div > div.css-1dbjc4n.r-18u37iz > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu > div:nth-child(1) > div > div.css-1dbjc4n.r-k4xj1c.r-18u37iz.r-1wtj0ep > div.css-1dbjc4n.r-1d09ksm.r-18u37iz.r-1wbh5a2 > a > time")).get_attribute('datetime')
                    dateee = parser.isoparse(str(last_active))
                    date_finall = dateee.strftime("%B %d, %Y (%H:%M:%S)")
                    result.append({
                        'username': username,
                        'status': 'active',
                        'last_post_link': last_post_linkk,
                        'last_active': date_finall
                    })
                except:
                    last_post_link = wait.until(lambda driver: driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > div > div > div:nth-child(3) > section > div > div > div:nth-child(1) > div > div > article > div > div > div > div.css-1dbjc4n.r-18u37iz > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu > div:nth-child(1) > div > div.css-1dbjc4n.r-k4xj1c.r-18u37iz.r-1wtj0ep > div.css-1dbjc4n.r-1d09ksm.r-18u37iz.r-1wbh5a2 > a")).get_attribute('href')
                    last_active = wait.until(lambda driver: driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-1gm7m50.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div:nth-child(2) > div > div > div:nth-child(3) > section > div > div > div:nth-child(1) > div > div > article > div > div > div > div.css-1dbjc4n.r-18u37iz > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu > div:nth-child(1) > div > div.css-1dbjc4n.r-k4xj1c.r-18u37iz.r-1wtj0ep > div.css-1dbjc4n.r-1d09ksm.r-18u37iz.r-1wbh5a2 > a > time")).get_attribute('datetime')
                    datee = parser.isoparse(str(last_active))
                    date_final = datee.strftime("%B %d, %Y (%H:%M:%S)")
                    result.append({
                        'username': username,
                        'status': 'active',
                        'last_post_link': last_post_link,
                        'last_active': date_final
                    })

            test += 1
            print(test)
        except:
            result.append({
                'username': username,
                'status': 'active',
                'last_post_link': 'not found',
                'last_active': 'not found'
            })
            test += 1
            print(test)
finally:
    json_object = json.dumps({
        'check_account': result
    })
    with open('result.json', 'w') as save_as:
        save_as.write(json_object)