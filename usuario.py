import requests
import json

class Usuario:
	nombre=''
	def __init__(self):
		self.url = "https://graph.facebook.com/v2.8/me"
		self.token = "EAACEdEose0cBAMqAWYXqQhlVK54kGA0tSCHYws79ujrLdgfEeqK1KQIFld26Whk0LpI4FyF9h9Egi22fj6VIwTrPNjNkHNYsXRoFZAs021q6IslAx6mRHMzTE2CWLYiXwvCkOlPoTcSWpGrbwDhdUmjPlorka4JgUIzf5BRgBHAJ5TfLxPwGWv4qi8FLrv0hTKl1KpAZDZD"

	def obtenInformacion(self):
		parametros = {'access_token': self.token}
		resultado = requests.get(self.url, params = parametros).json()
		print(resultado)
		return resultado

	def publicarComentario(self,message):
		self.url = "http://graph.facebook.com/v2.8/feed"
		parametros = {'message':message,'access_token':self.token}
		resultado = requests.post(self.url, params=parametros).json()
		print(resultado)
		return resultado