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
		
	def generate_movie_list(self):
		movie_list = ['movie1','movie2',self.recommender_to_use]
		movie_list.extend(self.users_to_query)
		return movie_list
	