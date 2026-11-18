"""Scrivere un programma che analizzi una stringa e conti quante volte compare un determinato carattere."""

while True: #finché è vero esegui vvv
    p = input("Inserisci una parola: ").strip() #verifico che l'utente non invii in input una stringa vuota o uno spazio
    if not p.isalpha(): #con isalpha() verifico che la stringa sia composta esclusivamente da caratteri alfabetici
        print("Devi inserire una parola!\n")
        continue
    break

while True: #nuovo ciclo con gli stessi controlli
    c = input("Inserisci il carattere da cercare: ").strip()
    if not c.isalpha() or len(c) != 1: #mi serve solo un carattere non una stringa più lunga
        print("Devi inserire un solo carattere!\n")
        continue

    i = 0 #contatore
    for l in p: #stesso ciclo del primo esercizio che conta quante occorrenze ci sono del carattere scelto all'interno di p
        if l in c:
            i+=1


    print(f"Il carattere {c} compare: {i} volte")

    break