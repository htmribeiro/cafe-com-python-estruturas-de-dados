# ESTRUTURA DE DADOS #3

## 1. Lista em alocação sequencial

### INSERÇÃO E REMOÇÃO EM LISTAS

### Complexidade de Inserir e Remover na Lista

### Objetivo

Entender como ocorrem dentro de uma lista de alocação sequencial, as operações de:

1. INSERÇÃO
2. REMOÇÃO

## Inserção de novos elementos

### Caso 1

Acontece quando queremos inserir um elemento ao final da lista.

E como a nossa lista se encontra em alocação sequencial, ou seja, cada
elemento se encontra um ao lado do outro na memória, basta nós colocarmos um
novo elemento no endereço de memória que vem logo após o endereço do último
elemento da lista.

Como nós conseguimos realizar acesso aleatório em uma lista de alocação sequencial, ou seja, nós conseguimos acessar uma posição da memória diretamente a partir de um índice, a quantidade de operações que nós precisamos realizar para inserir um elemento no final da lista, independe do tamanho da lista, ela é sempre constante. Basta identificarmos qual que é aquela posição e irmos diretamente lá, por um índice e colocar aquele elemento.

#### Complexidade do algoritmo (Caso 1)

A complexidade de inserir um novo elemento na lista ao final da lista, é **O[1]**.
Porque ela depende apenas de um número constante de operações.

### Caso 2

Neste caso, nós queremos inserir um novo elemento em qualquer posição da lista, o que eleva um pouco mais a sua complexidade.

Para isso, nós precisaremos empurrar todos os elementos que vêm logo após a posição desejada, para trás.

Por exemplo, temos uma sequência de valores em nossa lista, vamos supor que a gente queira colocar um novo elemento, o número 1, na posição de índice 2, ou seja, onde se encontra atualmente o número 8.

* Posição atual: | 12 | 5 | 8 | 30 | 7 | 9 |

Para realizarmos esta operação, nós podemos deixar o 12 e o 5 na posição atual, porém do número 8 (posição 2) em diante, todos terão que ser empurrados em uma posição.

* Nova posição: | 12 | 5 | **1** | 8 | 30 | 7 | 9 |

#### Complexidade do algoritmo (Caso 2)

Por conta do número de operações, que nós realizamos, a cada inserção no meio da lista é **variável** e depende do tamanho da lista e ele depende também da posição em que nós queremos inserir.

Colocar na penúltima posição, por exemplo, exige que a gente empurre apenas o último elemento para frente. Já se colocarmos na primeira posição, vamos ter que empurrar todos os elementos para frente.

Então nós vimos que quando temos um algoritmo que a quantidade de operações varia dependendo de algum parâmetro que você passa para a operação, e neste caso a posição em que será inserido, nós analisamos a complexidade do pior caso, ou seja, aquele que nós vamos realizar o maior número possível de operações. E o pior caso ocorre quando queremos inserir na primeira posição da lista.

Se começarmos movendo os elementos de trás pra frente, nós conseguiremos realizar essa operação com uma única passagem pela lista. E aí para cada elemento nós realizamos um número constante de operações.

Neste caso, a complexidade da operação seria de **O[n]**, onde *n* é o tamanho dessa lista.

### Desvantagens da organização sequencial de memória

Nós não conseguimos mexer com a posição de memória que vem antes do primeiro elemento, e nem sempre conseguimos mexer com a posição de memória que que se encontra após o último elemento.

Ou seja, no momento em que a gente cria uma lista, nós precisamos reservar um espaço de memória que vai conter todos os seus elementos e aí o espaço que vem antes desse espaço reservado e o que vem logo após o espaço reservado, esses endereços são livres e podem ser usados para armazenar quaisquer outros dados que não pertencem a nossa lista.

Mas, e se quisermos inserir um novo elemento, como fica?

### Solicitando mais memória para o computador

Vamos alocar um espaço de memória, maior do que tínhamos.

Serão copiados cada um dos valores que tínhamos no espaço anterior, para esse novo espaço. E agora com espaço disponível para a nossa lista, conseguiremos inserir um novo elemento em nossa lista. Já o espaço de memória antigo poderá ser descartado.

> **Obs.: no python não fazemos gerenciamento direto de memória, as próprias listas prontas já fazem esse gerenciamento pra gente.**

## Remoção de novos elementos

### Caso 3

Para operação de remoção, os casos são similares. Se nós quisermos remover um elemento do final da lista, basta um número **constante** de operações para ignorarmos a última posição, e aí a remoção acontece com complexidade de **O[1]**.

Porém, se a agente quiser remover um elemento do meio da lista, nós precisaríamos mover todos os elementos, após a posição desejada, uma posição a frente, pois não podemos ter buracos no meio da lista.

Daí o pior caso acontece, quando desejamos remover o primeiro elemento. Pois, teríamos que trazer todos os demais elementos, uma posição a frente.

#### Complexidade do algoritmo (Caso 3)

E para este caso, essa operação de remoção, ocorre com complexidade **O[n]**, em que *n* é o tamanho da lista.

### Mais uma desvantagens da organização sequencial de memória

A quantidade de memória que uma lista consome, é aquela que lhe foi reservada no momento da sua **CRIAÇÃO**, então, independente da lista estar vazia ou de ter dois ou três elementos e seu espaço foi reservado para caber oito ou dez elementos, por exemplo, é essa a quantidade de espaço que a lista está consumindo, porque essas posições não poderão ser ocupadas por qualquer outro tipo de dado.

Logo, se a nossa lista está diminuindo, é importante fazermos uma nova alocação para um espaço menor e descartar o espaço anterior, e assim conseguirmos ser mais eficientes no uso de memória.
