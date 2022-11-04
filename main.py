import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Retrieves URL and page source
response = requests.get(url=URL)
page_source = response.text

# Scrapes page source for movie title
soup = BeautifulSoup(page_source, 'html.parser')

movie_title = soup.find_all(name='h3', class_='title')

# Makes a list of movie titles descending from 1 - 100
movies_list = []
for movie in movie_title:
    movies = movie.getText()
    movies_list.append(movies)
reordered_movies_list = movies_list[::-1]

with open('movies.txt', 'a', encoding='utf-8') as file:
    for movie in reordered_movies_list:
        file.write(f'{movie}\n')
