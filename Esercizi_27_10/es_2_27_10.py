"""
2 - Crea una classe Utente con:

- nome;
- un set chiamato accessi.

Implementa il metodo:

- registra_accesso(data).

Crea due sottoclassi: Corsista e Docente

Per Corsista aggiungi il metodo report_accessi() che restituisce il numero totale di accessi effettuati.

Per Docente aggiungi il metodo report_accessi() che restituisce "Docente molto attivo" se gli accessi sono almeno 5,
altrimenti "Docente poco attivo".

"""
from datetime import datetime #utile per l'input della data

class Utente:

    def __init__(self, nome):
        self.nome = nome
        self.accessi = set()

    def registra_accesso(self, data):
        self.accessi.add(data)

class Corsista(Utente):

    def report_accessi(self):
        return len(self.accessi)

class Docente(Utente):

    def report_accessi(self):
        if len(self.accessi) >= 5:
            return "Docente molto attivo"
        return "Docente poco attivo"


c = Corsista("Marco")
c.registra_accesso("2026-10-01")
c.registra_accesso("2026-10-11")
c.registra_accesso("2026-10-12")
print(f"Numero totale accessi di {c.nome}: {c.report_accessi()}\n")

d = Docente("Laura")
for g in range(1, 5):
    d.registra_accesso(f"2026-10-0{g}")
print(f"Report del docente {d.nome}: {d.report_accessi()}") #docente poco attivo

d.registra_accesso("2026-10-05")
print(f"Report del docente {d.nome}: {d.report_accessi()}") #docente molto attivo