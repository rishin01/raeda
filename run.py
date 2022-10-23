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
from match import Match
from blondie.token.scripts.blockchain_interaction import *
# from car_backend import taximain
# from flask_ngrok import run_with_ngrok

app = Flask(__name__, static_folder='static', static_url_path='')
# run_with_ngrok(app)

taxi_id_p = -1

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
  taxi_id_p = Match(find_taxis()).match()
  return {'paired':True}#,'taxi_id':taxi_id
  
@app.route('/api/inittaxi', methods=['POST'])
def inittaxi():
  data = json.loads(request.data)
  print(data['flatrate'])
  print(data['pricemin'])
  print(data['numcars'])
  # x_init, y_init = init_locations()
  # taxi_id = add_taxi(x_init,y_init,data['flatrate'],data['pricemin'])
  taximain(data['flatrate'],data['pricemin'],data['numcars']);
  return {}
  # return {'taxi_id':taxi_id}

@app.route('/waiting')
def waiting():
  return render_template('waiting.html',data={})
  # return render_template('waiting.html',data={'taxi_id':request.args.get('taxi_id')})

@app.route('/paired')
def paired():
  return render_template('paired.html',data={'name':'Bob car','costofjourney':'5','estimatedlen':'2'}) #,'taxi_id':taxi_id

@app.route('/api/endjourney', methods=['POST'])
def endjourney():
  passenger_end_journey(taxi_id_p);

@app.route('/taxiadded')
def taxiadded():
  return render_template('taxiadded.html',data={})

if __name__ == "__main__":
	app.run()
