
contrasena= (input("agregar una contrasena com 10 caracteres: "))
import re
def validar(contrasena):
    criterios=[]
    if len(contrasena)<10:
        criterios.append("deben de tener minimo 10 caracteres")

   #aqui es para que tenga la contrasena una mayuscula
    if not re.search(r"[A-Z]",contrasena):
        criterios.append("deben de tener una letra mayusculas")
         #aqui debe tener la caractere de minuscula la contrasena
    if not re.search(r"[a-z]",contrasena):
        #.append sirve para agregar elementos a una lista existente
        criterios.append("deben de tener una caracter minuscula")
    if not re.search(r"\d",contrasena):
        criterios.append("debe de contener un numero")
    if not re.search(r"[?¡!,.]",contrasena):
        criterios.append("debe de tener un signo de estos :?¡!,")

    if criterios:
        return "la contrasena  no es segura . "+" " .join(criterios) 
    else:
        return" la contrasena es segura"
resultado = validar(contrasena)
print(resultado)


#ehercicio 2
moneda=int(input("diga  la cantidad de la moneda mexicana que quiere convercionar =   "))
paises = {  
    "estados_unidos": 0.055 * moneda,
     "EUR": 0.050 * moneda,

   }
print ( paises)


#ejercicio 3
botos=(input("dime el nombre del que desea votar, alan ,sergio, gonzalo  :  "))
agregar=(input("si no esta el candidato puedes agregar y si no saltarte esta parte=    "))
candidatos={
    "alan": 0,
    "sergio":  0,
    "gonzalo": 0,
    "nuevo candidato " :agregar
}
candidatos[botos]+=1
print(candidatos)

#ejerccicio4
palabras= []
while True :
 palabras = input("ingresa una palabra")
 if palabras.lower() == "salir":
     break
 palabras.append(palabras)
print("las palabras son : ",palabras)