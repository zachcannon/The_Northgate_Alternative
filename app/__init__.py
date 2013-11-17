from flask import Flask
import settings

app = Flask('app')
app.config.from_object('app.settings')

import views
