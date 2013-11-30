from flaskext import wtf
from flaskext.wtf import validators

class RemoveUserForm(wtf.Form):
	usertodelete = wtf.HiddenField('User To Delete')

class UserForm(wtf.Form):
	username = wtf.TextField('User Name', validators=[validators.Required()])
	