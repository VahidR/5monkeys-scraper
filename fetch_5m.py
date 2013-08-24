#!/usr/bin/env python
''' 
Copyright (C) 2013  Vahid Rafiei (@vahid_r)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


from bs4 import BeautifulSoup, Comment
import requests
import re

class ParseMonkey(object):
	'''
	class `ParseMonkey` is supposed to implement this interesting quiz.
	'''

	def __init__(self):
		self._url = 'http://www.5monkeys.se/'
		self._response = ''
		self._source = ''
		self._comments = ''
		self._reg = ''
	
	def process_parsing(self):
		'''
		method `process_parsing` is responsible for doing the main logic.
		It calls `requests`, `BeautifulSoup` and `re` libs and process an interesting steps.
		The step-by-step procedure is mentioned as comments.
		'''
		
		# First, we fetch the contents of `5monkeys.se` to be processed.
		self._response = requests.get(self._url)
		self._response = self._response.text[122:] # neglecting the DOCTYPE
		
		# calling BeautifulSoup lib
		self._source = BeautifulSoup(self._response)

		#let's remove all the attributes
		for tag in self._source.find_all(True):
			tag.attrs = {}

		# we are not interested in HTML comments, too
		self._comments = self._source.find_all(text=lambda text:isinstance(text, Comment))
		for comment in self._comments:
			comment.extract()
		
		# the same logic for h1 and h2 tag's content
		self._source.h1.clear()
		for h2 in self._source.find_all('h2'):
			h2.clear()
		
		# and links
		for a in self._source.find_all('a'):
			a.clear()
		
		# and title
		self._source.title.clear()

		# and strong tag in the bottom
		for con in self._source.find_all('strong'):
			con.clear()
		
		# Alright .. we have some <p> tags, but all of them have different type of contents!
		# so, let's approach each <p> differently:
		# the first P is simple
		self._source.find_all('p')[0].clear()

		# the second <p> has an <script> tag. We are not interested in it. So let's get rid of it..
		self._source.find_all('p')[1].clear()

		# 3rd <p> is more interesting. It has nested tags! So we should be careful!
		# Here we have the name and the address of the company. We are not interested in those stuff,
		# so, we carefully select and remove them
		for i in [14,12,5,3]: # pop occurrences form the Stack
			self._source.find_all('p')[2].contents[i].extract()

		# Now, this is a pure hack to make prettify() work just like what you requested
		self._trans_to_str = str(self._source.prettify())
		self._str_re_left = re.sub(r'<', r'[', self._trans_to_str)
		self._str_re_right = re.sub(r'>', r']', self._str_re_left)
		self._back_to_soup = BeautifulSoup(self._str_re_right)

		return self._modified_prettify(self._back_to_soup)[30:1721]

	def _modified_prettify(self, stream, encoding=None, formatter="minimal"):
		'''
		hacking BeautifulSoup.prettify() to indent by 2 spaces rather than one space
		'''
		self._reg = re.compile(r'^(\s*)', re.MULTILINE)
		return self._reg.sub(r'\1\1', stream.prettify(encoding, formatter))



			

if __name__ == '__main__':
	ParseMonkey = ParseMonkey()
	print "*** Fetching and parsing http://www.5monkeys.se/"
	print ParseMonkey.process_parsing()



