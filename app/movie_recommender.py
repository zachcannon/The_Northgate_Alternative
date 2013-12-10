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
	
	def populate_users(self, users):
		self.users_to_query = users
		
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
		delta = [0]*15
		closest = [0]*15
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
				d = dot/(luserd*dother)
				i = 0
				flag = True
				for dd in delta:
					if d > dd and flag:
						delta.insert(i,d)
						closest.insert(i,other)
						delta.remove( delta[ len(delta)-1 ] )
						closest.remove( closest[ len(closest)-1 ] )
						flag = False
					i = i+1
		return closest
		
	def get_rec(self, otherdata, group, md):
		user1 = otherdata[0]
		results = {}
		for m in user1:
			numsame = 0
			s = 0
			for otheruser in otherdata:
				if m in otheruser:
					numsame = numsame+1
					s = s + otheruser[m]
				if numsame > (len(otherdata)/2):
					avg = s / numsame
					numseen = 0
					for u in group:
						if m in md[u]:
							numseen = numseen + 1
					if numseen <= (len(group)/3):
						results.update( { m:avg } )
		return results
	
	def generate_movie_list(self):
		movie_data = read_data("u.data")
		movies = read_movies("u.item")
		
		users = self.users_to_query
		userd = self.get_avg(users, movie_data)
		
		other = self.find_closest_user(users, userd, movie_data)
		otherdata = [ movie_data[other[0]] ,movie_data[other[1]] ,movie_data[other[2]]  ]
		reccomend = self.get_rec(otherdata, users, movie_data)
	
		movie_list = []
		i=0
		for m in sorted(reccomend, key=reccomend.get, reverse=True):
			movie_list.append( movies[m] )
			i = i+1
			if i>9:
				break
		

		return movie_list
	