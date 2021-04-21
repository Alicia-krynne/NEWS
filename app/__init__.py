from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)
    #app.url_map.converters [ "re"] = Reconverter # custom converter registered to the flask

    #app.config.from_object(config_type)

    # Creating the app configurations

    app.config.from_object(config_options[config_name])
   
     # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .requests import configure_request
    configure_request(app)


    return app


#from werkzeug.routing import BaseConverter
'''
# Regular converter
class RegexConverter(BaseConverter):


    def __init__(self, url_map, *args):
        super(RegexConverter, self).__init__(url_map)
        self.regex = args[0]


   
'''