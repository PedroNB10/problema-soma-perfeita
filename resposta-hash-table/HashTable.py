import random

class HashTable:
    def __init__(self, size):
        # Inicializar a tabela hash com o tamanho informado
        self.size = size
        # Cada slot é uma lista vazia inicialmente para caso de colisão o elemento ser inserido na lista
        self.slots = [[] for _ in range(size)]
        # Contador de elementos inseridos
        self.count = 0

    # Função de hash, que retorna o resto da divisão do número informado pelo tamanho da tabela
    def _hash(self, value):
        return value % self.size

    # Função para inserir um elemento na tabela
    def put(self, value):
        # Calcular o hash do elemento
        hash_key = self._hash(value)

        # Verificar se o valor já existe na tabela
        if not self.contains(value):
            self.slots[hash_key].append(value)
            self.count += 1  # Incrementar o número de elementos inseridos

    # verifica se o valor está na tabela
    def contains(self, value):
        hash_key = self._hash(value)
        return value in self.slots[hash_key]


if __name__ == '__main__':

    size = int(input("Informe o tamanho da lista: "))
    print("\nTamanho da lista informado: ", size)
    random.seed(size)
    # Criação da Tabela hash com o total de slots equivalente ao tamanho informado
    hashtable = HashTable(size)

    # Inserir elementos aleatórios na tabela hash
    while hashtable.count < size:
        num = random.randint(0, 2**17)
        hashtable.put(num)

    target = random.randint(0, 2**17)
    while target % 2 == 0:
        target = random.randint(0, 2**17)

    # Contar pares cujo complemento soma para o alvo
    count = 0

    for slot in hashtable.slots:
        for num in slot:
            compl = target - num
            if compl != num and hashtable.contains(compl):
                count += 1

    print(f"Número de pares cujo complemento soma para {
          target}: {int(count/2)}")
