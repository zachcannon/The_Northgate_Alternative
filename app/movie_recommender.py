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

class MovieRecommender():
	
	def __init__(self):
		'''
		Movie recommender class
		'''
		self.users_to_query = []
		self.recommender_to_use = ''
	
	def populate_users(self, users, recommender):
		self.users_to_query = users
		self.recommender_to_use = recommender
		
	def get_avg(self, user_list, movie_data):
		groupr = {}
		numr = {}
		for u in user_list:
			ur = movie_data[u]			
			for r in ur:
				if groupr.has_key(r):
					groupr[r] = (groupr[r]*numr[r]+ur[r])/(numr[r]+1)
					numr[r] = numr[r]+1
				else:
					groupr.update( { r: ur[r]} )
					numr.update({ r:1 })
					
		return groupr

	def find_closest_user(self, group, userd, md):
		luserd = 0
		for r in userd:
			luserd = luserd + userd[r]*userd[r]
		luserd = math.sqrt(luserd)
		delta = 0
		closest = 0
		numsame = 0
		for other in md:
			if other not in group:
				dother = 0
				otherdata = md[other]
				for r in otherdata:
					dother = dother + otherdata[r]*otherdata[r]
				dother = math.sqrt(dother)

				inter = list(set(otherdata.keys()) & set(userd.keys()))
				dot = 0
				for m in inter:
					dot = dot + userd[m]*otherdata[m]
				if (dot / (luserd*dother) > delta ):
					closest = other
					delta = dot/(luserd*dother)
					numsame = len(inter)
		return closest
	
	def generate_movie_list(self):
		movie_data = read_data("u.data")
		movies = read_movies("u.item")
		
		userd = self.get_avg(self.users_to_query, movie_data)
		
		other = self.find_closest_user(self.users_to_query, userd, movie_data)
		
		reccomend = movie_data[other]
	
		movie_list = ['Users in group', self.users_to_query, 'Recommender used',self.recommender_to_use,'Movies Recommended']
		i=0
		for m in sorted(reccomend, key=reccomend.get, reverse=True):
			movie_list.append( movies[m] )
			i = i+1
			if i>9:
				break
		

		return movie_list
	