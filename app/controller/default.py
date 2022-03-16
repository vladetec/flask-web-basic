from flask import render_template, request
from app import app, db
from app.model.entities import Pessoa

@app.route('/')
@app.route('/listagem')
def listagem():
	return "<h1>Sejam Bem Vindos </h1>"