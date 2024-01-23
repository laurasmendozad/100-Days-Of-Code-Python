''' Musical Time Machine '''
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

# Step 1 - Scrapping the Billboard Hot 100
date = input("Which year do you want to travel to? (Type the date in this format YYYY-MM-DD) -> ")

URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL, timeout=10)

soup = BeautifulSoup(response.text, "html.parser")

songs_artists = soup.select(".o-chart-results-list__item .a-no-trucate")
songs_artists = [song_artist.get_text().strip() for song_artist in songs_artists]

# Step 2 - Authentication with Spotify
# Lista de Scopes: https://developer.spotify.com/documentation/web-api/concepts/scopes
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get("SPOTIFY_CLIENTID"),
                                               client_secret=os.environ.get("SPOTIFY_CLIENTSECRET"),
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               cache_path=r"ProjectsPerDay\Day 046\token.txt"))
user_id = sp.current_user()["id"]

# Step 3 - Search Spotify for the Songs from Step 1
song_uris = []
year = date.split("-")[0]

for i in range(0,len(songs_artists),2):
    result = sp.search(q=f"artist: {songs_artists[i+1]} track: {songs_artists[i]}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{songs_artists[i]} doesn't exist in Spotify. Skipped.")

# Step 4 - Creating and Adding to Spotify Playlist
playlist_name = f"{date} Billboard 100"
playlist = sp.user_playlist_create(user_id,playlist_name, public=False)
sp.playlist_add_items(playlist['id'], song_uris)
print(f"Private playlist '{playlist_name}' created successfully.")
