''' Musical Time Machine '''
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? (Type the date in this format YYYY-MM-DD) -> ")

URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL, timeout=10)

soup = BeautifulSoup(response.text, "html.parser")
songs = soup.select("li #title-of-a-story")
songs_titles = [song.get_text().strip() for song in songs]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="",
                                               client_secret="YOUR_APP_CLIENT_SECRET",
                                               redirect_uri="YOUR_APP_REDIRECT_URI",
                                               scope="user-library-read"))
 