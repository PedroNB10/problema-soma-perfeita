import random
import BinaryTree as bt
import time

if __name__ == '__main__':
    starttime = time.time()
    size = int(input("Informe o tamanho da lista: "))
    print("\nTamanho da lista informado: ", size)
    random.seed(size)
    # Adiciona o primeiro valor à árvore binária, ou seja, o primeiro nó
    l = bt.BinaryTree(random.randint(0, 2**17))
    # Contador de elementos que começa em 1 pois já adicionamos o primeiro
    count = 1

    # Adiciona elementos à árvore binária com base no size
    while count < size:
        num = random.randint(0, 2**17)
        if not l.contains(num):  # Verifica se o número já está na árvore
            l.put(num)
            count += 1

    target = random.randint(0, 2**17)
    while target % 2 == 0:
        target = random.randint(0, 2**17)

    # Encontrar o número de pares cujo complemento soma para o valor target
    complement_count = l.find_complement(target)
    print(f"Número de pares cujo complemento soma para {
          target}: {int(complement_count/2)}")
    print(f"Tempo de execução: {time.time() - starttime} segundos")