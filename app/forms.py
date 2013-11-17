from flaskext import wtf
from flaskext.wtf import validators

class UserForm(wtf.Form):
	username = wtf.TextField('User Name', validators=[validators.Required()])
	
class RecommenderForm(wtf.Form):
	recommendertype = wtf.RadioField('Recommender Type',
		choices=[('recommender1','Recommender 1'),('recommender2','Recommender 2')])