from flask import Flask, g
import config

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

    return app

app = create_app(True)

@app.route('/')
def index():
    return "App is working!"

# if __name__ == '__main__':
#     app.run(debug=True)