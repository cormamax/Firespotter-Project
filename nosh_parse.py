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
#print "url = " + url

######
#Do error handling for the number of arguments

######


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


#get ids
items = soup.findChildren('div', id=re.compile("^item-"))

#get items and reviews
names = []
reviews = []
i = 0;
while i < len(items):
	my_table = items[i]
	name_row = my_table.findChildren('div', attrs={"class" : 'ow-check-in-mi'})
	# get name
	for a in name_row:
		#You are now at each child in this row
		names.extend(a.contents[0])
		#print names[i]
	
	# get review
	review_row = my_table.findChildren('div', attrs={"class" : 'ow-check-in-review'})
	#print review_row
	#print len(review_row)
	if (len(review_row) > 0):
		for a in review_row:
			temp = a.contents[1].contents[0]
			#print temp
			reviews.extend(temp)
	else:
		reviews.extend('')
		
	i = i + 1


#print "size names"
#print len(names)
#print "size reviews"
#print len(reviews)

for a in names:
	print a
	
#for a in reviews:
#	print a

# 4. Write to a csv file
import csv

#examples
with open('some.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerows(names)





















"""
tags = soup.findAll('td', attrs={"class" : 'ow-check-in-m'})

for a in tags:
	child = a.findChildren()
	print a
	#print child
	print ""
"""

"""
#find first object in the menu
#tags = soup.find('td', attrs={"class" : 'ow-check-in-m'})
tags = soup.findAll('div', id=re.compile("^item-"))
print len(tags)

#Search the menu list for the item ids. Get a list of those
ids = []


i = 0
while i < len(tags):
	temp = tags[i]['id']
	print temp
	#print ""
	ids.extend(temp)
	i = i + 1

print len(ids)

while i < len(ids):
	print ids[i].string
	
"""


"""
#found all items. Get the names of them!
item = tags.findAllNext('div', attrs={"class" : 'ow-check-in-mi'})
i = 0
item_names = []
while i < len(item):
	temp = item[i].contents[0].contents	
	item_names.extend(temp)
	print item_names[i]
	i = i + 1
	
#now search for the review!
i = 0
while i < len(item)
	name = tags.find
	
"""	
	
	
#i = 0
#temp = soup.find('div', )
#print temp
#print len(item)
#while i < len(item):
#	temp = soup.find(item[i].body)
#	i = i + 1
	
#now look for description
#desc = tags.findAllNext('div', attrs={"class" : 'ow-check-in-review'})
#for a in desc:
#	print a

#print item
#print len(item)
#print ""
#while a < len(tags):
#	item = tags.findAllNext('div', attrs={"class" : 'ow-check-in-mi'})
#	print item
#	a = a + 1
	#if (item)
		

#print tags




"""
tags = soup.findAll('a', href=re.compile("^/menuitem/"))
#tags = soup.findAll('td', attrs={"class" : 'ow-check-in-review'})
#remove image tags. They have the same href.
for a in tags:
	children = a.findChildren()
	if (len(children) > 0):
		tags.remove(a)

for a in tags:
	print a
	
# now get the food description
#soup = BeautifulSoup(''.join(html_contents))
#get parent of description
reviews = soup.findAll('div', attrs={"class" : 'ow-check-in-review'})
desc = []
print "review size = "
print len(reviews)
for a in reviews:
	child = a.findChildren()
	desc.extend(child)
	#print a
		
for a in desc:
	print a
"""	

#get parser
#My parser
#parser = MyHtmlParser.MyHtmlParser()
#parser.feed(html_contents)




print "done"


#print 'Number of argument:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)


#getopt.getopt(args, options[, long_options])











