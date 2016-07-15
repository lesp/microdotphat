#!/usr/bin/env python

from microdotphat import WIDTH, HEIGHT, set_pixel, write_string, scroll, scroll_to, show
import time
import feedparser

rewind = True
delay = 0.001

line_height = HEIGHT + 2
feed = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml".encode('utf-8'))
             
#lines = [feed['entries'][0]['title'],feed['entries'][1]['title'],feed['entries'][2]['title']]
lines = []
for i in range(6):
    lines.append(feed['entries'][i]['title'])
    
lengths = [0] * len(lines)

offset_left = 0

for line, text in enumerate(lines):
    lengths[line] = write_string(text, offset_x=offset_left, offset_y=line_height * line)
    offset_left += lengths[line]

set_pixel(0, (len(lines) * line_height) - 1, 0)

current_line = 0

show()

while True:
    pos_x = 0
    pos_y = 0
    for current_line in range(len(lines)):
        time.sleep(delay*10)
        for y in range(lengths[current_line]):
            scroll(1,0)
            pos_x += 1
            time.sleep(delay)
            show()
        if current_line == len(lines) - 1 and rewind:
            for y in range(pos_y):
                scroll(-int(pos_x/pos_y),-1)
                show()
                time.sleep(delay)
            scroll_to(0,0)
            show()
            time.sleep(delay)
        else:
            for x in range(line_height):
                scroll(0,1)
                pos_y += 1
                show()
                time.sleep(delay)
