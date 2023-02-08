from dotenv import load_dotenv
import os
import base64
from requests import post, get
import requests
import json

# testing import of redd-api.py
import redd_api
# Runs through the reddit api and returns an array of arrays containing song/artist/genre/year info and stores value
reddit_data_arr = redd_api.test_calls()

print(reddit_data_arr)
print('-----------------------------')
print('-----------------------------')
print('-----------------------------')

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_token_alt():
    auth_header = f"Basic {base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()}"

    auth_response = requests.post("https://accounts.spotify.com/api/token", headers={
             "Authorization": auth_header}, data={"grant_type": "client_credentials"})

    access_token = auth_response.json()["access_token"]


def get_auth_header(token):
    access_token = token
    user_id = "flecked"
    playlist_name = "testing123"

    return {"Authorization": "Bearer " + token}


def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("Artist cannot be found or doesn't exist...")
        return None

    return json_result[0]


def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result


def get_user_id(token):
    # token = get_token()
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    response = requests.get("https://api.spotify.com/v1/me", headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data["id"]
        print(user_id)
    else:
        print(f"Status code: {response.status_code}. Failed to get user data.")

# def get_trackid_by_songandartist(token, songdata):
#     for i in songdata:

#     print("something")


token = get_token()
songid_arr = []
# result = search_for_artist(token, "Death's Dynamic Shroud")
# artist_id = result["id"]
# songs = get_songs_by_artist(token, artist_id)

# print(songs)


# print(response1_json['data']['children'][0]["data"]["title"])

# json_reslt['tracks']['items'][0]

def get_track_ids(token):
    headers = get_auth_header(token)

    # artist_name = 'The Logic Box '
    # song_name = ' Liquid '
    # url = f"https://api.spotify.com/v1/search?q={song_name}+artist:{artist_name}&type=track"
    # result = get(url, headers=headers)
    # json_result = result.json()
    # print(result)
    # print(json_result)

    for x in reddit_data_arr:
        try:
            song_name = x[1]
            artist_name = x[0]
            url = f"https://api.spotify.com/v1/search?q={song_name}+artist:{artist_name}&type=track"
            result = get(url, headers=headers)
            json_result = result.json()
            songid_arr.append(json_result['tracks']['items'][0]['id'])
            # print(f"Song:{temp_song}\nArtist:{temp_artist}\n")
        except IndexError:
            print(f"'{x[1]}' by '{x[0]}' was not found. Skipping this iteration.")

    return songid_arr


def post_to_playlist(token):
    song_ids = get_track_ids(token)
    user_id = get_user_id(token)
    headers = get_auth_header(token)

    # params = {'uris':''}
    uri_key_value = ''

    i = 0

    for x in song_ids:
        if i < len(song_ids) - 1:
            uri_key_value += 'spotify:track:' + x + ','
            i += 1
        else:
            uri_key_value += 'spotify:track:' + x
            i += 1
    print(uri_key_value)
    print("------")
    print(user_id)


# print("========================")
# print(f"{0}.{songs[0].keys()}")
# print("========================")
# for idx, song in enumerate(songs):
#     print(f"{idx + 1}. {song['track_number']}")
# testing(token,' Trouble in Mind ','Bud Grant')
# post_to_playlist(token)
test = get_token()
print(test)
