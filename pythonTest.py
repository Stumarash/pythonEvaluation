from sklearn.externals.joblib.test.test_numpy_pickle import _class

__author__ = 'Tumelom'

import mechanize
import cookielib
from bs4 import BeautifulSoup
import urllib2
from mechanize._form import ControlNotFoundError
import re

URL = "https://slashdot.org"
br = mechanize.Browser()
br.open(URL)
html_file = urllib2.urlopen(URL)
soup = BeautifulSoup(html_file)

cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

br.set_handle_equiv(True)
br.set_handle_gzip(False)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# user is expected to input his/her login details
nickname = raw_input("please enter your nickname :")
password = raw_input("please enter your password :")

#i loop through links that are available in the browser
#when link url is the same as target url then browser will navigate to that link
for link in br.links():
    target_url = "my/login"
    if link.url == target_url:
        br.follow_link(link)

#here i am using exception handling to login
#i am selecting the first form and assign it user details
#if found is found the will be submitted
#else control not found error will be thrown
<<<<<<< HEAD
#and headlines,author and date a story was published
=======
>>>>>>> origin/master
try:
    br.select_form(nr=0)
    br.form["unickname"] = nickname
    br.form["upasswd"] = password
    br.submit()
except ControlNotFoundError:
    print "couldn't login no control found!"

<<<<<<< HEAD
try:
    print "headlines : " + soup.findAll('span', {'id': 'title-62092829'})[1].contents[0]
except:IndexError

try:
    print "author : " + soup.findAll('div', {'class': 'details'})[1].contents[0]
except :IndexError

try:
    print "date : " + soup.findAll('time',{'datetime': re.findAll(re.compile("(.+?)", html_file))})[1].content[0]
except:IndexError
=======
#here i am trying to collect page headlines,date it was published and author
try:
    headlines = soup.findAll('span', {'id': 'title-62092829'})[1].contents[0]
except:IndexError

try:
    author = soup.findAll('div', {'class': 'details'})[1].contents[0]
except :IndexError

try:
    date = soup.findAll('time',{'datetime': re.findAll(re.compile("(.+?)", html_file))})[1].content[0]
except:IndexError

print "%s,%s,%s" % (headlines, author, date)
>>>>>>> origin/master
