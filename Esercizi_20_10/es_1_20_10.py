"""
Hai una lista con duplicati e vuoi ottenere una lista pulita, mantenendo però l’ordine originale.
 Scrivere una funzione che, data una lista, restituisca una lista senza duplicati.
"""
def no_duplicati(lista):
    """
    Funzione che restituisce una lista senza duplicati
    :param lista: lista da passare in chiamata
    :return: None, è una stampa
    """
    nuova_lista = []
    for i in lista:
        if i not in nuova_lista:
            nuova_lista.append(i)

    print(nuova_lista)


ls = ["a", "a", "b", "b", "c", "c", "d", "d"] #lista d'esempio
no_duplicati(ls) #invoke della funzione passando ls -> restituisce ['a','b','c','d']