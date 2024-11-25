from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    with app.app_context():
        # Import and register blueprints
        from app import routes
        app.register_blueprint(routes.bp)
        
        return app
