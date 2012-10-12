#this file is a command line script.
#it goes to a url in nosh and pulls that restaurants menu list
# 1. The script takes a restaurant url on the command line
# 2. fetches the html from the page
# 3. parses just the menu item information out 
# 4. writes menu item information to a .csv file. 
#	Put the menu item name as the first value in the csv row, 
#	and the description (if it exists), as the second value.


# 1. Get to url from the command line.
# Use OptionParer from optparse
from optparse import OptionParser

parser = OptionParser()
# There are no options for this program
# There is one positional argument, which is the url of
# the restuarant in nosh
# example of url is http://www.nosh.com/restaurant/2630123
					
(options, args) = parser.parse_args()

url = args[0]
print "url = " + url
#print args for testing
#print args

# 2. fetch the html from the url

#import urllib. Fetches over HTTP
import urllib

website = urllib.urlopen(url)

#read from website. Store contents
html_contents = website.read()

#close website
website.close()

# can print the html. Don't print! Its a lot!
#print html_contents
#import MyHtmlParser


# 3. Parse the html!
#import BeautifulSoup! This is the BeautifulSoup4 Beta.
#from bs4 import BeautifulSoup

#import BeautifulSoup! This is BeautifulSoup3
from BeautifulSoup import BeautifulSoup
#import regular expression library
import re

# steps to do this. 
# use BS.findAll to find all tags that are a menu item
# and have the proper attributes

soup = BeautifulSoup(''.join(html_contents))
# find all tags that = a and attribute is regex "/menuitem/... wher
# the strings in the language "/menuitem/"
tags = soup.findAll('a', href=re.compile("^/menuitem/"))

#remove image tags. They have the same href.
for a in tags:
	children = a.findChildren()
	if (len(children) > 0):
		tags.remove(a)

#for a in tags:
	#print a
	
# now get the food description
soup = BeautifulSoup(''.join(html_contents))

reviews = soup.findAll('div', attrs={"class" : 'ow-check-in-review'})

for a in reviews:
	print a
	

#example
#doc = ['<html><head><title>Page title</title></head>',
#       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
#       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
#       '</html>']
#soup = BeautifulSoup(''.join(html_contents))

#print soup.prettify()


#get parser
#My parser
#parser = MyHtmlParser.MyHtmlParser()
#parser.feed(html_contents)




print "done"


#print 'Number of argument:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)


#getopt.getopt(args, options[, long_options])











