from flask import Flask, g
from flask_login import LoginManager
import config


login_manager = LoginManager()

def create_app(debug=True):
    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)

    with app.app_context():
            import database
            database.get_db()
    
    from controllers.player_controller import player_bp
    app.register_blueprint(player_bp)
    from controllers.transfer_controller import transfer_bp
    app.register_blueprint(transfer_bp)
    from controllers.home_controller import home_bp
    app.register_blueprint(home_bp)
    from controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    login_manager.init_app(app)
    login_manager.login_view = "auth_bp.login"

    return app

app = create_app(True)

# if __name__ == '__main__':
#     app.run(debug=True)