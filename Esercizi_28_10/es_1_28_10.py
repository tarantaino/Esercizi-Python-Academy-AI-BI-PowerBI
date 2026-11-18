"""
1) Crea una classe PrenotazioneVolo per gestire le prenotazioni di passeggeri.

Attributi incapsulati:

_nome_passaggero

_numero_volo

In più si avrà l'attributo posti_disponibili (condiviso tra tutte le prenotazioni).

Aggiungi un controllo nel setter di numero_volo: il numero deve essere una stringa di 2 lettere seguite da 3 cifre (es. "AZ123").

Implementa un metodo effettua_prenotazione() che:

- Riduce il numero di posti disponibili solo se maggiore di zero.

- In caso contrario, stampa "Nessun posto disponibile".
"""

class PrenotazioneVolo:

    posti_disponibili = 5

    def __init__(self, nome_passeggero, numero_volo):

        self._nome_passeggero = nome_passeggero
        self.numero_volo = numero_volo

    @property
    def numero_volo(self):
        return self._numero_volo

    @numero_volo.setter
    def numero_volo(self, volo):
        if ((isinstance(volo, str)) and
                volo[:2].isalpha() and
                volo[:2].isupper() and
                volo[2:].isdigit() and
                len(volo) ==5):
            self._numero_volo = volo
        else:
            raise ValueError("Numero volo non valido!")


    def effettua_prenotazione(self):

        if PrenotazioneVolo.posti_disponibili > 0:
            PrenotazioneVolo.posti_disponibili -= 1
        else:
            print("Nessun posto disponibile!")


def prenota():
    while True:
        n = input("Nome passeggero: ").strip()
        v = input("Numero volo (es. AZ123): ").strip().upper()
        try:
            return PrenotazioneVolo(n, v)
        except ValueError as e:
            print(f"Dati non validi - {e}")

while True:
    if PrenotazioneVolo.posti_disponibili == 0:
        print("Nessun posto disponibile!")
        break

    r = input("Vuoi inserire un'altra prenotazione? (s/n): ").strip().lower()
    if r != "s":
        break

    p = prenota()
    p.effettua_prenotazione()
    print(f"Posti rimasti: {PrenotazioneVolo.posti_disponibili}")

#TEST SENZA INPUT
"""p1 = PrenotazioneVolo("René", "BB123")
p2 = PrenotazioneVolo("Duccio", "CC123")
p3 = PrenotazioneVolo("Stanis", "DD123")
p4 = PrenotazioneVolo("Alessandro", "AA123")
p5 = PrenotazioneVolo("Arianna", "FF123")

try: #esempio di prenotazione con numero volo errato
    p6 = PrenotazioneVolo("Itala", "a")
except ValueError as e:
    print("Prenotazione rifiutata:", e)

for p in (p1, p2, p3, p4, p5):
    p.effettua_prenotazione()
    print(f"Posti rimasti: ", PrenotazioneVolo.posti_disponibili)

p1.effettua_prenotazione() #esempio extra per verificare che i posti non sono disponibili"""