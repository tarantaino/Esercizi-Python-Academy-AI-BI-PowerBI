"""
3) Scrivi un programma che gestisca un piccolo magazzino. L'utente può:

- Aggiungere un prodotto indicando nome, quantità e prezzo unitario.
- Visualizzare l'inventario completo.
- Calcolare il valore totale del magazzino.
- Cercare un prodotto per nome.

Il programma deve gestire:
- Inserimenti non numerici.
- Ricerca di prodotti inesistenti.
- Tentativi di inserire quantità o prezzi negativi.

"""

def aggiungi_prod(magazzino):

    while True:
        try:
            pr = input("Inserisci nome prodotto: ").strip()
            if pr.isdigit(): #se è un numero - raise ValueError
                raise ValueError
            q = int(input("Inserisci qta: "))
            if q < 0:  #se è minore di 0
                raise ValueError
            pz = float(input("Inserisci prezzo: "))
            if pz <= 0: #se è minore o uguale - raise ValueError
                raise ValueError
        except ValueError:
            print("ERRORE - Dati inconsistenti!")
            continue

        magazzino.append({ #append dei dati nella lista di dizionari
            "prodotto": pr,
            "qta": q,
            "prezzo": pz,
        })

        r = input("Vuoi inserire un altro prodotto? (s/n) ").strip().lower()
        if r != "s":
            break #se è necessario inserire altro


def visualizza(magazzino):
    #semplice stampa
    print("=== STOCK ===")
    for prodotti in magazzino:
                print(prodotti)
    else: #se magazzino vuoto
           print("Magazzino vuoto!")

def totale(magazzino):
    #totale = qta * prezzo
    tot = 0
    for p in magazzino:
        tot += p["qta"] * p["prezzo"]
    print(f"Valore totale del magazzino: {tot:.2f}€")

def cerca_prod(magazzino):

    n = input("Nome del prodotto da cercare: ").strip().lower()
    for p in magazzino:
        if p["prodotto"].lower() == n:
            print(p)
            return
    print(f"Prodotto '{n}' non trovato!")

magazzino = []
#lista vuota che viene riempita avviando la funzione

while True: #match case per avviare le funzioni
    print("\n=== MAGAZZINO ===")
    print("1 - Aggiungi prodotto")
    print("2 - Visualizza inventario")
    print("3 - Valore totale")
    print("4 - Cerca prodotto")
    print("0 - Esci\n")

    try:
        r = int(input("Quale operazione desideri eseguire? "))
    except ValueError:
        print("Devi inserire un numero!")
        continue

    match r:
        case 1:
            aggiungi_prod(magazzino)
        case 2:
            visualizza(magazzino)
        case 3:
            totale(magazzino)
        case 4:
            cerca_prod(magazzino)
        case 0:
            print("Arrivederci!")
            break
        case _:
            print("Operazione non valida!")