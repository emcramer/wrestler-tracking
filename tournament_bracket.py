# Class file for a tournament bracket object
# Eric  Cramer <cramerericm@gmail.com>

from wrestler import wrestler
import numpy as np 

class bracket:
	""" Class definition for a tournament bracket """

	def __init__(self, weight_class, size):
		self.weight_class = weight_class
		self.size = size
		self.wrestlers = {}

	""" Fucntion to add a wrestler to the bracket
		Input: 
			wrestler: wrestler to be added to the bracket
		Output: none, appends the wrestler to an internal list
	"""
	def add_wrestler(self, wrestler, seed):
		self.wrestlers[seed] = wrestler

	""" Function to generate the matches in the bracket
		Input:
		Output:
	"""
	def gen_bracket(self):
		print("TODO")

	""" Function to divide up the initial brackets based on seeding. Taken from https://stackoverflow.com/questions/13792213/algorithm-for-generating-a-bracket-model-list-in-python
		Input:
			arr:
			dept:
			me:
		Output:
	"""
	def divide(arr, depth, m):
    if len(complements) <= depth:
        complements.append(2 ** (depth + 2) + 1)
    complement = complements[depth]
    for i in range(2):
        if complement - arr[i] <= m:
            arr[i] = [arr[i], complement - arr[i]]
            divide(arr[i], depth + 1, m)

	""" Function to update the status of the bracket
		Input:
		Output:
	"""
	def update_bracket(self):
		print("TODO")