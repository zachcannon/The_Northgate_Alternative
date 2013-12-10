from app import app
from google.appengine.ext import db
from models import RecommenderUser
from movie_recommender import MovieRecommender
from forms import UserForm, RemoveUserForm
from decorators import login_required
from flask import render_template, flash, url_for, redirect, request, jsonify
from google.appengine.api import users

@app.route('/')
def redirect_to_home():
	return redirect(url_for('manage_users'))
	
@app.route('/manage_users')
def manage_users():			
	recommender_users = RecommenderUser.all()
	form = UserForm()
	remove_user_form = RemoveUserForm()
	
	return render_template('manage_users.html', 
		recommender_users = recommender_users, 
		form=form,
		remove_user_form=remove_user_form)

@app.route('/load_preformed_group', methods = ['POST'])	
def add_preformed_group():
	if request.method == 'POST':	
		q = db.GqlQuery("SELECT * FROM RecommenderUser")
		results = q.fetch(15)
		for result in results:
			flash('Removing ' + result.username + ' from the db.')
			result.delete()
			
		group_members = request.form['group']
		group_members_list = eval(group_members)
		for member in group_members_list:
			recommenderuser = RecommenderUser(username = str(member))
			recommenderuser.put()
		
		return redirect(url_for('manage_users'))

@app.route('/add_recommender_user', methods = ['GET', 'POST'])
def add_recommender_user():
	form = UserForm()
	if form.validate_on_submit():
		recommenderuser = RecommenderUser(username = form.username.data)		
		recommenderuser.put()
		flash('New user ' +form.username.data+ ' added to list')
		return redirect(url_for('manage_users'))

@app.route('/remove_user', methods = ['POST'])
def remove_user():		
	form = RemoveUserForm()
	flash('MADE IT IN!')
	if request.method == 'POST':
		flash(form.usertodelete.data)
		#Long Mai states: Shy away from direct text queries, GOD DAMN IT!
		q = db.GqlQuery("SELECT * FROM RecommenderUser where username = :1", form.usertodelete.data)
		results = q.fetch(10)
		for result in results:
			flash('Removing ' + result.username + ' from the db.')
			result.delete()
		return redirect(url_for('manage_users'))

@app.route('/recommender_results', methods = ['POST'])
def group_recommend():
	recommender_users = RecommenderUser.all()
	recommender_to_use = request.form['recommender']
	users_for_search = []
	for user in recommender_users:
		users_for_search.append(int(user.username))	
	recommender = MovieRecommender()
	recommender.populate_users(users_for_search, recommender_to_use)		
	results = recommender.generate_movie_list()
	return jsonify({'movies': results})