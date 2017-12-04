# Class file for a team object
# Eric  Cramer <cramerericm@gmail.com>

class team:
	""" Class definition for a team object """

	def __init__(self, teamname):
		self.teamname = teamname
		self.roster = []

	""" Function to add a wrestler to a team's roster 
		Input:
			wrestler: a wrestler object to be added to the team's roster
		Output: 
			assigns the wrestler to the the roster internal data structure
	"""
	def add_wrestler(self, wrestler):
		self.roster.append(wrestler)