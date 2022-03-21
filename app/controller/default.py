from flask import render_template, request
from app import app, db
from app.model.entities import Pessoa

@app.route('/')
@app.route('/listagem')
def listagem():
	lista_pessoas = [
		{'id': 1, 'nome': "Maria Silva", 'idade': 30, 'sexo': 'F', 'salario': 5000},
		{'id': 2, 'nome': "Jose Silva", 'idade': 25, 'sexo': 'M', 'salario': 3000},
		{'id': 3, 'nome': "Joao Silva", 'idade': 20, 'sexo': 'M', 'salario': 2000}
	]
	return render_template('home.html', pessoas=lista_pessoas, ordem='ID' )