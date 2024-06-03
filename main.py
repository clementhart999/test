from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

@app.route('/')
def home():
  return "HI"

app.run(host='0.0.0.0', port=8080)
