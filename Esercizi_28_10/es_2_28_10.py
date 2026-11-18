"""
2) Crea una classe Prodotto che rappresenta un articolo in vendita in un negozio.

Attributi:

.nome: nome del prodotto (accessibile e modificabile),
.prezzo: il prezzo unitario del prodotto (deve essere incapsulato),
.quantita: la quantità disponibile in magazzino (anch’essa incapsulata).


- Crea un metodo aggiorna_prezzo(nuovo_prezzo) che modifica il prezzo solo se il nuovo prezzo è maggiore di zero.
- Crea un metodo vendi(pezzi) che scala la quantità se ce ne sono abbastanza a magazzino, altrimenti stampa un messaggio di errore.
- Crea un metodo rifornisci(pezzi) che aggiunge pezzi in magazzino (solo se il numero è positivo).
"""

class Prodotto:

    def __init__(self, nome, prezzo, qta):
        self.nome = nome
        self._prezzo = prezzo
        self._qta = qta

    @property
    def prezzo(self):
        return self._prezzo

    @property
    def qta(self):
        return self._qta

    def aggiorna_prezzo(self, nuovo_prezzo):

        if nuovo_prezzo > 0:
            self._prezzo = nuovo_prezzo
            print(f"Prezzo aggiornato: {nuovo_prezzo}")
        else:
            print("Errore: il prezzo deve essere maggiore di 0!")

    def vendi(self, pezzi):

        if 0 < pezzi <= self._qta:
            self._qta -= pezzi
            print(f"Vendita effettuata. {self._qta} pezzi rimasti in magazzino.")
        else:
            print("Errore: quantità non disponibile in magazzino!")

    def rifornisci(self, pezzi):

        if pezzi > 0:
            self._qta += pezzi
            print(f"Rifornimento effettuato. Nuova quantità: {self._qta}")
        else:
            print("Errore: i pezzi da aggiungere devono essere maggiori di zero!")


print("=== PRODOTTI ===")

n = input("Inserisci nome prodotto: ").strip()

while True:
    try:
        prezzo = float(input("Inserisci il prezzo: "))
        if prezzo > 0:
            break
        print("Il prezzo deve essere maggiore di zero!")
    except ValueError:
        print("Errore: inserisci un valore numerico valido!")

while True:
    try:
        qta = int(input("Inserisci la qta iniziale in magazzino: "))
        if qta >=0:
            break
        print("La qta non può essere negativa!")
    except ValueError:
        print("Errore: inserisci un numero intero valido")

p = Prodotto(n, prezzo, qta)
print(f"\n Prodotto '{p.nome}' creato!")

while True:
    print("\n==============================")
    print(f"GESTIONE MAGAZZINO: {p.nome.upper()}")
    print("==============================")
    print("1. Vendi pezzi")
    print("2. Rifornisci magazzino")
    print("3. Aggiorna prezzo")
    print("4. Visualizza informazioni prodotto")
    print("0. Esci")

    scelta = input("\nScegli un'opzione (0-4): ").strip()

    if scelta == '1':
        try:
            pezzi = int(input("Quanti pezzi vuoi vendere? "))
            p.vendi(pezzi)
        except ValueError:
            print("Errore: inserisci un numero intero valido.")

    elif scelta == '2':
        try:
            pezzi = int(input("Quanti pezzi vuoi aggiungere? "))
            p.rifornisci(pezzi)
        except ValueError:
            print("Errore: inserisci un numero intero valido.")

    elif scelta == '3':
        try:
            nuovo_prezzo = float(input("Inserisci il nuovo prezzo (€): "))
            p.aggiorna_prezzo(nuovo_prezzo)
        except ValueError:
            print("Errore: inserisci un valore numerico valido.")

    elif scelta == '4':
        print("\n--- STATO ATTUALE ---")
        print(f"Nome: {p.nome}")
        print(f"Prezzo: {p.prezzo}€")
        print(f"Quantità: {p.qta}")

    elif scelta == '0':
        print("\nChiusura del programma. Arrivederci!")
        break
    else:
        print("Opzione non valida. Scegli un numero compreso tra 0 e 4.")

"""p = Prodotto("Penna", 1.5, 3)

p.vendi(2)
print(p.qta)
p.vendi(5)
p.rifornisci(10)
print(p.qta)
p.aggiorna_prezzo(-4)
print(p.prezzo)
p.aggiorna_prezzo(2)
print(p.prezzo)"""