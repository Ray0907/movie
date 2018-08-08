from bs4 import BeautifulSoup
from selenium import webdriver
import re
SEARCH_URL= 'http://search.atmovies.com.tw/search/'
PAGE_URL = 'http://www.atmovies.com.tw/movie'

class Movie(object):
    def __init__(self):
        self.title = ""
        self.year = ""
        self.rate = 0
        self.director = ""
        self.casts = ""
        self.intro = ""

    def __str__(self):
        text = "===============   開眼電影   ====================\n" + \
               "Title: " + self.title + '\n' + \
                str(self.year) + '\n' + \
               "Introduction: " + self.intro + "\n" + \
               "====================================================="
        return text
def search(text):
    driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    driver.get(SEARCH_URL)
    element = driver.find_element_by_css_selector('input#search-field')
    element.send_keys(text)
    submit = driver.find_element_by_css_selector('input[class=form-submit]')
    submit.click()
    html =driver.page_source
    driver.close()
    soup =BeautifulSoup(html,'lxml')
    if soup.findAll('a',{'class','title big'}):
        movies = []
        for item in soup.findAll('a',{'class','title big'}):
            movie = Movie()
            movie.title = item.text
            movie.url = item['href']
            movies.append(movie)
    return movies

def parse(movie):

    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    url = PAGE_URL+ re.sub('F/',"",movie.url)
    driver.get(url)
    html = driver.page_source
    driver.close()
    soup = BeautifulSoup(html, 'lxml')
    movie.intro = soup.find('div',{"style": "width:90%;font-size: 1.1em;"}).text
    movie.year = soup.select('span:nth-of-type(3) ul > li')[1].text
    print(movie)

def get_movie(text):
    movies = search(text)
    if movies and len(movies):
        parse(movies[0])
    else:
        print ('cound not find movie: ' + text)

