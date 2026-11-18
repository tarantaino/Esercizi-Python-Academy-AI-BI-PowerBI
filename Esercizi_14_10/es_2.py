"""
2 - Scrivi un programma che chieda all’utente quanti voti vuole inserire e, per ogni voto, se risulta >= 18 stampa "Promosso", altrimenti stampa "Bocciato". Alla fine stampa quanti promossi e quanti bocciati ci sono.
"""

while True:
    num_voti = input("Quanti voti vuoi inserire? ").strip()  #controllo sul numero di voti da inserire che deve essere maggiore di 0
    if not num_voti.isdigit() or int(num_voti) == 0:
        print("Devi inserire un numero maggiore di 0!\n")
        continue
    num_voti = int(num_voti)
    break #fine blocco richiesta numero voti con controlli

p = 0  #varibaili conteggio promossi e bocciati settate a 0
b = 0

for i in range(num_voti): #entro nel ciclo che itera in base al numero di voti scelto
    while True:
        voto = input("Inserisci un voto: ").strip() #controlli sull'input (se stringa vuota o carattere alfaebtico)
        if not voto.isdigit():
            print("Devi inserire un valore numerico!\n")
            continue
        voto = int(voto)
        if voto > 30: #il voto non deve essere maggiore di 30
            print("Il voto deve essere compreso tra 0 e 30!\n")
            continue
        break
#controlli e conteggio
    if voto >= 18:
        print("Promosso")
        p += 1
    else:
        print("Bocciato")
        b += 1

    i+=1 #incremento

    #stampa
    print("Promossi:", p)
    print("Bocciati:", b)