
import os
from flask import Flask
from src.extensions import db, ma, migrate
from src.context_processors import inject_static_url
from src.logs import register_logging

from flask import jsonify, make_response
from flask import render_template
from flask import request
from flask import url_for

def create_app():
    config = os.environ.get('CONFIG', 'src.settings.DevConfig')
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    register_context_processors(app)
    register_logging(app, config)
    return app

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

def register_blueprints(app):
    from src.pdfhook import blueprint as pdfhook
    app.register_blueprint(pdfhook)

def register_context_processors(app):
    app.context_processor(inject_static_url)



if __name__ == '__main__':
    create_app().run()
