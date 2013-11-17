class MovieRecommender():
	
	def __init__(self):
		'''
		Movie recommender class
		'''
		self.users_to_query = []
	
	def populate_users(self, users):
		self.users_to_query = users
		
	def generate_movie_list(self):
		movie_list = ['movie1','movie2']
		movie_list.extend(self.users_to_query)
		return movie_list
	