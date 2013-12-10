import operator
import math
import os

def read_data(filename):
	data = {}
	numavg = {}
	finaldata = {}

	with open('app/'+filename) as f:
		for line in f:
			linedata = line.split()
			if data.has_key(int(linedata[0])):
				data[int(linedata[0])].update({ int(linedata[1]) : float(linedata[2]) })
			else:
				data.update({int(linedata[0]) : { int(linedata[1]) : float(linedata[2]) } } )



	return data

def read_movies(filename):
	data = {}
	with open('app/'+filename) as f:
		for line in f:
			linedata = line.split("|")
			data.update({ float(linedata[0]) : linedata[1] })
	return data

class RatingInfoGetter():
	
	def __init__(self):
		'''
		Movie recommender class
		'''
		self.movie_info_list = []
	
	def get_the_info(self):
		movie_data = read_data("u.data")
		movies = read_movies("u.item")
		movie_info = movies
		return movie_info