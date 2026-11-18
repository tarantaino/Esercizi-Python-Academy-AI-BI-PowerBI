"""1 - Partendo dai seguenti dati:

vendite = [
    ("Mouse", 5),
    ("Tastiera", 3),
    ("Monitor", 2),
    ("Mouse", 4),
    ("Monitor", 1)
]


Dove (nome_prodotto, quantità_venduta),
costruisci un dizionario con il totale venduto per prodotto,
stampa il dizionario finale e individua i prodotti con più di 3 unità vendute."""

vendite = [
    ("Mouse", 5),
    ("Tastiera", 3),
    ("Monitor", 2),
    ("Mouse", 4),
    ("Monitor", 1)
]

diz_vendite = {} #inizializzazione diz vuoto
#dal momento che le chiavi sono uniche, dobbiamo realizzare il totale per "Monitor" e "Mouse"

for prod, qta in vendite:
    diz_vendite[prod] = diz_vendite.get(prod, 0)+qta #usiamo un for con prod per salvare le chiavi e qta per salvare i valori, da sommare
    #accediamo al valore dell'item con il metodo get() ed effettuiamo al somma delle qta

print(f"Dizionario prodotti e vendite:\n {diz_vendite}") #la stampa ritorna il nome dei prodotti e il totale delle quantità vendute
print("\n") #newline per separare i risultati
for k,v in diz_vendite.items():  #per ogni key, value negli item di vendite, se value è maggiore di 3 stampa e ritorna il prodotto con le vendite maggiori di 3
    if v > 3:
        print(f"Prodotto con vendite superiore a 3: {k,v}")