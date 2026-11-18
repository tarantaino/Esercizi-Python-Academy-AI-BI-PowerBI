"""
Realizzare una semplice calcolatrice che permetta di eseguire quattro operazioni matematiche: addizione, sottrazione, moltiplicazione
e divisione implementate con funzioni lambda.
Creare un dizionario in cui le chiavi siano i simboli delle operazioni e
i valori siano le corrispondenti funzioni lambda. Chiedere all'utente due numeri e l'operazione da eseguire.
Se l'operazione non è valida, visualizzare un messaggio di errore.
Gestire anche il caso in cui si tenti di dividere per zero.
"""
print("======= CALCOLATRICE =======")

diz_o = { #setto dizionario con operazioni arrotondate (vedi sotto)
    "+": lambda x,y: round(x + y, 2),
    "-": lambda x,y: round(x - y, 2),
    "*": lambda x,y: round(x * y, 2),
    "/": lambda x,y: round(x / y, 2),
}

while True: #avrei direttamente usato un try/except per escludere i caratteri alfabetici
    n1 = input("Benvenuto nella calcolatrice, inserisci primo numero: ").strip()
    n2 = input("Inserisci secondo numero: ").strip()
    if n1.isalpha() or n2.isalpha():
        print("Devi inserire due numeri!")
        continue
    elif not n1 or not n2: #controllo per evitare gli invio vuoti
        print("Devi inserire due numeri!")
        continue

    n1 = float(n1)
    n2 = float(n2) #trasformati in float e non int per far assumere valori con virgola, tutte le operazioni sono arrotondate a 2 cifre decimali (vedi sopra)
    # print(n1, n2) stampa di debug
    s = input("Inserisci il simbolo dell'operazione da effettuare sui due numeri (+, -, *, /): ").strip()

    if s not in diz_o: #esclude qualunque carattere che non sia un'operatore
        print("Operazione non valida!")
    elif s == "/" and n2 == 0:
        print("Impossibile dividere per 0")
    else:
        print(diz_o[s](n1,n2)) #passo la risposta s al dizionario che recupera l'operatore associato alla lambda a cui passo i due numeri

    break





