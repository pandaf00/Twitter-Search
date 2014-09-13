#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: pandaf00
Last Modified: September 2014
Twitter: @pandaf00
"""

import urllib2
import sys
from bs4 import BeautifulSoup

def Search():
    hashtag = sys.argv[1]
    page = urllib2.urlopen("http://www.twitter.com/hashtag/" + hashtag)
    soup = BeautifulSoup(page)
    tweets = soup.findAll("li", "js-stream-item")
    
    print tweets

Search()
