"""2 - Un team di supporto ha raccolto le parole chiave più frequenti presenti nei ticket ricevuti.

ticket = "
login errore password login accesso
timeout login errore password
errore timeout login
"

Trasforma il testo in una lista di parole, per conta quante volte compare ogni parola,
stampa il conteggio completo, stampa le 3 parole più frequenti, individua quali parole compaiono una sola volta.

N.B. prova ad utilizzare il metodo most_common() della classe Counter."""

from collections import Counter
#import modulo Counter
ticket = "login errore password login accesso timeout login errore password errore timeout login"

ls_ticket = ticket.split() #creo lista
#print(ls_ticket)#stampa di debug

cnt_compl = Counter(ls_ticket)
print(f"Conteggio completo: {cnt_compl}")
print("\n")
print(f"Le 3 parole più frequenti sono: {cnt_compl.most_common(3)}")
print("\n")
#ciclo che cerca l'elemento che compare solo una volta + stampa
for k,v in cnt_compl.items():
    if v == 1:
        print(f"Le parole che si ripetono solo una volta sono: {k,v}")