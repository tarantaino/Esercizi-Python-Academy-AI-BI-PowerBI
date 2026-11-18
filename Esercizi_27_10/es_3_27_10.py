"""
3 - Un'azienda deve selezionare i candidati per un colloquio.

Creare le classi:

ValutazioneTecnica
ValutazioneSoftSkills

La candidatura è rappresentata da un dizionario con le chiavi:

{
    "nome": ...,
    "test_tecnico": ...,
    "problem_solving": ...,
    "team_work": ...
}

Nella classe ValutazioneTecnica implementare il metodo "valuta_tecnica(candidato)" che:

- assegni 3 punti se il test tecnico è ≥ 80;
- assegni 2 punti se è compreso tra 60 e 79;
- assegni 0 punti altrimenti.


Nella classe ValutazioneSoftSkills implementare il metodo  "valuta_soft(candidato)"  che:

- assegni 2 punti se problem_solving è almeno 7;
- assegni 2 punti se team_work è almeno 7.

Nella classe  Selezionatore (che eredita da entrambe) effettuare l'override del metodo "valuta(candidato)"  che:

- richiami i due metodi delle classi genitrici;
- calcoli il punteggio totale;
- restituisca un dizionario con nome, punteggio ed esito ("Ammesso" o "Non ammesso").

Un candidato è ammesso con almeno 5 punti.
"""

class ValutazioneTecnica:

    def __init__(self):
        self.candidato = {}

    def valuta_tecnica(self, candidato):

        p = 0
        if candidato["test_tecnico"] >= 80:
            p += 3
        elif candidato["test_tecnico"] >= 60:
            p += 2
        else:
            p += 0

        return p

class ValutazioneSoftSkills:

    def __init__(self):
        self.candidato = {}

    def valuta_soft(self, candidato):

        p = 0
        if candidato["problem_solving"] >= 7:
            p += 2
        if candidato["team_work"] >= 7:
            p += 2

        return p

class Selezionatore(ValutazioneTecnica, ValutazioneSoftSkills):

    def valuta(self, candidato):
        punti_tec = self.valuta_tecnica(candidato)
        punti_soft = self.valuta_soft(candidato)

        totale = punti_tec + punti_soft

        if totale >= 5:
            return f"{candidato} Amesso!"
        return f"{candidato} Non ammesso!"


def inserisci_candidato():

    d = {}
    while True:

        n = input("Inserisci nome candidato: ").strip().capitalize()
        if n.isdigit():
            print("Devi inserire un nome!")
            continue

        tt = int(input("Inserisci punteggio test tecnico (0-100): "))
        if tt < 0 or tt > 100:
            print("Devi inserire un valore compreso tra 0 e 100!")
            continue

        ps = int(input("Inserisci punteggio problem solving (0-10): "))
        if ps < 0 or ps > 10:
            print("Devi inserire un valore compreso tra 0 e 10!")
            continue

        tm = int(input("Inserisci punteggio team work (0-10): "))
        if tm < 0 or tm > 10:
            print("Devi inserire un valore compreso tra 0 e 10!")
            continue

        d = {
            "nome": n,
            "test_tecnico" : tt,
            "problem_solving" : ps,
            "team_work": tm,
        }

        return d


s = Selezionatore()
print(s.valuta(inserisci_candidato()))
