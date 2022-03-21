from flask import render_template, request
from app import app, db
from app.model.entities import Pessoa

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')