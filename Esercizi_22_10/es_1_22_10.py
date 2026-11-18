"""
1 - Scrivere un programma in Python che:
    .Acquisisca da tastiera un elenco di prodotti con i relativi prezzi.
    .Calcoli il totale della spesa.
    .Verifichi se è stato rispettato un budget predefinito.
    .Stampi un riepilogo completo della spesa.
"""

BUDGET = 10.00

#lista dizionari
magazzino = [
            {"Prodotto": "Latte", "Prezzo": 2.00},
            {"Prodotto": "Prosecco", "Prezzo": 18.00},
            {"Prodotto": "Formaggio", "Prezzo": 4.00},
            {"Prodotto": "Uova", "Prezzo": 4.50},
            {"Prodotto": "Pane", "Prezzo": 3.00},
]

print("===== MAGAZZINO =====")
for i in magazzino:
    print(i)

print("\n")


def spesa():
    somma = 0
    carrello = []

    prodotto = ""
    while prodotto != "Exit":
        prodotto = input(
            "Inserisci prodotto da acquistare, finché non sfori il budget. Scrivi 'exit' per uscire: ").strip().capitalize()
        for prod in magazzino:
            if prodotto == prod["Prodotto"]:
                carrello.append(prodotto)
                somma = somma + prod["Prezzo"]

    print(f"Il tuo carrello: {carrello}\n"
          f"Totale: {somma}")

    if somma > BUDGET:
        print("Non hai rispettato il budget.\n")
    else:
        print("Hai rispettato il budget.\n")



spesa()
