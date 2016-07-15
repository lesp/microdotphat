#!/usr/bin/env python

from microdotphat import write_string, scroll, show, clear
import time
import feedparser

def feedme(feed):
    feed = feedparser.parse(feed.encode('utf-8'))
    for i in range(1):
        print(feed['entries'][i]['title'])
    write_string(feed['entries'][0]['title'], offset_x=1)
    scroll()
    show()
    time.sleep(0.05)
    #time.sleep(5)

while True:
    feedme("http://feeds.bbci.co.uk/news/rss.xml")
    clear()
    #time.sleep(5)

