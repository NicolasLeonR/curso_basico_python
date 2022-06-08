#Ingresamos una variable
calificacion=input("Ingresa la calificación: ")
calificacion=int(calificacion)
#Pregunta si la calificación es mayora 700
if calificacion < 700 and calificacion>0:
    print("Repruebas")
elif calificacion == 700:
    print("Pansas")
elif calificacion>1000 or calificacion<0:
    print("No es cierto")
else :
    print("Felicidades")

#Verifica si eres mayor de edad
edad=input("Introduce tu edad: ")
edad=int(edad)

if edad >= 18 and edad <=115:
    print("Bienvenido al mamitas")
elif edad >115:
    print("Si vienes acompañado de tus abuelitos te podemos fiar")
elif edad < -5:
    print("Ni que fueras viajero del tiempo")
else:
    print("No puedes llevarte esos cigarros")