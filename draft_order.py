'''
Generates the order for the Fantasy Football draft.
'''

import datetime
import random

def make_order(pos):
	# shuffles in place, returning random.shuffle(pos) would result in None
	random.shuffle(pos)
	return pos

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
players = {'1': 'Berry',
		   '2': 'Asriel',
		   '3': 'JB',
		   '4': 'Durf',
		   '5': 'Hayden',
		   '6': 'Nate',
		   '7': 'Bradford',
		   '8': 'Lich',
		   '9': 'Nick',
		   '10': 'Curtis',
		   '11': 'Danny',
		   '12': 'Schnupp',
		   '13': 'Walston',
		   '14': 'John Wyatt'}
order = make_order(nums)
pos = 1
print datetime.datetime.now().strftime('\nProgram was run at: %-I:%M:%S %p, %-m-%-d-%y')
print "\nORDER\t|    PERSON"
print "----------------------"
for person in order:
	print "  %d\t|    %s" % (pos, players[str(person)])
	pos += 1
print "\nDisclaimer: I do not take any responsibility for\nthe results of this ordering. Blame the computer.\n"