import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
content = response.text

soup = BeautifulSoup(markup=content, features="html.parser")
movie_list = soup.find_all(name="h3", class_="title")[::-1]
for movie_title in movie_list:
    with open(file="movies.txt", mode="a", encoding="utf-8") as file:
        file.write(f"{movie_title.text}\n")
