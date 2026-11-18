"""Si vuole gestire la classifica dei punteggi ottenuti da alcuni giocatori in un videogioco.
Creare una lista di dizionari, dove ogni dizionario contiene il nome del giocatore e il punteggio ottenuto.
Utilizzare la funzione sorted() e una funzione lambda per ordinare i giocatori dal punteggio più alto al più basso.
Infine, stampare la classifica numerando ogni posizione"""

classifica = [
    {"Doran": 1500},
    {"PaoloCannone22": 1900},
    {"Terenas": 1300},
    {"Faker": 3000},
    {"Brizz": 2700 }
]

class_ord = sorted(classifica, key=lambda p: list(p.values())[0], reverse = True)#reverse = True perché sorted ordina in maniera crescente
                            #(p.values())[0] restituisce i valori del dizionario, list() per convertirli in lista

for i in enumerate(class_ord, start = 1):
    print(i) #stampa classifica con posizione numerata