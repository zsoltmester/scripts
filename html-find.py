#!/usr/bin/python3

##
# This script helps to search in a html file. Currently it supports only searching for a value of a tag.
#
# Params:
#	1.: The HTML file.
#	2.: The result file.
#	3.: The name of the tag to search for.
##

# process args
import sys
pathHtml = sys.argv[1]
pathResult = sys.argv[2]
tag = sys.argv[3]

##
# search for the tag and log the values
##

from html.parser import HTMLParser
class TagHTMLParser(HTMLParser):
	def __init__(self):
        	HTMLParser.__init__(self)
        	self.count = 0
	def handle_starttag(self, start_tag, attrs):
		if tag == start_tag:
			self.count += 1
	def handle_endtag(self, end_tag):
		if tag == end_tag:
			self.count -= 1
	def handle_data(self, data):
		if self.count > 0:
			result.write(data)

htmlFile = open(pathHtml, 'r')
html = htmlFile.read()
htmlFile.close()

result = open(pathResult, 'w', True)
parser = TagHTMLParser()
parser.feed(html)
result.close()
