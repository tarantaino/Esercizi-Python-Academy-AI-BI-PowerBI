"""4 - Hai una frase inserita dall’utente.
Vuoi costruire un sistema che:

- separa le parole
- conta quante volte compaiono
- restituisce un dizionario"""

from collections import Counter #import di counter per contare le parole

def diz_cnt():
    """
    Nessun valore da passare perché è richiesto in input
    :return: Ritorna un dizionario
    """
    while True:
        f = input("Inserisci frase: ").strip()
        f_low = f.lower()
        f_split = f_low.split() #per separare
        print(f"Parole separate: {f_split}")
        print("\n")

        print(f"Conteggio parole:\n {Counter(f_split)}")
        print("\n") #conteggio parole

        diz = {}
        for i in f_split:
            diz[i] = diz.get(i, 0)+1 #per ogni parola all'interno di f_split associo il value che sarà uguale a 0+1 per ogni parola comparsa

        break

    return  diz


print(f"Dizionario frase inserita:\n {diz_cnt()}")