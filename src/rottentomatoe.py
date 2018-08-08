from bs4 import BeautifulSoup
import requests
import json
from six.moves.urllib.parse import quote


SEARCH_URL='https://www.rottentomatoes.com/api/private/v2.0/search?q='
PAGE_URL='https://www.rottentomatoes.com'

class Movie(object):
    def __init__(self):
        self.title = ""
        self.year = ""
        self.TOMATOMETER = 0
        self.AUDIENCE_SCORE = 0
        self.director = ""
        self.casts = ""
        self.intro = ""

    def __str__(self):
        text = "===============   RottenTomatoes   ====================\n" + \
               "Title: " + self.title + '\n' + \
               "TOMATOMETER: " + str(self.TOMATOMETER) + '\n' + \
               "AUDIENCE SCORE: " + str(self.AUDIENCE_SCORE) + '\n' + \
               "Year: " + str(self.year) + '\n' + \
               "Casts: " + self.casts + '\n' + \
               "Introduction: " + self.intro + "\n" +\
               "====================================================="
        return text
def search(text):
    text = quote(text)
    url = SEARCH_URL + text + "&t=movie"
    res = requests.get(url)
    if res.status_code != 200:
        return

    data = res.text.encode('utf-8')
    items = json.loads(data).get('movies')
    if len(items) == 0:
        return
    movies = []
    for item in items:
        movie = Movie()
        movie.title = item['name']
        movie.year = item['year']
        movie.url = item['url']
        movie.casts = item['subline']
        movies.append(movie)
    return movies

def parse(movie):
    url = PAGE_URL + movie.url
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    if soup.find('span',{'class':'meter-value superPageFontColor'}):
        movie.TOMATOMETER = soup.find('span',{'class':'meter-value superPageFontColor'}).text
    if soup.find('span',{'class':'superPageFontColor','style': 'vertical-align:top'}):
        movie.AUDIENCE_SCORE = soup.find('span',{'class':'superPageFontColor','style': 'vertical-align:top'}).text
    movie.intro = soup.find('div', {"id": 'movieSynopsis'}).text
    print (movie)

def get_movie(text):
    movies = search(text)
    if movies and len(movies):
        parse(movies[0])
    else:
        print ('cound not find movie: ' + text)

