"""
1 - Realizza una classe Registro.

La classe deve memorizzare i voti degli studenti utilizzando una lista.

Implementa i seguenti metodi:

- aggiungi_voto(voto): aggiunge un voto alla lista;
- calcola_media(): restituisce la media dei voti;
- conta_sufficienti(): restituisce il numero di voti maggiori o uguali a 18;
- mostra_esito(): restituisce "Classe promossa" se almeno metà dei voti è sufficiente, altrimenti "Classe da recuperare".

Crea un oggetto Registro, inserisci alcuni voti e stampa i risultati.
"""

"""
class NomeClasse:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def func():
        pass
"""

print("=== REGISTRO ===\n")

class Registro:

    def __init__(self):
        self.voti = []

    def aggiungi_voto(self, voto):

        self.voti.append(voto)

    def calcola_media(self):
        s = 0
        for i in self.voti:
            s += i

        media = s / len(self.voti)
        return media

    def conta_sufficienti(self):

        c = 0
        for i in self.voti:
            if i >= 18:
                c+=1

        return c

    def mostra_esito(self):

        suff = self.conta_sufficienti()
        tot = len(self.voti)
        if suff >= tot/2:
            return "Classe promossa!"
        return "Classe da recuperare :("

#funzione inserimento voti
def inserisci_voto():
    while True:
        v = input("Inserisci un voto (0-30): ")
        try:
            v = int(v)
        except ValueError:
            print("Devi inserire un numero intero!")
            continue
        if  v > 30 or v < 0:
            print("Il voto deve essere compreso tra 0 e 30!")
            continue
        return v

### MAIN

r = Registro() #creazione istanza

n = int(input("Quanti voti vuoi inserire? "))
for i in range(n):
    r.aggiungi_voto(inserisci_voto()) #riempimento lista grazie al metodo e alla funzione

print(f"Lista voti: {r.voti}") #stampe dei metodi
print(f"Media voti: {r.calcola_media():.2f}")
print(f"Voti sufficienti: {r.conta_sufficienti()}\n")
print(f"Esito: {r.mostra_esito()}")