#ejercicio 1
lista= ["Python", "Java", "C++", "Python", "JavaScript", "Python", "C#"]
print("cuantos python tiene",lista.count("Python"))

#ejercicio 2
frases = ["hola", "mundo", "python", "es", "genial"]
print("frase a mayuscula")
for i in range(len(frases)):
    frases[i] = "".join([chr(ord(c) - 32) for c in frases[i]])
print(frases)
#Dada una lista de palabras, elimina todas aquellas palabras que tengan menos de 4 caracteres.
palabras = ["sol", "luna", "cielo", "mar", "estrella", "pez"]
numeramos=[palabras for palaabra in palabras if len (palabras)>=4]
print(numeramos)