# Edwin Yair Molina Cerón ------- 408873

def SelectionSort(A): # Este metodo define la función que recibe una lista.
    N = len(A) # Obtiene la cantidad de elemntos de la lista.
    i = 0 # Se inicializa el indice para que recorra la lista desde el inicio.

    while i < N - 1: # Mientras el indice sea menor a la cantidad de elemento hace que la ultima posición sea valida.
        minIndex = i # Asume que el indice es el menor.
        j = i + 1 # Hace que se inicialice j en la siguiente psoción de i.
        while j < N: # Mientras j este dentro del rango de la lista, entones...
            if A[j]["code"] < A[minIndex]["code"]:# Compara j con el minIndex.
                minIndex = j # Si se encuentra un número menor actualize minIndex.
            j = j + 1 # Hace que j avance al siguiente elemento.
        if minIndex != i: # Si minIndex es diferente del indice, entonces..
            A[i], A[minIndex] = A[minIndex], A[i] # MinIndex tendra el valor del indice y el indice tendra el valor de MinIndex
        i = i + 1 # Y esto hace i avance al siguiente elemento.

# Lista con los datos
A = [
    {"name": "Felipe", "code": 10},
    {"name": "Mariana", "code": 9},
    {"name": "Andrés", "code": 8},
    {"name": "Isabella", "code": 7},
    {"name": "Carlos", "code": 6},
    {"name": "Valentina", "code": 5},
    {"name": "Juan", "code": 4},
    {"name": "Sofía", "code": 3},
    {"name": "Daniel", "code": 2},
    {"name": "Camila", "code": 1}
]
SelectionSort(A) # Llamamos al metodo SelectionSort
for item in A: # Recorre la lista ya ordenada.
    print(item) # Imprime la lista.