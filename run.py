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

if __name__ == "__main__":
	app.run()
