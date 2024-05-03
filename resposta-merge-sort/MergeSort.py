import random


def merge(ord_l1, ord_l2):
    i = 0
    j = 0
    lista_resultado = []
    while i < len(ord_l1) and j < len(ord_l2):
        if ord_l1[i] <= ord_l2[j]:
            lista_resultado.append(ord_l1[i])
            i = i + 1
        else:
            lista_resultado.append(ord_l2[j])
            j = j + 1
    # Caso sobre elementos em alguma das listas eles são apenas copiados para a lista 3 pois já estão ordenados:
    while i < len(ord_l1):
        lista_resultado.append(ord_l1[i])
        i = i + 1
    while j < len(ord_l2):
        lista_resultado.append(ord_l2[j])
        j = j + 1
    return lista_resultado


def merge_sort(l):
    if len(l) == 1:
        return l
    meio = int(len(l)/2)    # Divide uma lista em duas metades
    l1 = l[0:meio]
    l2 = l[meio:]
    # Organiza as metades recursivamente
    l1 = merge_sort(l1)
    l2 = merge_sort(l2)
    return merge(l1, l2)


# Gera a lista (TA LENTO - IMPLEMENTA USANDO SET EH MAIS RAPIDOS)
tamanho = int(input("Informe o tamanho da lista: "))
random.seed(tamanho)
l = []
while len(l) < tamanho:
    num = random.randint(0, 2**17)
    if num not in l:
        l.append(num)

# Gera o alvo
alvo = random.randint(0, 2**17)
while alvo % 2 == 0:
    alvo = random.randint(0, 2**17)

# Ordena a lista
l = merge_sort(l)

# Conta pares cujo complemento soma para o alvo
contador_pares = 0
left = 0    # Ponteiro que aponta para o início da lista
right = len(l) - 1  # Ponteiro que aponta para o final da lista

# Loop que ocorre enquanto os ponteiros não se cruzarem
while left < right:
    soma_elementos = l[left] + l[right]
    if soma_elementos == alvo:
        contador_pares += 1
        # print(f"Par encontrado: ({l[left]}, {l[right]})")
        left += 1
        right -= 1
    elif soma_elementos < alvo:
        left += 1
    else:
        right -= 1

print(f"Número de pares cujo complemento soma para {alvo}: {contador_pares}")
