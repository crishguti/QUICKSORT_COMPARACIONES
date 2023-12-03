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


def Merge_Sort(arr):
    if len(arr) == 1:
        return arr

    middle = len(arr) // 2
    left_array = arr[:middle]
    right_array = arr[middle:]

    sorted_left_array = Merge_Sort(left_array)
    sorted_right_array = Merge_Sort(right_array)

    return Merge(sorted_left_array, sorted_right_array)


def Merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


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
Ordenamientos = [Quick_Sort, Merge_Sort]

# Medir el tiempo de ejecución para cada algoritmo
for algoritmo in Ordenamientos:
    tiempo = measure_time(algoritmo, random_array)
    tiempos.append(tiempo)
    print(f"{algoritmo.__name__}: {tiempo:.3f} segundos")

# Visualizar gráficamente los tiempos de ejecución
nombres_algoritmos = [algoritmo.__name__ for algoritmo in Ordenamientos]
plt.bar(nombres_algoritmos, tiempos)
plt.title('Tiempo de ejecución de Quick Sort y Merge Sort')
plt.xlabel('Algoritmo')
plt.ylabel('Tiempo (segundos)')
plt.show()
