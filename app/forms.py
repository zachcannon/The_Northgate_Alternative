from flaskext import wtf
from flaskext.wtf import validators

class UserForm(wtf.Form):
	username = wtf.TextField('User Name', validators=[validators.Required()])