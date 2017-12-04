# Class file for a wrestler object
# Eric  Cramer <cramerericm@gmail.com>

import datetime

class wrestler:
	""" Class definition for a wrestler object 
		
		Class Description: 
		The wrestler.py class contains information about the wrestler. These fields include the wrestler's full name, their weight class, minimum weight, a daily record of their weights before and after practice along with teh date of the practice, and the number of matches that the wrestler has won and lost. The class also contains auxillary information such as the wrestler's clearance status (ie. their physical, concussion testing, and database status)

	"""

	def __init__(self, firstname, lastname, weight_class, year, minweight):
		self.firstname = firstname
		self.lastname = lastname
		self.weight_class = weight_class
		self.minweight = minweight
		self.daily_weight_in = []
		self.daily_weight_out = []
		self.weigh_dates = []
		self.matches_won = 0
		self.matches_lost = 0
		self.has_physical = False
		self.has_concussion_test = False
		self.has_database_clearance = False

	""" Function to record a wrestler's weight at the beginning of practice
		Input:
			weight: the wrestler's weight as a float
		Output: none
	"""
	def record_weight_in(weight):
		self.daily_weight_in.add(weight)

	""" Function to record the wrestler's weight at the end of practice
		Input:
			weight: the wrestler's weight as a float
		Output: none
	"""
	def record_weight_out(weight):
		self.daily_weight_out.add(weight)

	""" Function to record the date the wresstler's weights were recorded
		Input:
			date: a datetime object indicating the weight record date
		Output: none
	"""
	def record_weigh_date(date):
		self.weigh_dates.add(date)

	""" Function to record a wrestler's win
		Input: none
		Output: none
	"""
	def record_win(self):
		self.matches_won += 1

	""" Function to record a wrestler's loss
		Input: none
		output: none
	"""
	def record_loss(self):
		self.matches_lost += 1

	""" Function to print out the wrestlers win-loss record
		Input: none
		Output: none
	"""
	def get_record(self):
		return "%d - %d" % (self.matches_won, self.matches_lost)

