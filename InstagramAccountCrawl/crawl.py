import json
import calendar
import time
from login import InstagramLogin
from target import target

class InstagramCrawl():
    requests = InstagramLogin().Login()
    post_list = []
    comment_list = []
    times_ago = calendar.timegm(time.gmtime())-(60*60*24*7)

    def parse_post(self, target:str):
        page = self.requests.get("https://www.instagram.com/"+target+"/?__a=1")
        graphql = json.loads(page.text)['graphql']
        user_id = graphql['user']['id'] 
        has_next_page = graphql['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
        end_cursor = graphql['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
        edges = graphql['user']['edge_owner_to_timeline_media']['edges']
        for edge in edges:
            taken_at_timestamp = edge['node']['taken_at_timestamp']
            if taken_at_timestamp > self.times_ago:
                post = {
                    "id": edge['node']['id'],
                    "shortcode": edge['node']['shortcode'],
                    "display_url": edge['node']['display_url'],
                    "owner": edge['node']['owner']['id'],
                    "caption": edge['node']['edge_media_to_caption']['edges'][0]['node']['text'],
                    "comments_count": edge['node']['edge_media_to_comment']['count'],
                    "comments_disabled": edge['node']['comments_disabled'],
                    "likes": edge['node']['edge_media_preview_like']['count'],
                    "taken_at_timestamp": taken_at_timestamp,
                    "is_video": edge['node']['is_video']
                }
                self.post_list.append(post)

        post_count = 0
        while has_next_page:
            page2 = self.requests.get("https://instagram.com/graphql/query/?query_id=17888483320059182&id="+user_id+"&first=50&after="+end_cursor)
            graphql2 = json.loads(page2.text)
            edges2 = graphql2['data']['user']['edge_owner_to_timeline_media']['edges']

            has_next_page = graphql2['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
            end_cursor = graphql2['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']

            for edge2 in edges2:
                caption = ""
                for c in edge2['node']['edge_media_to_caption']['edges']:
                    caption = c['node']['text']
                taken_at_timestamp = edge2['node']['taken_at_timestamp']
                if taken_at_timestamp > self.times_ago:
                    post2 = {
                        "id": edge2['node']['id'],
                        "shortcode": edge2['node']['shortcode'],
                        "display_url": edge2['node']['display_url'],
                        "owner": edge2['node']['owner']['id'],
                        "caption": caption,
                        "comments_count": edge2['node']['edge_media_to_comment']['count'],
                        "comments_disabled": edge2['node']['comments_disabled'],
                        "likes": edge2['node']['edge_media_preview_like']['count'],
                        "taken_at_timestamp": taken_at_timestamp,
                        "is_video": edge2['node']['is_video']
                    }
                    self.post_list.append(post2)
                else:
                    has_next_page = False

            post_count += len(edges2)
            print("Successfully Get '"+str(post_count)+"' Post From '"+target+"'")
    
    def parse_comments(self, target:str):
        self.parse_post(target)
        shortcode_list = []
        for post in self.post_list:
            shortcode_list.append(post['shortcode'])
        for shortcode in shortcode_list:
            has_next_page = True
            end_cursor = ""
            all_comments = []
            while has_next_page:
                page = self.requests.get('https://www.instagram.com/graphql/query/?query_hash=33ba35852cb50da46f5b5e889df7d159&variables={"shortcode":"'+shortcode+'","first":100,"after":"'+end_cursor+'"}')
                graphql = json.loads(page.text)

                has_next_page = graphql['data']['shortcode_media']['edge_media_to_comment']['page_info']['has_next_page']
                end_cursor = graphql['data']['shortcode_media']['edge_media_to_comment']['page_info']['end_cursor']
                edges = graphql['data']['shortcode_media']['edge_media_to_comment']['edges']

                for edge in edges:
                    all_comments.append(edge['node'])
            
            self.comment_list.append({
                'comments': all_comments,
                'shortcode': shortcode,
                'target': target
            })

    def save(self, formatName:str, list:str, parse):
        for username in target:
            parse(username)
            json_object = json.dumps({
                username: list
            })
            with open(username+formatName+'.json', 'w') as save_as:
                save_as.write(json_object)
            print("\n"+"-"*50+"\n|| Successfully Saved Data To '"+username+formatName+".json'"+"\n"+"-"*50+"\n")

    def save_post(self):
        self.save('_post', self.post_list, self.parse_post)

    def save_comments(self):
        self.save('_comments', self.comment_list, self.parse_comments)