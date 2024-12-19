import time
import multiprocessing

# Función de búsqueda binaria
def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

# Búsqueda secuencial
def sequential_binary_search(arr, target):
    return binary_search(arr, target, 0, len(arr) - 1)

# Función para realizar la búsqueda binaria paralela
def parallel_binary_search(arr, target, processes_amount=4):
    pool = multiprocessing.Pool(processes=processes_amount)
    step = len(arr) // processes_amount

    results = []
    for i in range(processes_amount):
        start = i * step
        end = (i + 1) * step if i != processes_amount - 1 else len(arr)
        # En lugar de obtener futuros, hacemos que la ejecución de cada hilo sea asincrona
        result = pool.apply_async(binary_search, args=(arr, target, start, end - 1))
        results.append(result)

    pool.close()
    pool.join()

    for result in results:
        # Reunimos todos los resultados obtenidos asincronamente
        res = result.get()
        if res != -1:
            return res
    return -1

# Función para medir tiempos
def compare_times(arr, target):
    print(f"Cantidad de elementos: {len(arr)}")
    
    # Medir tiempo secuencial
    start_time = time.perf_counter()
    seq_result = sequential_binary_search(arr, target)
    seq_time = time.perf_counter() - start_time
    print(f"Resultado no paralelo: {seq_result}, Tiempo: {seq_time:.6f} segundo")

    # Medir tiempo paralelo
    start_time = time.perf_counter()
    par_result = parallel_binary_search(arr, target)
    par_time = time.perf_counter() - start_time
    print(f"Resultado paralelo: {par_result}, Tiempo: {par_time:.6f} segundo")


if __name__ == "__main__":
    # Probar con diferentes tamaños de lista
    for size in [10**5, 10**6, 10**7]:
        arr = list(range(size))
        target = size - 1  # Último valor
        compare_times(arr, target)
