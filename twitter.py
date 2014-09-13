#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: pandaf00
Last Modified: September 2014
Twitter: @pandaf00
"""

import csv
from bs4 import BeautifulSoup
import urllib2
import sys
import time
import os

def Search():
    hashtag = sys.argv[1]
    # twitter url to grep results from
    print "Loading results please wait..."
    os.system("cls")
    time.sleep(2.0)
    page = urllib2.urlopen("http://www.twitter.com/hashtag/" + hashtag)
    soup = BeautifulSoup(page)
    
    # data to extract
    tweet_content   = soup.find_all("p", "js-tweet-text")
    tweet_timestamp = soup.find_all("a", "tweet-timestamp")
    tweet_links     = soup.find_all("a", "js-details")

    print tweet_timestamp + tweet

def save_Results():
    # define what goes in our .csv
    authors     = []
    timestamps  = []
    tweets      = []
    hashtags    = []

Search()
    



