import os

DEBUG = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')
ADMIN_EMAILS = [
    # Put your admin emails here.
    'zach.cannon10@gmail.com'
]
SECRET_KEY = '123456789123456789123456'
