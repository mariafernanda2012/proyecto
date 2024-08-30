#elaborar una lista de 7 numeross
#ay modificar dos elemento

numeros=["1","6" , "8" , "10" , "23", "56" , "5"] 
numeros[4]="5"
print(numeros)

#elabra una listaa de frutas de tu gusto
#y que al usuarlo puede cambbiar la fruta la cual es de su gradoss
# y que se guarde en la lista nueva´
frut = ['Mango', 'Fresa', 'Uva', 'Piña', 'Manzana', 'Platano']
print("Esta es la lista de frutas: ")
for i, fruta in enumerate(frut):
    print(f"{i+1}. {fruta}")

cambio_frut = int(input("¿Cuál te gustaría cambiar? (ingresa el número de la fruta) ")) - 1
nueva_frut = input("¿Cuál es la nueva? ")

frut[cambio_frut] = nueva_frut
print(frut)
   



#realiza una listaa que contega elementos dee dierentes tipos numero ay un valor +
#ay con un pueda mostrar lo que contiene
