"""3 - Data una lista di nomi, vuoi raggrupparli per iniziale nel seguente modo:

es:

{
    "L": ["Luca", "Leonardo"],
    "A": ["Anna"],
    "M": ["Marco"]
}

"""

def d_iniziali(lista):
    diz_iniziali = {} #inizializzazione dizionario

    for n in lista: #per ogni nome nella lista
        if n[0] not in diz_iniziali: #se il nome[0] non è chiave nel dizionario
            diz_iniziali[n[0]] = [] #la associo ad una lista vuota
        diz_iniziali[n[0]].append(n) #dopodiché se la chiave esiste aggiungo il nome intero alla lista iniziale

    print(f"Dizionario delle iniziali e nomi associati:\n {diz_iniziali}")



ls_nomi = ['Alessandro', 'Anna', 'Maria', 'Giorgio', 'Gaetano']
d_iniziali(ls_nomi)