#crear un programa 1.
#revisar si ya existe un usuario registrado
#si no hay usuario pedirle al usuario que se registre con nombre,email y contraseña
#una vez registrado pedir que inicie sesion con su email y contraseña
#despues pedir una cantidad y convertirla a dolares

nombreusuario=""
emailusuario=""
contrasena=""

emailiniciodesesion=""
contrasenaIniciodeSesion=""
cantidadDolar=""
resultadoDeConversion=""

if emailusuario=="" and contrasena=="":
    print("por favor registrate")
    nombreusuario = input("ingresa el nombre de usuario ")
    emailusuario = input("ingresa tu correo electronico")
    contrasena = input("ingresa tu contraseña")

print("porfavor inicia sesion")
emailinicioSesion=input("ingresa tu correo electronico")
contrasenaInicioSesion=input("ingresa tu contraseña ")

if emailinicioSesion == emailusuario and contrasena == contrasenaIniciodeSesion:
    cantidadDolar = int(input("ingresa una cantidad para convertir a dolares"))
    resultadoDeConversion=cantidadDolar/17.47
    print("La cantidad ",cantidadDolar, " es igual a ",resultadoDeConversion)
else:
    print("los valores ingresados son incorrectos")