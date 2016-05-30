#!/usr/bin/python
import os
import sys
import urllib, urllib2
from BeautifulSoup import BeautifulSoup

BASE_URL = 'http://kindle4rss.com/'
USERNAME = ''
PASSWORD = ''

# build opener
o = urllib2.build_opener(urllib2.HTTPCookieProcessor())
urllib2.install_opener(o)

# login
p = urllib.urlencode({'email_address': USERNAME, 'password': PASSWORD})
doc = BeautifulSoup(o.open(BASE_URL + '/login/',  p).read().decode('utf8', 'replace'))

# get list of courses
doc = BeautifulSoup(o.open(BASE_URL,  p).read().decode('utf8', 'replace'))

if not doc:
    sys.exit(3)
else:
    if int(doc.em.text)>0:
        BeautifulSoup(o.open(BASE_URL + '/send_now/').read().decode('utf8', 'replace'))
