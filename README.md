# Trabalho 01 - Soma Perfeita

- [Trabalho 01 - Soma Perfeita](#trabalho-01---soma-perfeita)
  - [Importante:](#importante)
  - [Enunciado do Problema:](#enunciado-do-problema)
  - [Resolução](#resolução)
    - [Rodando os Scripts](#rodando-os-scripts)

## Importante:
- Não olhe códigos de outros ou da internet. Exceto os que são fornecidos. Também
não mostre ou publique o seu.
- Em caso de plágio, fraude ou tentativa de burlar os sistemas será aplicado nota 0 na
disciplina aos envolvidos.
- Alguns alunos podem ser solicitados para explicar com detalhes a implementação.
- Passar em todos os testes não é garantia de tirar a nota máxima. Sua nota ainda
depende do cumprimento das especificações do trabalho, qualidade do código,
clareza dos comentários, boas práticas de programação e entendimento da matéria
demonstrada em possível reunião.


## Enunciado do Problema: 

Considere o seguinte problema, seja 𝑆 ⊂ ℕ , e 𝑘 ∈ ℕ, encontrar quantos pares
{ 𝑖, 𝑗 } : 𝑖,   𝑗 ∈ 𝑆, 𝑖 ≠ 𝑗    e 𝑖 + 𝑗 = 𝑘, existem em 𝑆.

Um programador implementou o seguinte código para sortear 𝑆 e resolver o problema:

```python
import random

tamanho = int(input())
random.seed(tamanho)
l = []

while len(l) < tamanho:
    num = random.randint(0, 2**17)
    if num not in l:
        l.append(num)

alvo = random.randint(0, 2**17)

while alvo % 2 == 0:
    alvo = random.randint(0, 2**17)

contador = 0

for i in l:
    compl = alvo - i
    if compl in l:
        contador = contador + 1
print(int(contador/2))
```

Entretanto o código feito é bastante ineficiente, nesse trabalho você deverá entender o
porque esse código é ineficiente e desenvolver 3 alternativas (ainda em Python) para
melhorá-lo, chegando ao mesmo resultado. Sujeito às seguintes restrições:

1. Uma das alternativas obrigatoriamente deve usar **Tabela Hash** implementada por
você.
2. Você não deve usar bibliotecas muito elaboradas (ex: NumPy, itertools, etc). Em
caso de dúvida se algo pode ser utilizado consulte o professor.
3. Suas alternativas devem seguir ideias diferentes (e não apenas implementações
diferentes da mesma ideia.)


## Resolução 
### Rodando os Scripts

Para que consiga rodar cada script primeiro selecione a pasta em que se encontra o script:

```bash
cd resposta-hash-table
```

Para rodar o script com a possibilidade de colocar o input do tamanho da lista, entre com:
```bash
python HashTable.py
```

Para rodar o script com um número do tamanho da lista pré-setado digite (lembre-se de alterar o arquivo `tamanho-lista.txt`):

```bash
time python MergeSort.py < ../tamanho-lista.txt
```

