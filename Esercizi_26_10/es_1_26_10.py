"""
1) Scrivi un programma che chieda all’utente due numeri e un’operazione (+, -, *, /) da eseguire.
Il programma deve gestire i seguenti errori:

- Inserimento non numerico
- Divisione per zero
- Operazione non valida

"""

print("=== OPERAZIONI ===")

diz_o = {  # prendo dizionario con le lambda da esercizio precedente
        "+": lambda x, y: round(x + y, 2),
        "-": lambda x, y: round(x - y, 2),
        "*": lambda x, y: round(x * y, 2),
        "/": lambda x, y: round(x / y, 2),
    }

def chiedi_numeri():
#funzione per chiedere i numeri in input, while True per continuare a chiedere in caso di errore
    while True:
       try: #blocco try/except nel caso di ValueError
            x = float(input("Inserisci primo numero: "))
            y = float(input("Inserisci secondo numero: "))
            return (x, y)
       except ValueError:
           print("Devi inserire un numero!\n")

def operazione(x,y): #passo x,y
#input operazione, se si trova nel dizionario altro try/except sul ZeroDivisionError
    while True:
        o = input("Inserisci operazione (+,-,*,/): ").strip()
        if o in diz_o:
           try:
            return f"Risultato: {diz_o[o](x,y)}"
           except ZeroDivisionError:
               return "ERRORE - Non è possibile dividere per 0!"
        print("Simbolo non valido!")


x, y = chiedi_numeri()
print(operazione(x,y))

