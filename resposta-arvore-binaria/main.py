import random
import BinaryTree as bt

if __name__ == '__main__':
    tamanho = int(input("Informe o tamanho da lista: "))
    random.seed(tamanho)
    # Adiciona o primeiro valor à árvore binária ou seja o primeiro nó
    l = bt.BinaryTree(random.randint(0, 2**17))
    # contador de elementos que começa em 1 pois já adicionamos o primeiro
    count = 1

    # Adiciona elementos à árvore binária com base no tamanho
    while count < tamanho:
        num = random.randint(0, 2**17)
        if not l.contains(num):  # Verifica se o número já está na árvore
            l.put(num)
            count += 1

    alvo = random.randint(0, 2**17)
    while alvo % 2 == 0:
        alvo = random.randint(0, 2**17)

    # Encontrar o número de pares cujo complemento soma para o valor alvo
    complement_count = l.find_complement(alvo)
    print(f"Número de pares cujo complemento soma para {
          alvo}: {int(complement_count/2)}")
