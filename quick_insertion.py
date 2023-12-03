import random
import time
import matplotlib.pyplot as plt

def Quick_Sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return Quick_Sort(left) + middle + Quick_Sort(right)

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def generate_random_array(size):
    return [random.randint(1, 10000) for _ in range(size)]

def measure_time(sort_function, array):
    start_time = time.time()
    sort_function(array.copy())
    return time.time() - start_time

array_size = int(input("Ingrese el tamaño del arreglo: "))
random_array = generate_random_array(array_size)

# Lista para almacenar los tiempos de ejecución de cada algoritmo
tiempos = []

# Algoritmos de ordenamiento a probar
Ordenamientos = [Quick_Sort, insertion_sort]

# Medir el tiempo de ejecución para cada algoritmo
for algoritmo in Ordenamientos:
    tiempo = measure_time(algoritmo, random_array)
    tiempos.append(tiempo)
    print(f"{algoritmo.__name__}: {tiempo:.3f} segundos")

# Visualizar gráficamente los tiempos de ejecución
nombres_algoritmos = [algoritmo.__name__ for algoritmo in Ordenamientos]
plt.bar(nombres_algoritmos, tiempos)
plt.title('Tiempo de ejecución de Quick Sort y Insertion Sort')
plt.xlabel('Algoritmo')
plt.ylabel('Tiempo (segundos)')
plt.show()
