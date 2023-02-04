import requests
import requests.auth
from rich import print
from credential import USERNAME, PASSWORD

import re

CLIENT_ID = 'NR71pbxIncACKKdjTFbdnQ'
CLIENT_SECRET = 'rsVZY0NGYfn8MT5aDv1mXibBu9d2wg'

#Authenticate Reddit App
client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
post_data = {'grant_type':'password', 'username': USERNAME, 'password': PASSWORD}
headers = {
    'User-Agent': 'A reddit automation script'
}

# Getting Token Access Id
TOKEN_ACCESS_ENDPOINT = 'https://www.reddit.com/api/v1/access_token'
response = requests.post(TOKEN_ACCESS_ENDPOINT, data=post_data, headers=headers, auth=client_auth)
# If request is 'OK' then get the key, 'access_token's value
if response.status_code == 200:
    token_id = response.json()['access_token']



#Use Reddit's REST API to perform operations
OAUTH_ENDPOINT = 'https://oauth.reddit.com'
param_get = {
    'limit': 10
}
headers_get = {
    'User-Agent': 'A reddit automation script',
    'Authorization': 'Bearer ' + token_id
}
response1 = requests.get(OAUTH_ENDPOINT + '/r/Listentothis/top', headers = headers_get, params = param_get)
response1_json = response1.json()

# testing import json

title_string = response1_json['data']['children'][0]["data"]["title"]

# data -> ['after', 'dist', 'modhash', 'geo_filter', 'children', 'before']
# print(response1_json['data']['children'].keys())
print("----------------------------")
# print(title_string)



# for i in response1_json:
#     for value in i.items():
#         print(value)
    # print(response1_json['data']['children'][0]["data"]["title"])

song_list = []
music_keys = ['title','artist','genre','year']

for post in response1.json()['data']['children']:
    song_list.append(post['data']['title'])
    # print(post['data']['title'])

for i in song_list:
    re.split('')


print(song_list)

# for data1 in response1_json['data']:
#     print(data1)


    # for children in data['children']:
    #     print(children.get('data'))
    # for children in data:
    #     for data in children:
    #         print(data)



# print(response1_json)

   