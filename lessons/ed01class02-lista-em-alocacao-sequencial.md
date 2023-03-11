# ESTRUTURA DE DADOS #2

## 1. Lista em alocação sequencial

### BUSCA LINEAR EM LISTAS (ALOCAÇÃO SEQUENCIAL)

### Implementando um algoritmo de busca

### Caso 1

Se não soubermos nada da lista que queremos buscar os elementos,
o melhor é olharmos para cada elemento da lista e verificar se
ele é igual ou não ao elemento que estamos procurando.

Iremos analisar a lista **sequencialmente**, para evitar de olhar
para o mesmo elemento mais de uma vez, ou seja, vamos olhar para
o primeiro elemento da lista, no índice zero e avançar de uma em
uma posição da lista, até encontrar o elemento desejado.

#### Code

Nossa função `busca()` receberá dois argumentos:

* a lista (`lista`) e
* o elemento (`elem`) que estamos procurando

```py
def busca(lista, elem):
```

Iremos percorrer essa lista, sequencialmente, uma vez que não sabemos a posição do elemento que estamos buscando, utilizando a função `range()` que interage com a lista pelo índice. Essa função irá variar de zero até o tamanho da lista -1.

```py
def busca(lista, elem):
    for i in range(len(lista)):
```

Nós iremos verificar se o índice da lista na posição `i`, é igual ao `elem` que estamos procurando.

```py
def busca(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
```

Se o elemento na posição `i` for igual ao `elem`, nós poderemos
retornar a posição de `i`.

```py
def busca(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
```

Caso contrário a iteração seguirá para o próximo índice do `range()`.

Vamos optar por usar `None` no retorno, caso o `elem` buscado
na lista não exista e iremos deixar documentado essa decisão,
utilizando o DOCSTRING.

```py
def busca(lista, elem):
    """Retorna o índice do elem se ele estiver na lista ou None, caso contrário"""
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None
```

Para testarmos a nossa função, vamos utilizar uma `lista_estranha` que contém 6 elementos, sendo eles:

* quatro números inteiros
* e duas strings

Iremos buscar pelo elemento `32` dentro dessa lista.

```py
lista_estranha = [8, "5", 32, 0, "python", 11]
elemento = 32
```

Vamos atribuir o retorno da função de `busca()` na variável
chamada `indice`.

Iremos chamar a nossa função, passando como argumento a

* `lista_estranha`
* e o `elemento` buscado.

```py
indice = busca(lista_estranha, elemento)
```

E iremos verificar se o valor do nosso `indice` não é `None`.

```py
if indice is not None:
```

Se não for, significa que encontramos este elemento na lista e
poderemos mostrar o resultado na tela do usuário.

```py
if indice is not None:
    print("O índice do elemento {} é {}".format(elemento, indice))
```

Caso contrário, se o for `None`, significa que não encontramos
o elemento na lista.

```py
if indice is not None:
    print("O índice do elemento {} é {}".format(elemento, indice))
else:
    print("O elemento {} não se encontra na lista.".format(elemento))
```

### Complexidade do algoritmo

* O[N]
  * **`N`** = tamanho da lista
  * mais 2 **operações elementares**
    * `for i in range(len(lista)):` - atribuição de valor ao `i`
    * `if lista[i] == elem:` - comparação entre dois valores
  * Mais uma operação elementar
    * `return i`
  * Sendo, **`2*N + 1`**
    * a constante `1` podemos eliminar, pois queremos analisar
    * apenas o **termo dominante**
      * obtemos, **`2*N`**
    * a constante multiplicativa do **termo dominante**, também
    não importa na notação do **BIG[O]**
      * permanecendo apenas, **`N`**, onde chegamos na notação
      apresentada.

#### Conclusão

A complexidade do algoritmo de busca é **LINEAR** com o tamanho
da entrada, cujo o gráfico é uma reta.
