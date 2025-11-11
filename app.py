from flask import Flask
from flask_cors import CORS
import logging
from config import Config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    from blueprints.main import main_bp

    app.register_blueprint(main_bp)

    return app


app = create_app()


if __name__ == '__main__':
    app.run(
        debug=Config.DEBUG,
        host=Config.HOST,
        port=Config.PORT
    )