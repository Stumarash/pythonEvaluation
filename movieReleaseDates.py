__author__ = 'Tumelom'
import re
from bs4 import BeautifulSoup
import urllib2
URL = "http://www.imdb.com/calendar/?ref_=nv_mv_cal_5"

html_text = urllib2.urlopen(URL).read()
soup = BeautifulSoup(html_text)


movie_title = raw_input("please enter name of the movie you'd like to view.")

titleslist = []
for titles in soup:
    titleslist.append(titles)
    try:
        title_released = soup.findAll('div', {'id': 'main'})[1].contents[0]
        release_date = soup.findAll('span', {'class': 'year_type'})[1].contents[0]
        while len(titleslist) < 10:
            if movie_title == title_released:
                print title_released
                print release_date
            else:
                print movie_title + " is not in the list"
    except:IndexError
