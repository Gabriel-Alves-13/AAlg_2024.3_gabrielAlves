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

# Medir o tempo de execução
start_time = time.time()  # Marca o tempo de início

# Chama a função para ordenar e sobrescrever o arquivo
sort_csv(input_filename, column_index)

# Marca o tempo de término
end_time = time.time()

# Calcula o tempo de execução
execution_time = end_time - start_time

print(f"O arquivo '{input_filename}' foi ordenado com sucesso!")
print(f"Tempo de execução: {execution_time:.4f} segundos")
