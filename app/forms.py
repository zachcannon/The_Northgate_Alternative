from flaskext import wtf
from flaskext.wtf import validators

class RemoveUserForm(wtf.Form):
	usertodelete = wtf.HiddenField('User To Delete')

class UserForm(wtf.Form):
	username = wtf.TextField('User Name', validators=[validators.Required()])
	
class RecommenderForm(wtf.Form):
	recommendertype = wtf.SelectField('Select a recommender to use...',
		choices=[('recommender1','Recommender 1'),('recommender2','Recommender 2')])