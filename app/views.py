from app import app
from google.appengine.ext import db
from models import RecommenderUser
from forms import UserForm
from decorators import login_required

from flask import render_template, flash, url_for, redirect

from google.appengine.api import users

@app.route('/')
def redirect_to_home():
	return redirect(url_for('list_users'))
	
@app.route('/list_users', methods = ['GET', 'POST'])
def list_users():			
	recommender_users = RecommenderUser.all()
	return render_template('list_recommender_users.html', recommender_users = recommender_users)

@app.route('/add_recommender_user', methods = ['GET', 'POST'])
def add_recommender_user():
	form = UserForm()
	if form.validate_on_submit():
		recommenderuser = RecommenderUser(username = form.username.data)		
		recommenderuser.put()
		flash('New user added to list')
		return redirect(url_for('list_users'))
		
	return render_template('new_user.html', form=form)

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
	return render_template('remove_user.html', form=form)