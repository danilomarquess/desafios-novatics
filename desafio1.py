lista = [8, 5, 10, 5, 2, 4, 4, 3]
def manipular_lista():
    lista.sort()
    print(lista)
    listaUnica = list(set(lista))
    print(listaUnica)
    return
if __name__ == "__main__":
    manipular_lista()