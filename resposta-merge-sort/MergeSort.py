import random

def merge(ord_l1, ord_l2):
    i = 0
    j = 0
    result_list = []
    while i < len(ord_l1) and j < len(ord_l2):
        if ord_l1[i] <= ord_l2[j]:
            result_list.append(ord_l1[i])
            i = i + 1
        else:
            result_list.append(ord_l2[j])
            j = j + 1
    # Caso sobre elementos em alguma das listas eles são apenas copiados para a lista 3 pois já estão ordenados:
    while i < len(ord_l1):
        result_list.append(ord_l1[i])
        i = i + 1
    while j < len(ord_l2):
        result_list.append(ord_l2[j])
        j = j + 1
    return result_list


def merge_sort(l):
    if len(l) == 1:
        return l
    half = int(len(l)/2)    # Divide uma lista em duas metades
    l1 = l[0:half]
    l2 = l[half:]
    # Organiza as metades recursivamente
    l1 = merge_sort(l1)
    l2 = merge_sort(l2)
    return merge(l1, l2)


# Gera a lista
size = int(input("Informe o tamanho da lista: "))
print("\nTamanho da lista informado: ", size)
random.seed(size)
l = set()  # Usando set para garantir elementos únicos
while len(l) < size:
    num = random.randint(0, 2**17)
    l.add(num)

l = list(l)  # Convertendo de volta para lista para ordenação e manipulação

# Gera o alvo
target = random.randint(0, 2**17)
while target % 2 == 0:
    target = random.randint(0, 2**17)

# Ordena a lista
l = merge_sort(l)

# Conta pares cujo complemento soma para o alvo
pair_counter = 0
left = 0    # Ponteiro que aponta para o início da lista
right = len(l) - 1  # Ponteiro que aponta para o final da lista

# Loop que ocorre enquanto os ponteiros não se cruzarem
while left < right:
    sum_elements = l[left] + l[right]
    if sum_elements == target:
        pair_counter += 1
        # print(f"Par encontrado: ({l[esquerda]}, {l[direita]})")
        left += 1
        right -= 1
    elif sum_elements < target:
        left += 1
    else:
        right -= 1

print(f"Número de pares cujo complemento soma para {target}: {pair_counter}")
