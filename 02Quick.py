import csv
import time  # Importa o módulo time para medir o tempo de execução

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

def sort_csv(input_file, column_index):
    # Registrar o tempo de início
    start_time = time.time()
    
    # Abrir o arquivo CSV para leitura
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Captura o cabeçalho
        rows = list(reader)    # Captura as linhas de dados
    
    # Ordenar as linhas utilizando o Quicksort com base na coluna desejada
    sorted_rows = quicksort(rows, key=lambda x: x[column_index])
    
    # Imprimir o cabeçalho
    """print(','.join(header))"""
    
    # Imprimir as linhas ordenadas
    for row in sorted_rows:
        """print(','.join(row))"""
    
    # Calcular o tempo total de execução
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Imprimir o tempo que levou para ordenar
    print(f"\nTempo de execução: {elapsed_time:.6f} segundos")

# Exemplo de uso:
input_file = input("Digite o nome do arquivo CSV: ")  # Nome do arquivo CSV de entrada
column_index = int(input("Digite o índice da coluna para ordenar (começando de 0): "))  # Índice da coluna para ordenar

sort_csv(input_file, column_index)
