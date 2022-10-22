""" INFO:
  if the virtual env not running:
    - navigate to /raeda_project
    - run: source venv/bin/activate
  to test locally (running flask backend):
    - navigate to /raeda folder in terminal
    - run: python run.py
    - go to http://localhost:5000
"""


from flask import Flask, render_template, jsonify, request
# from flask_ngrok import run_with_ngrok

app = Flask(__name__, static_folder='static', static_url_path='')
# run_with_ngrok(app)

@app.route('/')
def index():
	data = {}
	return render_template('index.html',data=data)

@app.route('/api/requesttaxi', methods=['POST'])
def requesttaxi():
  data = {
    'from': request.args.get('from', default = '(0,0)', type = str),
    'to': request.args.get('to', default = '(4,4)', type = str),
  }
  print(data['from'])
  print(data['to'])
  # caitlin to do stuff
  return data
    
if __name__ == "__main__":
	app.run()
