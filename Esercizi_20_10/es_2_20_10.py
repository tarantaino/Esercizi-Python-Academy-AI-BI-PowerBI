"""
2 - Data una lista di tuple, ogni tupla rappresenta un voto per gli studenti.

es:

[("Luca", 7), ("Anna", 8), ("Luca", 6)]

Vuoi calcolare la media dei voti per ogni studente sottoforma di dizionario.

"""
def dizionario_media(tupla):
    """

    :param tupla: Tupla con nomi e voti da passare
    :return: None
    """
    diz_media = {} #creiamo diz vuoto
    for n,v in tupla: #per ogni nome e voto all'interno della tupla
        somma = 0 #variabile per somma a 0
        conteggio = 0 #conteggio voti a 0
        for n2, v2 in tupla: #per ogni nome2 e voto2 in tupla
            if n2 == n: #se uguali, per eliminare i duplicati
                somma +=v2 #aggiungi v2 alla somma
                conteggio +=1 #aumenta il conteggio
        diz_media[n] = somma/conteggio #ad ogni nome, associamo la media

    print(f"Studenti e media dei voti: {diz_media}")


stud_voti = [("Usagi", 9), ("Ami", 6), ("Minako", 5), ("Usagi", 6), ("Minako", 8)]
dizionario_media(stud_voti)