from blog import app
from models import RecommenderUser
from forms import AddUserForm
from decorators import login_required

from flask import render_template, flash, url_for, redirect

from google.appengine.api import users

#Default pages/routes with template
@app.route('/')
def redirect_to_home():
	return redirect(url_for('list_users'))
	
#Added pages/routes for TNGA
@app.route('/list_users')
def list_users():
	recommender_users = RecommenderUser.all()
	return render_template('list_recommender_users.html', recommender_users = recommender_users)

@app.route('/add_recommender_user', methods = ['GET', 'POST'])
def add_recommender_user():
	form = AddUserForm()
	if form.validate_on_submit():
		recommenderuser = RecommenderUser(username = form.username.data)
		
		recommenderuser.put()
		flash('New user added to list')
		return redirect(url_for('list_users'))
		
	return render_template('new_user.html', form=form)

	