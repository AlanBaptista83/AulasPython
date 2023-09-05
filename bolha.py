def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Últimos i elementos já estão no lugar correto
        for j in range(0, n - i - 1):
            # Percorre o array da esquerda para a direita
            # Troca os elementos adjacentes se estiverem fora de ordem
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Exemplo de uso
array = [64, 34, 25, 12, 22, 11, 90]
resultado = bubble_sort(array)
print("Array ordenado:")
print(resultado)
