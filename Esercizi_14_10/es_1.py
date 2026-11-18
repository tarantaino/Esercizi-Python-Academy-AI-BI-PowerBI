"""1 - Scrivi un programma Python che chieda all’utente di inserire una parola per poi:

1 - Stampare tutti i caratteri uno alla volta
2 - Stampi solo i caratteri in posizione dispari (indice 1, 3, 5…)
3 - Conti quante vocali (a, e, i, o, u) ci sono nella parola e stampi il risultato

N.B. l’operatore “in” serve a verificare se un elemento è contenuto in una sequenza o in una collezione. Restituisce sempre o “True” o “False”."""

while True: #finché è vero esegui vvv
    p = input("Inserisci una parola: ").strip() #verifico che l'utente non invii in input una stringa vuota o uno spazio
    if not p.isalpha(): #con isalpha() verifico che la stringa sia composta esclusivamente da caratteri alfabetici
        print("Devi inserire una parola!\n")
        continue #consente di ripetere l'operazione se l'utente ha inserito valori non previsti ^^^

    for i in range(len(p)):
        print(p[i]) #stampa caratteri singoli
        i+=1

    print("\n") #new line per separare i blocchi di operazioni in stampa

    for i in range(1, len(p), 2): #contatore che inizia parte da 1 e somma 2 finché non arriva alla lunghezza della stringa in modo tale da ottenere i caratteri in posizione dispari
        print(p[i])

    print("\n")

    vocali = "aeiou"
    c = 0
    for l in p.lower(): #nel dubbio metto tutto in minuscolo, per ogni l=lettera in p, se lettera compare in vocali, aumenta il contatore c, esce fuori e stampa il numero di vocali
        if  l in vocali:
                c += 1


    print("Numero di vocali all'interno: ", c)


    break #fine
    