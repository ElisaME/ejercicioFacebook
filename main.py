from usuario import Usuario

user = Usuario()
print(type(user))
print(user.nombre)

respuesta = user.obtenInformacion()
print(type(respuesta))

respuesta2 = user.publicarComentario('Hola')
print(respuesta2)