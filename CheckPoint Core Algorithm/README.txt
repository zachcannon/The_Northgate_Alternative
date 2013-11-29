For a demonstration of our core algorithm, this python
script takes in a list of users and outputs a list of
10 movie recommendations. The users are numbered from 1
to 1000, and the script takes in the lsit of users
as a space-separated list on one line. The algorithm takes
in the list of users and creates an "average" user by averaging
the ratings for movies that more than one user in the group
has rated. It then finds the closest user (that is not
in the group) to this average user by cosine similarity.
Then it chooses the top 10 movies from this user to use 
as recommendations. This is not our final algorithm, as we
plan to have the algorithm average the top k closest users
to the average user, and also incorporate genres and age
groups into the recommendation. In addition we also plan 
to have 2 recommendation algorithms: the "average user" algorithm,
as well as a "shoot for the fences" algorithm that aims less
to please everyone and more to recommend a movie that really 
suits one or more of the users in the group. Overall, this implementation
has the vast majority of the work done for our recommender, the 
rest of the work will just be tweaking this algorithm.
