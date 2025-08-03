import os
from flask import Flask
from dotenv import load_dotenv
from auth.login import LoginManager
from routes.catch import catch_pokemon
from routes.challenge import challenge_trainer
from routes.region import get_daily_region

load_dotenv()
SECRET_KEY = "SECRET_KEY"

app = Flask(__name__)
app.config[SECRET_KEY] = os.getenv(SECRET_KEY)

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def home():
    return "Welcome to the Pokemon Fan App!"

@app.route('/catch', methods=['POST'])
def catch():
    return catch_pokemon()

@app.route('/challenge', methods=['POST'])
def challenge():
    return challenge_trainer()

@app.route('/daily-region', methods=['GET'])
def daily_region():
    return get_daily_region()

if __name__ == '__main__':
    app.run(debug=True)
