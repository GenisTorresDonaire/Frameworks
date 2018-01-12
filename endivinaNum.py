from bottle import route,run,template,get,request,redirect
from random import randint

@route('/hello', method='GET')
def index():
	numeroAdivinar = randint(0, 100)

	num = request.GET.get('numeroEnviado')

	if num and numeroAdivinar:
		if numeroAdivinar == int(num):
			return template('template_endivinaNumFelicidades.tpl', numeroAdivinar=numeroAdivinar)

		if numeroAdivinar < int(num):
			return template('template_endivinaNumMasPeque.tpl', numeroAdivinar=numeroAdivinar, num=num)

		if numeroAdivinar > int(num):
			return template('template_endivinaNumMasGrand.tpl', numeroAdivinar=numeroAdivinar, num=num)
		else:
			return template('template_endivinaNum.tpl', numeroAdivinar=numeroAdivinar, num=num)
	else:
		return template('template_endivinaNum.tpl', numeroAdivinar=numeroAdivinar, num=num)

run(host='localhost', port=8080)