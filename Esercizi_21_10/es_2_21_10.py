"""
Data la lista [3, -1, 7, -5, 10],
usa filter() con una funzione lambda per ottenere solo i numeri positivi e poi calcolane la media con una funzione
"""
def media_numeri(lista):
    s = 0
    c = 0
    for i in lista:
        s += i
        c += 1

    m = s/c
    return f"La media della lista di numeri è: {round(m, 2)}" #funzione che calcola la media
    #restituisce direttamente la stringa con il valore, ergo è necessario un print della funzione con la lista come arg

n = [3, -1, 7, -5, 10]

p_n = list(filter(lambda x: x>=0, n)) #crea lista con lambda che filtra i numeri maggiori zero per escludere i negativi
print(p_n)#stampa di debug

print(media_numeri(p_n)) #invoke funzione