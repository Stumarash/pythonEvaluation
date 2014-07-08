__author__ = 'Tumelom'

import mechanize
import cookielib
import re

URL = "http://slashdot.org/"
br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

br.set_handle_equiv(True)
br.set_handle_gzip(False)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

username = raw_input("please enter username : ")
password = raw_input("please enter password :")
USERNAME = "Tumelom"
PASSWORD = "Tumelom123"
regexHeadLine = '<h2 class="(.+?)*"></h2>'
regexAuthor = '<a href="(.+?)*" rel="nofollow">(.+?)*</a>'
regexDate = '<time id="(.+?)*" datetime="(.+?)*">(.+?)*</time>'

htmlfile = br.open(URL).read()


def patterns(string):
    pattern1 = re.compile(regexHeadLine)
    head = re.findall(pattern1, string)
    pattern2 = re.compile(regexAuthor)
    author = re.findall(pattern2, string)
    pattern3 = re.compile(regexDate)
    date = re.findall(pattern3, string)
    print head, "\n", author, "\n", date


def validate_user(user_name, user_password, html):
    if user_name == USERNAME and user_password == PASSWORD:
        print html
    else:
        return patterns(html)


validate_user(username, password, htmlfile)
