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
# An example of an option is this (for my knowledge)
# There is one positional argument, which is the url of
# the restuarant in nosh
					
(options, args) = parser.parse_args()

print args
print "done"

#print 'Number of argument:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)


#getopt.getopt(args, options[, long_options])











