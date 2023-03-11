def busca(lista, elem):
    """Retorna o índice do elem se ele estiver na lista ou None, caso contrário"""
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None


if __name__ == "__main__":

    lista_estranha = [8, "5", 32, 0, "python", 11]
    elemento = 32

    indice = busca(lista_estranha, elemento)

    if indice is not None:
        print("O índice do elemento {} é {}".format(elemento, indice))
    else:
        print("O elemento {} não se encontra na lista.".format(elemento))
