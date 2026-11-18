"""
2) Scrivi un dizionario con alcune voci (ad esempio nomi di città e le relative temperature).
 Chiedi all’utente di inserire il nome di una città, e stampa la temperatura corrispondente.
 Gestisci il caso in cui la città non sia presente nel dizionario.

"""

def chiedi_utente():

    while True:
        i = input("Quale città vuoi visualizzare? ").strip().capitalize()

        try:
            print(f"Temperature di {i}: {meteo[i]}")
            break
        except KeyError:
            print(f"Errore - {i} non è presente nella lista!\n")


print("=== METEO ===\n")

meteo = {
    "Roma": 18.5,
    "Milano": 12.0,
    "Napoli": 20.3,
    "Torino": 10.8,
    "Palermo": 22.1,
    "Pisa": 15.6,
}


print("Elenco città: ")
for i in meteo.keys():
        print(f"{i}")

print("\n")


chiedi_utente()