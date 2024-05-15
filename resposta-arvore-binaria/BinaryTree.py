class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Adiciona elementos não repetidos
    def put(self, value):
        # Se o valor que estou tentando adicionar é igual ao valor da raiz não faço nada
        if value == self.value:
            return

        # Se o valor que estou tentando adicionar é menor que o valor da raiz
        elif value < self.value:
            if self.left == None:
                self.left = BinaryTree(value)
            else:
                self.left.put(value)
        # Se o valor que estou tentando adicionar é maior que o valor da raiz
        else:
            if self.right == None:
                self.right = BinaryTree(value)
            else:
                self.right.put(value)

    def print(self):
        print("(", end="")
        if self.left != None:
            self.left.print()

        print(str(self.value), end="")

        if self.right != None:
            self.right.print()
        print(")", end="")

    # Verifica se o valor está na árvore por meio da busca binária
    def contains(self, value):
        if self.value == value:
            return True
        
        elif value < self.value and self.left != None:
            return self.left.contains(value)
        
        elif value > self.value and self.right != None:
            return self.right.contains(value)
        
        return False

    def find_complement(self, target):
        complement_count = 0  # Contador de pares cujo complemento soma para o valor alvo
        stack = []  # Pilha para armazenar os nós visitados da árvore
        current = self  # Começa pelo nó raiz da árvore

        while True:
            if current != None:
                stack.append(current)
                current = current.left

            # Se o nó atual é nulo e a pilha não está vazia
            # Nesse elif todos os nós da esquerda foram visitados e agora é necessário verificar os nós da direita
            elif stack:
                current = stack.pop()  # Remove o nó que está no topo e o atribui a current
                complement = target - current.value
                # Se o complemento é diferente do valor atual e o complemento está na árvore
                # Precisa da verificação se o complement é diferente pois se for igual não atende aos requisitos prospostos que são pares diferentes que somados resultam no valor alvo, não podem ser pares iguais
                if complement != current.value and self.contains(complement):
                    complement_count += 1
                current = current.right
            else:
                break

        return complement_count


if __name__ == '__main__':
    BT = BinaryTree(5)
    BT.put(3)
    BT.put(3)
    BT.put(7)
    BT.put(2)
    BT.put(4)
    BT.put(6)
    BT.put(8)
    BT.print()
