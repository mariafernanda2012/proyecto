mi_tupla=(1,2,3,4,5,)
print(mi_tupla[2])




numero1=float(input("agrega un numero para agregar ala tupla: "))
numero2=float(input("agrega otro numero para agregar ala tupla: "))
tupla2=mi_tupla + (numero1 ,numero2)
print("la nueva tupla es ",tupla2)

lista=list(tupla2)
print(lista)

def sumar(tupla):
    return sum (tupla)
 
resultado=sumar(tupla2)
print("la suma y la tupla es ", resultado)






#2
#crear un diccionario
nombre = input("Agrega un nuevo contacto: ") 
telefono = input("Agrega el número de teléfono: ") 
cual=input("cual  nombre deseas  buscar ,juan,fer,hola : ")

contactos = {
    'juan': '83732923',
    'fer': '38323293',
    'hola': '8343843'
}
# Add the new contact to the dictionary
contactos[nombre] = telefono
if cual in contactos:
    print(f'el numero de cual,cual es{contactos[cual]}')
else:
    print(f'{cual}no se encuentra en la lista')
    print(contactos)

          

