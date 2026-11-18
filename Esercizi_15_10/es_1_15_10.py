""" - Un sistema registra gli ID dei dipendenti che hanno effettuato l'accesso
a un'applicazione durante la giornata.

accessi = [
    "A102",
    "B205",
    "A102",
    "C310",
    "B205",
    "D411",
    "E150",
    "D411",
    "D411"
]

Costruisci una struttura contenente tutti gli ID unici,
conta quanti accessi duplicati sono presenti nella lista,
stampa ogni ID che compare per la prima volta,
stampa ogni ID che viene trovato nuovamente (duplicato),
stampa il numero totale di dipendenti distinti che hanno effettuato l'accesso.

N.B. se serve, avvalersi del metodo di creazione del set tramite funzione. Es: s = set()

"""

accessi = [
    "A102",
    "B205",
    "A102",
    "C310",
    "B205",
    "D411",
    "E150",
    "D411",
    "D411"
]

set_accessi = set()
#print(set_accessi)

duplicato = 0
for i in accessi:
    if i not in set_accessi:
        set_accessi.add(i)
        print(f"Primo accesso: {i}")
    else:
        duplicato += 1
        print(f"Accesso duplicato rilevato da parte di: {i}\n") #stampa l'id che viene trovato nuovamente

print("\n")
print(f"Numero accessi duplicati: {duplicato}") #stampa numero accessi duplicati
print(f"Utenti distinti: {set_accessi}") #stampa utenti distinti