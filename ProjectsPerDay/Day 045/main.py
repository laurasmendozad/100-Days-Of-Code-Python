''' Movies That You Must Watch Project '''
from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL, timeout=10)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
movies = soup.find_all("h3", class_="title")
best_movies = []
for m in movies:
    best_movies.append(m.get_text())
best_movies.reverse()

with open(r"ProjectsPerDay\Day 45\movies.txt", mode="w", encoding="utf-8") as file:
    for movie in best_movies:
        print(movie)
        file.write(f"{movie}\n")
