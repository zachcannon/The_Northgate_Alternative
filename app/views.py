from app import app
from google.appengine.ext import db
from models import RecommenderUser
from movie_recommender import MovieRecommender
from forms import UserForm
from decorators import login_required
from flask import render_template, flash, url_for, redirect
from google.appengine.api import users

@app.route('/')
def redirect_to_home():
	return redirect(url_for('list_users'))
	
@app.route('/list_users')
def list_users():			
	recommender_users = RecommenderUser.all()
	form = UserForm()
	return render_template('manage_users.html', recommender_users = recommender_users, form=form)

@app.route('/add_recommender_user', methods = ['GET', 'POST'])
def add_recommender_user():
	form = UserForm()
	if form.validate_on_submit():
		recommenderuser = RecommenderUser(username = form.username.data)		
		recommenderuser.put()
		flash('New user ' +form.username.data+ ' added to list')
		return redirect(url_for('list_users'))

@app.route('/remove_user', methods = ['GET', 'POST'])
def remove_user():
	form = UserForm()	
	if form.validate_on_submit():
		q = db.GqlQuery("SELECT * FROM RecommenderUser where username = :1", form.username.data)
		results = q.fetch(10)
		for result in results:
			flash('Removing ' + result.username + ' from the db.')
			result.delete()
		return redirect(url_for('list_users'))

@app.route('/search_results')
def group_search():
	recommender_users = RecommenderUser.all()
	users_for_search = []
	for user in recommender_users:
		users_for_search.append(user.username)
	
	recommender = MovieRecommender()
	recommender.populate_users(users_for_search)
	results = recommender.generate_movie_list()
	
	return render_template('search_results.html', movies_returned=results)