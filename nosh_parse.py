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
print url

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
		names.append(a.contents[0].contents[0])
		#print names[i]
	
	# get review
	review_row = my_table.findChildren('div', attrs={"class" : 'ow-check-in-review'})
	#print review_row
	#print len(review_row)
	if (len(review_row) > 0):
		for a in review_row:
			temp = a.contents[1].contents[0]
			#print temp
			reviews.append(temp)
	else:
		reviews.append('')
		
	i = i + 1


print "size names"
print len(names)
print "size reviews"
print len(reviews)
# len of names and reviews should be the same


for a in names:
	print a
	
for a in reviews:
	print a

# 4. Write to a csv file

import csv
# get the number of the restaurant from the url
# you still have url!
#http://www.nosh.com/restaurant/2630123
filename = url[31:] + '.csv'
#print filename
#filename = 'file.csv'
with open(filename, 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=' ',
						quotechar='|', quoting=csv.QUOTE_MINIMAL)
	i = 0
	while (i < len(names)):
		str1 = names[i]
		str2 = reviews[i]
		list = [str1, str2]
		spamwriter.writerow(list)
		#spamwriter.writerow(names[i] + reviews[i])
		i = i + 1
	















