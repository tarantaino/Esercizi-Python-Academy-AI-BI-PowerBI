partecipanti = [
    {"nome": "Marco",   "num_vittorie": 12, "num_sconfitte": 3,  "exp_pts": 1450},
    {"nome": "Giulia",  "num_vittorie": 9,  "num_sconfitte": 6,  "exp_pts": 1120},
    {"nome": "Luca",    "num_vittorie": 15, "num_sconfitte": 1,  "exp_pts": 1890},
    {"nome": "Sara",    "num_vittorie": 7,  "num_sconfitte": 8,  "exp_pts": 860},
    {"nome": "Davide",  "num_vittorie": 4,  "num_sconfitte": 11, "exp_pts": 530},
    {"nome": "Savato",  "num_vittorie": 0,  "num_sconfitte": 0, "exp_pts": 0},
]

nome = ""
while nome != "exit":

    nome = input("Inserisci Nome giocatore. Scrivi 'exit' per uscire: ").strip()
    nuovo_partecipante = {}

    trovata = False
    for n in partecipanti:
        if nome.casefold() == n["nome"].casefold():
            trovata = True
            break

    if trovata:
        print("Giocatore già presente.")
    else:
        vittorie = int(input("Numero di vittorie: "))
        sconfitte = int(input("Numero di sconfitte: "))
        esperienza = int(input("Punti esperienza: "))

        nuovo_partecipante = {
            "nome": nome,
            "num_vittorie": vittorie,
            "num_sconfitte": sconfitte,
            "exp_pts": esperienza
        }

        partecipanti.append(nuovo_partecipante)
        print("Giocatore aggiunto!")