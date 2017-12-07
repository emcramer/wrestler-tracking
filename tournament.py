# Class file for a tournament object
# Eric  Cramer <cramerericm@gmail.com>

from wrestler import wrestler
from tournament_bracket import bracket
import numpy as np 
import datetime

class tournament:
	""" Class definition of a wrestling tournament """

	def __init__(self, name, date, location):
		self.name = name
		self.date = date
		self.location = location
		self.brackets = [] #internal list of bracket objects
