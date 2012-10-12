# My custom html parser. Helps parse for the proper tags
# I am looking for the <div id="menu-item-list"> start tag
# That tag holds all the menu item information
# The <div class="ow-check-in-mi"> is the start tag before
# the name of the item
# The <div class="ow-check-in-review"> is the start tag for the 
# description of the food time. BE CAREFUL. User Reviews can
# replace this. Check for a <a href="/user/741001"> tag right after
# It might mean that it is a user review



#get HTMLParser base class
from HTMLParser import HTMLParser
#this helps map HTML entity names to the Unicode codepoints
# we want this because the HTMLParser likes Unicode
from htmlentitydefs import name2codepoint

class MyHtmlParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print "Start tag:", tag
		for attr in attrs:
			print "		attr:", attr
	def handle_endtag(self, tag):
		print "End tag :", tag
	def handle_data(self, data):
		print "Data :", data
	def handle_comment(self, data):
		print "Comment :", data
	def handle_entityref(self, name):
		c = unichr(name2codepoint[name])
		print "Named ent: ", c
	def handle_charref(self, name):
		if name.startswith('x'):
			c = unichr(int(name[1:], 16))
		else:
			c = unichr(int(name))
		print "Num ent	:", c
	def handle_decl(self, data):
		print "Decl		:", data
		
		
#for testing		
#parser = MyHtmlParser()
#parser.feed('<img src="python-logo.png">')
#'<img src="python-logo.png" alt="The Python logo">'

#print "done"

