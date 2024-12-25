import csv
import time  # Importa o módulo time para medir o tempo de execução

# Função Quicksort
def quicksort(arr, key=lambda x: x):
    # Caso base: lista com 0 ou 1 elementos já está ordenada
    if len(arr) <= 1:
        return arr
    
    # Escolher o pivô (neste caso, o último elemento da lista)
    pivot = arr[-1]
    
    # Dividir a lista em dois subarrays: um com elementos menores que o pivô, outro com os maiores
    left = [x for x in arr[:-1] if key(x) <= key(pivot)]
    right = [x for x in arr[:-1] if key(x) > key(pivot)]
    
    # Recursão: ordenar os subarrays e juntar o resultado
    return quicksort(left, key) + [pivot] + quicksort(right, key)

# Função de Busca Linear
def linear_search(arr, value):
    # Percorre cada linha da lista e verifica se a linha é igual ao valor procurado
    for i, row in enumerate(arr):
        if row == value:
            return i, row  # Retorna o índice da linha e a linha correspondente
    return -1, None  # Retorna -1 se o valor não for encontrado

# Função de Busca Binária
def binary_search(arr, value, index):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Encontra o meio da lista
        # Compara o valor da linha no índice especificado
        if arr[mid][index] == value[index]:
            return mid, arr[mid]
        elif arr[mid][index] < value[index]:
            low = mid + 1  # Valor está na metade superior
        else:
            high = mid - 1  # Valor está na metade inferior
    
    return -1, None  # Retorna -1 se o valor não for encontrado

# Função para ler, ordenar e salvar o arquivo CSV
def sort_csv(input_file, column_index):
    # Registrar o tempo de início da ordenação
    start_time = time.time()
    
    # Abrir o arquivo CSV para leitura
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Captura o cabeçalho
        rows = list(reader)    # Captura as linhas de dados
    
    # Ordenar as linhas utilizando o Quicksort com base na coluna desejada
    sorted_rows = quicksort(rows, key=lambda x: x[column_index])
    
    # Calcular o tempo total de execução da ordenação
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Imprimir o tempo que levou para ordenar
    print(f"\nTempo de execução para ordenar o arquivo com Quicksort: {elapsed_time:.6f} segundos")
    
    return header, sorted_rows

# Exemplo de uso:
input_file = input("Digite o nome do arquivo CSV: ")  # Nome do arquivo CSV de entrada
column_index = int(input("Digite o índice da coluna para ordenar (começando de 0): "))  # Índice da coluna para ordenar

# Realiza a ordenação e mede o tempo
header, sorted_rows = sort_csv(input_file, column_index)

# Definindo o valor que queremos buscar
search_value = ["Alan Johnson Lee", "18", "39.0"]  # Exemplo de valor a ser buscado

# Realiza a busca linear e mede o tempo
start_search_time = time.time()  # Marca o tempo de início da busca linear

# Realiza a busca linear
linear_index, linear_found_row = linear_search(sorted_rows, search_value)  # Busca linear

# Marca o tempo de término da busca linear
end_search_time = time.time()

# Calcula o tempo de execução da busca linear
search_execution_time = end_search_time - start_search_time

# Exibe o resultado da busca linear
if linear_index != -1:
    print(f"Valor encontrado na linha {linear_index + 2} (busca linear): {linear_found_row}")  # index + 2 para considerar o cabeçalho
else:
    print(f"Valor '{'; '.join(search_value)}' não encontrado (busca linear).")

# Exibe o tempo de execução da busca linear
print(f"Tempo de execução para a busca linear: {search_execution_time:.6f} segundos")

# Realiza a busca binária e mede o tempo
start_binary_search_time = time.time()  # Marca o tempo de início da busca binária

# Realiza a busca binária
binary_index, binary_found_row = binary_search(sorted_rows, search_value, column_index)  # Busca binária

# Marca o tempo de término da busca binária
end_binary_search_time = time.time()

# Calcula o tempo de execução da busca binária
binary_search_execution_time = end_binary_search_time - start_binary_search_time

# Exibe o resultado da busca binária
if binary_index != -1:
    print(f"Valor encontrado na linha {binary_index + 2} (busca binária): {binary_found_row}")  # index + 2 para considerar o cabeçalho
else:
    print(f"Valor '{'; '.join(search_value)}' não encontrado (busca binária).")

# Exibe o tempo de execução da busca binária
print(f"Tempo de execução para a busca binária: {binary_search_execution_time:.6f} segundos")
