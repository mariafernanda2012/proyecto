 #tome dos matrices de igual tamaño (matrices bidimensionales) y devuelva una nueva matriz que sea la suma de las dos matrices original
matrix_1= [[1,2,3],
           [4,5,6],
           [7,8,9]]
print(f"esta es la primera matrix {matrix_1}")
matrix_2=[[3,4,5],
          [6,7,8],
          [8,9,0]]
#ay que agregar otra matrix que tenga puros ceros
resultado=[[0,0,0],
        [0,0,0],
        [0,0,0]]

print(f"esta es la segunda matrix{matrix_2}")
#para saber cual era matrix 1 puse la i y la j y asi las junte en el resutado 
for i in range(len(matrix_1)):
          #len es como para sumar
          for j in range(len(matrix_1)):
             #aqui junte las dos letras y las variables de matrix y las sume
             resultado[i][j] = matrix_1[i][j] + matrix_2 [i][j]
print("este es el resuktado",resultado)
#Escribe un programa que tome una matriz y devuelva su transpuesta (intercambiar filas por columnas) 
#utilizamps return ya que es una funcion que devuelve el valor a su lugar
matrix={{1,2,3},
        {4,5,6},
        {7,8,9}}
def transporte(matrix):
    return (matrix)  
print("este es el transpuesta ",matrix)