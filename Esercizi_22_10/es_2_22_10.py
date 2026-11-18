"""
2 - Un'organizzazione di eSport vuole realizzare un programma Python per gestire un torneo di videogiochi.
Il programma deve consentire di registrare i partecipanti, analizzare le loro prestazioni,
assegnare bonus e individuare i giocatori che accederanno alla fase finale.

Ogni giocatore è caratterizzato da un nome, dal numero di vittorie, dal numero di sconfitte e dai punti esperienza accumulati.
Le informazioni devono essere organizzate in una struttura dati adatta a gestire più giocatori.

Il programma dovrà consentire di analizzare i risultati del torneo, produrre classifiche e generare un report riepilogativo.
Alcune operazioni dovranno inoltre essere monitorate per tenere traccia della loro esecuzione.

Realizzare un programma che soddisfi i seguenti requisiti:
1. Predisporre alcuni dati iniziali relativi ai giocatori, includendo sia giocatori con risultati positivi sia giocatori che non hanno ancora disputato partite.

2. Consentire di registrare nuovi giocatori, verificando che i dati inseriti siano validi e che non siano già presenti altri giocatori con lo stesso nome.

3. Per ogni giocatore, calcolare il numero totale di partite disputate e la percentuale di vittorie.
Il programma deve gestire correttamente il caso di un giocatore che non abbia ancora disputato partite.

4. Prevedere la possibilità di assegnare punti esperienza aggiuntivi a un giocatore, mantenendo la possibilità di conservare i dati precedenti.


"""

#partecipanti = nome, num_vittorie, num_sconfitte, exp_pts, bonus, num_partite_giocate(num_vittorie+num_sconfitte)

"""
3. Per ogni giocatore, calcolare il numero totale di partite disputate e la percentuale di vittorie.
Il programma deve gestire correttamente il caso di un giocatore che non abbia ancora disputato partite.
"""


def tot_partite_wr(nome_giocatore):
    totale = 0
    wr = 0
    #print("ciao")
    for partecipante in partecipanti:
        if partecipante["nome"] == nome_giocatore:
            print(partecipante)



partecipanti = [
    {"nome": "Marco",   "num_vittorie": 12, "num_sconfitte": 3,  "exp_pts": 1450},
    {"nome": "Giulia",  "num_vittorie": 9,  "num_sconfitte": 6,  "exp_pts": 1120},
    {"nome": "Luca",    "num_vittorie": 15, "num_sconfitte": 1,  "exp_pts": 1890},
    {"nome": "Sara",    "num_vittorie": 7,  "num_sconfitte": 8,  "exp_pts": 860},
    {"nome": "Davide",  "num_vittorie": 4,  "num_sconfitte": 11, "exp_pts": 530},
    {"nome": "Savato",  "num_vittorie": 0,  "num_sconfitte": 0, "exp_pts": 0},
]


nome = ""


while True:
    esiste = False

    nome = input("Inserisci Nome giocatore. Scrivi 'exit' per uscire: ").strip()
    if nome == "exit" or nome == "":
        break


    nuovo_partecipante = {}

    for n in partecipanti:
        if n["nome"] == nome:
            esiste = True
            break

    if esiste:
        print("Nome già registrato.")
        tot_partite_wr(nome)
    else:
        print(f"Nuovo partecipante: {nome}")

        nuovo_partecipante["nome"] = nome
        nuovo_partecipante["num_vittorie"] = 0
        nuovo_partecipante["num_sconfitte"] = 0
        nuovo_partecipante["exp_pts"] = 0
        partecipanti.append(nuovo_partecipante)

print(partecipanti)

