from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
  
  return "<h1>Boldlink python 'hello' RestApi</h1>"


if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0")
