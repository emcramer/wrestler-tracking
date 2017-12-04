# Class file for a match object
# Eric  Cramer <cramerericm@gmail.com>

import datetime

class match:
	""" Definition for a match between two wrestlers """

	def __init__(self, red_wrestler, green_wrestler, red_team1, green_team):
		self.red_wr = (red_wrestler, red_team)
		self.green_wr = (green_wrestler, green_team)
		self.red_wr_score = 0
		self.green_wr_score = 0
		self.red_wr_cautions = 0
		self.green_wr_cautions = 0
		self.red_wr_match_record = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
		self.green_wr_match_record = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}

	""" Function to record a takedown 
		Input:
			wrestler: wrestler to award the takedown to ("red" or "green")
			period: the period in which the takedown occurred
		Output:
			increments the correct wrestler's score and assigns the takedown to the appropriate internal data structure, either red_wr_match_record or green_wr_match_record
	"""
	def score_takedown(self, wrestler, period):
		if wrestler == "red":
			self.red_wr_score += 2
			self.red_wr_match_record[period].append("T2")
		else:
			self.green_wr_score += 2
			self.green_wr_match_record[period].append("T2")

	""" Function to record an reversal
		Input:
			wrestler: wrestler to award the reversal to ("red" or "green")
			period: the period in which the reversal occurred
		Output:
			increments the correct wrestler's score and assigns the reversal to the appropriate internal data structure, either red_wr_match_record or green_wr_match_record
	"""
	def score_reversal(self, wrestler, period):
		if wrestler == "red":
			self.red_wr_score += 1
			self.red_wr_match_record[period].append("E1")
		else:
			self.green_wr_score += 1
			self.green_wr_match_record[period].append("E1")

	""" Function to record near fall
		Input:
			wrestler: wrestler to award the near fall to ("red" or "green")
			period: the period in which the near fall occurred
		Output:
			increments the correct wrestler's score and assigns the near fall to the appropriate internal data structure, either red_wr_match_record or green_wr_match_record
	"""
	def score_nearfall(self, wrestler, pts, period):
		if wrestler == "red":
			self.red_wr_score += pts
			self.red_wr_match_record[period].append("NF%d" % pts)
		else:
			self.green_wr_score += pts
			self.green_wr_match_record[period].append("NF%d" % pts)

	""" Function to record a reversal
		Input:
			wrestler: wrestler to award the reversal to ("red" or "green")
			period: the period in which the reversal occurred
		Output:
			increments the correct wrestler's score and assigns the reversal to the appropriate internal data structure, either red_wr_match_record or green_wr_match_record
	"""
	def score_reversal(self, wrestler, period):
		if wrestler == "red":
			self.red_wr_score += 2
			self.red_wr_match_record[period].append("R2")
		else:
			self.green_wr_score += 2
			self.green_wr_match_record[period].append("R2")

	""" Function to record a technical violation
		Input:
			wrestler: wrestler to award the technical violation to ("red" or "green")
			period: the period in which the technical violation occurred
		Output:
			increments the correct wrestler's score and assigns the technical violation to the appropriate internal data structure, either red_wr_match_record or green_wr_match_record
	"""
	def score_technical_violation(self, wrestler, period):
		if wrestler == "red":
			self.green_wr_score += 1
			self.red_wr_match_record[period].append("P")
			self.green_wr_match_record[period].append("P1")
		else:
			self.green_wr_score += 1
			self.green_wr_match_record[period].append("P")
			self.red_wr_match_record[period].append("P1")

	""" Function to record a pin
		Input: 
			wrestler: which wrestler scored the pin ("red" or "green")
			time: a time object that has the time of the pin in minutes and seconds
			period: which period the pin was recorded
		Output:
			assigns the pin to the appropriate internal data structure, either red_wr_match_record or green_wr_match_record
	""" 
	def score_pin(self, wrestler, time, period):
		if wrestler == "red":
			self.red_wr_match_record[period].append("F%d:%d" % (time.minute, time.second))
		else:
			self.green_wr_match_record[period].append("F%d:%d" % (time.minute, time.second))

	""" Function to record a technical fall
		Input: 
			wrestler: which wrestler scored the technical fall ("red" or "green")
			time: a time object that has the time of the technical fall in minutes and seconds
			period: which period the technical fall was recorded
		Output:
			assigns the technical fall to the appropriate internal data structure, either red_wr_match_record or green_wr_match_record
	""" 
	def score_techfall(self, time, period):
		if wrestler == "red":
			self.red_wr_match_record[period].append("TF%d:%d" % (time.minute, time.second))
		else:
			self.green_wr_match_record[period].append("TF%d:%d" % (time.minute, time.second))
