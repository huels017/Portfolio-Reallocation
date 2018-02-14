from flask import Flask, current_app
from flask_assets import Environment, Bundle
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Register static assets

    assets = Environment(app)
    css = Bundle('css/lib/bootstrap/bootstrap.min.css',
    	'css/main.css',
    	output='gen/styles.css')
    js = Bundle('js/lib/bootstrap/bootstrap.bundle.min.js', output='gen/scripts.js')

    assets.register('all_css', css)
    assets.register('js', js)

    # Bootstrap(app)

    return app
