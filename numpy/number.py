import numpy as np

# Bubble Sort com NumPy
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Criar um array NumPy
arr = np.array([64, 34, 25, 12, 22, 11, 90])

print("Array original:", arr)

# Aplicar o Bubble Sort no array
bubble_sort(arr)

print("Array ordenado:", arr)
