# Copyright (C) 2014 James Scott-Brown
# Licensed under the MIT license

import re
import datetime

from MarkdownPP.Module import Module
from MarkdownPP.Transform import Transform

datere = re.compile("^!DATE\s*$")
datetimere = re.compile("^!DATETIME\s*$")

class Date(Module):
	"""
	Module for adding the current date/date-time wherever a `!DATE` or 
	`!DATETIME` marker is found at the beginning of a line.
	"""

	def transform(self, data):
		now = datetime.datetime.now()

		transforms = []
		linenum = 0
		for line in data:
			dateMatch = datere.search(line)
			datetimeMatch = datetimere.search(line)

			dateString = ""
			if dateMatch:
				dateString = now.strftime("%Y-%m-%d\n")
			elif datetimeMatch:
				dateString = now.strftime("%Y-%m-%d %H:%M\n")

			if dateString:
				transform = Transform(linenum=linenum, oper="swap", data=dateString)
				transforms.append(transform)
			
			linenum += 1

		return transforms