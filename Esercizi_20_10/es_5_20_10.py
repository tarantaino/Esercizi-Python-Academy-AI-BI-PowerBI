"""5 - Stai sviluppando una funzione per gestire un ordine online.

Il cliente può acquistare un numero variabile di prodotti (prezzi)
Può anche specificare opzioni aggiuntive (sconto, spedizione, nome cliente, ecc.)

Scrivere una funzione che:

- somma tutti i prezzi dei prodotti
- applica uno sconto (se presente)
- aggiunge il costo di spedizione (se presente)
- restituisce il totale finale"""

def subtotale(*prezzi):
    return sum(prezzi) #calcolo del subtotale

def applica_sconto(importo, percentuale = 0):
        if percentuale !=0:
            importo = importo - importo * percentuale/100
        return round(importo, 2) #calcolo dello sconto se esiste

def ordine_prodotti(
        cliente,
        *prezzi,
        sconto = 0,
        spedizione= 0
    ):

    print("=== TOTALE PRODOTTI ACQUISTATI ===")
    tot = subtotale(*prezzi)
    if sconto != 0:
        tot = applica_sconto(tot, sconto)  #se esiste lo sconto passiamo applica_sconto che lo calcola

    if spedizione != 0:
        tot += spedizione #se la spedizione è diversa da zero fa una semplice somma

    return tot #ritorna il totale


ordine_mario = ordine_prodotti(
    "Mario",
    49.00,
    15.50,
    12.00,
    sconto = 10,
    spedizione = 5 #dichiarazione dei parametri da passare alla funzione ordine_prodotti
)

print(f"Totale finale: {ordine_mario:.2f} euro") #stampa
