# THIS IS THE CONTROLLER / WAITER DIRECTING TRAFFIC 🚦

# ---- YOUR APP STARTS HERE ----

# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
# route to index page
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
  
# route to the results page
@app.route('/results', methods=['POST', 'GET']) 
def results():
  if request.method == "POST": #if user clicks submit 
    name = request.form['name'].title() #user's name is stored
    genre = request.form['selector'] #user's genre is stored
    rec, titles_list, images_list, syn_list = model.getRec(genre) #calls getRec(genre) function in model.py
    return render_template('results.html', name=name, genre=genre, rec=rec, titles_list=titles_list, images_list=images_list, syn_list=syn_list) #returns results page with all info needed
    
  else: #if user goes directly to results page w/o completing form on index
    return "ERROR: You are getting the page, please do the form first!" 








	
	
# This keeps us in debug mode so you don't have to constantly refresh
app.run(host='0.0.0.0', port=81, debug=True)