#Definir la función BubbleSort que tiene como fin evaluar la matriz que le ingresamos
# y organizarla por orden númerico de menor a mayor
def BubbleSort(Matriz):
    #Redefinimos el nombre de la matriz
    Matriz=M
    #tomamos el tamaño de la matriz a modo de entero
    int= n = len(M)
    #iniciamos el indice en 0
    int= i =0
    #apoyados en el indice iniciamos un ciclo while
    while i< n-1:
        #iniciamos otro indicer en este caso "j"
        int= j =0
        #apoyados en el indice "j" iniciamos otro ciclo while
        while j<n-i-1:
            #si el codigo 
            if M[j]["code"]>M[j+1]["code"]:
                temp=M[j]
                M[j]=M[j+1]
                M[j+1]=temp
            j=j+1
        i=i+1
    return M



M = [
    {"name": "Mariana", "code": 9},
    {"name": "Valentina", "code":5},
    {"name": "Isabella", "code": 7},
    {"name": "Sofía", "code": 3},
    {"name": "Juan", "code": 4},
    {"name": "Daniel", "code": 2},
    {"name": "Carlos", "code":6},
    {"name": "Camila", "code": 1},
    {"name": "Felipe","code": 10},
    {"name": "Andrés", "code": 8}
]

print(M,"\n")

BubbleSort(M)
print(M)