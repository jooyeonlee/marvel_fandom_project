from flask import Flask
from config import Config

#import blueprints
from .authentication.routes import auth
from .marvel.routes import character
from .api.routes import api

#import db
from .models import db, login
from flask_migrate import Migrate

app = Flask(__name__)

#register blueprints
app.register_blueprint(auth)
app.register_blueprint(character)
app.register_blueprint(api)

#configure app
app.config.from_object(Config)

#configure db
db.init_app(app)
migrate = Migrate(app, db)

#configure login
login.init_app(app)
login.login_view = 'auth.signin'
login.login_message = 'Please log in to see this page'
login.login_message_category = 'alert-info'

from .import routes
from .import models