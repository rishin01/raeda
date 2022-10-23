""" INFO:
  if the virtual env not running:
    - navigate to /raeda_project
    - run: source venv/bin/activate
  to test locally (running flask backend):
    - navigate to /raeda folder in terminal
    - run: python run.py
    - go to http://localhost:5000
"""

import json
import random
from flask import Flask, render_template, jsonify, request
# from flask_ngrok import run_with_ngrok

app = Flask(__name__, static_folder='static', static_url_path='')
# run_with_ngrok(app)

@app.route('/')
def index():
	data = {}
	return render_template('index.html',data=data)

@app.route('/taxi')
def taxi():
  data = {}
  return render_template('taxi.html',data=data)

@app.route('/api/requesttaxi', methods=['POST'])
def requesttaxi():
  data = json.loads(request.data)
  print(data['from'])
  print(data['to'])
  # caitlin to do stuff
  return {'paired':True}
  
@app.route('/api/inittaxi', methods=['POST'])
def inittaxi():
  data = json.loads(request.data)
  print(data['flatrate'])
  print(data['pricemin'])
  x_init, y_init = init_locations()
  #sc.add_taxi(x_init,y_init,data['flatrate'],data['pricemin'],1)
  return render_template('taxiadded.html',data={})

@app.route('/waiting')
def waiting():
  return render_template('waiting.html',data={})

if __name__ == "__main__":
	app.run()
