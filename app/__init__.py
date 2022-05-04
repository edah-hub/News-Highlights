from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options



def create_app(config_name):
# Initializing application
    # app = Flask(__name__,instance_relative_config = True)
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(config_options[config_name])


        # Registering main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # Setting up configuration
    from .requests import configure_request
    configure_request(app)
    
    
    return app

# from . import views
# from . import error