import timeit
import matplotlib.pyplot as plt
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def benchmark_algorithm(sort_func, input_size):
    setup_code = f"from __main__ import {sort_func}, random; arr = [random.randint(1, 1000) for _ in range({input_size})]"
    stmt_code = f"{sort_func}(arr)"

    execution_time = timeit.timeit(stmt=stmt_code, setup=setup_code, number=100)
    return execution_time

# Benchmarking for different input sizes
input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
algorithms = ["insertion_sort", "selection_sort", "bubble_sort"]

results = {alg: [] for alg in algorithms}

for size in input_sizes:
    for alg in algorithms:
        execution_time = benchmark_algorithm(alg, size)
        results[alg].append(execution_time)

# Plotting the results
for alg in algorithms:
    plt.plot(input_sizes, results[alg], label=alg)

plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (s)')
plt.title('Algorithm Benchmarking')
plt.legend()
plt.show()
import timeit
import matplotlib.pyplot as plt
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def benchmark_algorithm(sort_func, input_size):
    setup_code = f"from __main__ import {sort_func}, random; arr = [random.randint(1, 1000) for _ in range({input_size})]"
    stmt_code = f"{sort_func}(arr)"

    execution_time = timeit.timeit(stmt=stmt_code, setup=setup_code, number=100)
    return execution_time

# Benchmarking for different input sizes
input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
algorithms = ["insertion_sort", "selection_sort", "bubble_sort"]

results = {alg: [] for alg in algorithms}

for size in input_sizes:
    for alg in algorithms:
        execution_time = benchmark_algorithm(alg, size)
        results[alg].append(execution_time)

# Plotting the results
for alg in algorithms:
    plt.plot(input_sizes, results[alg], label=alg)

plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (s)')
plt.title('Algorithm Benchmarking')
plt.legend()
plt.show()
