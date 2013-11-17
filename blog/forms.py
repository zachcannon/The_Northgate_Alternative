from flaskext import wtf
from flaskext.wtf import validators

class AddUserForm(wtf.Form):
	username = wtf.TextField('User Name', validators=[validators.Required()])
