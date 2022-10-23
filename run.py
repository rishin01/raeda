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
from driver_backened.car_backend import taximain, taxiongoing
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
  return {}
  
@app.route('/api/inittaxi', methods=['POST'])
def inittaxi():
  data = json.loads(request.data)
  print(data['flatrate'])
  print(data['pricemin'])
  print(data['numcars'])
  global taxis_data
  taxis_data = taximain(data['flatrate'],data['pricemin'],data['numcars'])
  print(taxis_data)
  # x_init, y_init = init_locations()
  # taxi_id = add_taxi(x_init,y_init,data['flatrate'],data['pricemin'])
  return {}
  # return {'taxi_id':taxi_id}

@app.route('/api/matchtaxi', methods=['POST'])
def matchtaxi():
  data = json.loads(request.data)
  print(data)
  # taxi_id_p, taxi_name, taxi_coj, taxi_el = Match(data['fx'],data['fy'],data['tx'],data['ty'],zip(find_taxis())).match()
  id,name,coj,el = Match(data['fx'],data['fy'],data['tx'],data['ty'],zip(find_taxis())).match()
  global taxi_id_p
  taxi_id_p = id
  
  return {'name':name,'costofjourney':coj,'estimatedlen':el}

@app.route('/waiting')
def waiting():
  return render_template('waiting.html',data={
   'fx':request.args.get('fromx'),
   'fy':request.args.get('fromy'),
   'tx':request.args.get('tox'),
   'ty':request.args.get('toy')
  })

@app.route('/paired')
def paired():
  return render_template('paired.html',data={'name':request.args.get('name'),'costofjourney':request.args.get('coj'),'estimatedlen':request.args.get('el')}) #,'taxi_id':taxi_id
  # return render_template('index.html',data={})

@app.route('/endjourney')
def endjourneypage():
  return render_template('endjourney.html',data={})

@app.route('/api/endjourney', methods=['POST'])
def endjourney():
  print(taxi_id_p)
  passenger_end_journey(taxi_id_p);
  return {}

@app.route('/taxiadded')
def taxiadded():
  return render_template('taxiadded.html',data={})

@app.route('/api/taxitobeongoing', methods=['POST'])
def taxitobeongoing():
  print(taxis_data)
  taxiongoing(taxis_data)
  return {}

if __name__ == "__main__":
	app.run()
