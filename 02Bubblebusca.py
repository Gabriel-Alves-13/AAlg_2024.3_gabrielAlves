import csv
import time  # Importa a biblioteca time para medir o tempo de execução

# Função Bubble Sort
def bubble_sort(arr, index):
    n = len(arr)
    
    # Percorre toda a lista
    for i in range(n):
        # A cada passagem, o maior elemento "borbulha" até a última posição não ordenada
        for j in range(0, n - i - 1):
            # Compara os valores na coluna específica (index)
            if arr[j][index] > arr[j + 1][index]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Função de Busca Linear para encontrar uma linha específica
def linear_search(arr, value):
    # Percorre cada linha da lista e verifica se a linha é igual ao valor procurado
    for i, row in enumerate(arr):
        if row == value:
            return i, row  # Retorna o índice da linha e a linha correspondente
    return -1, None  # Retorna -1 se o valor não for encontrado

# Função de Busca Binária para encontrar uma linha específica
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
def sort_csv(input_filename, column_index):
    # Lê o arquivo CSV
    with open(input_filename, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        # Lê todas as linhas do CSV
        rows = list(reader)
        
    # Chama o Bubble Sort para ordenar com base na coluna especificada
    bubble_sort(rows[1:], column_index)  # Ignora o cabeçalho (linha 0)
    
    # Sobrescreve o arquivo CSV com os dados ordenados
    with open(input_filename, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        # Escreve o cabeçalho e as linhas ordenadas
        writer.writerow(rows[0])  # Cabeçalho
        writer.writerows(rows[1:])  # Dados ordenados

# Exemplo de uso:
input_filename = input("Digite o nome do arquivo CSV (ex: dados.csv): ")  # Nome do arquivo de entrada
column_index = int(input("Digite o índice da coluna que deseja ordenar (começa em 0): "))  # Índice da coluna

# Medir o tempo de execução da ordenação
start_time = time.time()  # Marca o tempo de início

# Chama a função para ordenar e sobrescrever o arquivo
sort_csv(input_filename, column_index)

# Marca o tempo de término da ordenação
end_time = time.time()

# Calcula o tempo de execução para ordenação
execution_time = end_time - start_time

print(f"O arquivo '{input_filename}' foi ordenado com sucesso!")
print(f"Tempo de execução para ordenação: {execution_time:.4f} segundos")

# Definindo a linha exata a ser buscada
search_value = ["Alan Johnson Lee", "18", "39.0"]  # Valor da linha completa que queremos buscar

# Realiza a busca linear e mede o tempo
start_search_time = time.time()  # Marca o tempo de início da busca linear

# Realiza a busca linear
with open(input_filename, mode='r', newline='') as infile:
    reader = csv.reader(infile)
    rows = list(reader)

# Chama a função de busca linear
index, found_row = linear_search(rows[1:], search_value)  # Ignora o cabeçalho

# Marca o tempo de término da busca linear
end_search_time = time.time()

# Calcula o tempo de execução da busca linear
search_execution_time = end_search_time - start_search_time

# Exibe o resultado da busca linear
if index != -1:
    print(f"Valor encontrado na linha {index + 2}: {found_row}")  # index + 2 para considerar o cabeçalho
else:
    print(f"Valor '{'; '.join(search_value)}' não encontrado.")

# Exibe o tempo de execução da busca linear
print(f"Tempo de execução para a busca linear: {search_execution_time:.4f} segundos")

# Realiza a busca binária e mede o tempo
start_binary_search_time = time.time()  # Marca o tempo de início da busca binária

# Chama a função de busca binária
binary_index, binary_found_row = binary_search(rows[1:], search_value, column_index)  # Ignora o cabeçalho

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
print(f"Tempo de execução para a busca binária: {binary_search_execution_time:.4f} segundos")
