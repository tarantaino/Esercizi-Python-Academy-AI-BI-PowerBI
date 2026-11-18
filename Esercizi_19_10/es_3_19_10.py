"""Un'azienda vuole analizzare le vendite effettuate dai propri dipendenti durante una settimana.
Crea un dizionario vendite in cui le chiavi siano i nomi dei dipendenti e i valori siano gli importi delle vendite effettuate.
Visualizza tutti i dipendenti con il rispettivo importo.
Calcola e visualizza il totale delle vendite usando la funzione sum().
Utilizza una list comprehension per creare una lista contenente i nomi dei dipendenti che hanno venduto per almeno 1.000 euro.
Utilizza una dictionary comprehension per creare un nuovo dizionario contenente soltanto i dipendenti con vendite superiori a 500 euro.
Utilizza una list comprehension per creare una lista contenente gli importi delle vendite aumentati del 10%, senza modificare il dizionario originale.
Individua il dipendente con il valore di vendita più alto."""

vendite = {
    "Ross":900,
    "Chandler":2000,
    "Monica":1100,
    "Rachel":1200,
    "Phoebe":800,
    "Joey":1000,
    "Gunther": 500 #aggiunto Gunther: 500 per debuggare la print del nuovo dict
}

for k,v in vendite.items():
    print(f"Dipendente: {k}, Importo: {v}") #dipendenti e importo

print("\n")#newline per separare
print(f"Totale vendite: {sum(vendite.values())}")
print("\n")#newline per separare

ls_vendite = [k for k,v in vendite.items() if v >= 1000]
print(f"Dipendenti che hanno venduto almeno 1000: {ls_vendite}")
print("\n")#newline per separare

dic_vendite = {k: v for k,v in vendite.items() if v > 500}
print(f"Dipendenti con vendite superiori a 500: {dic_vendite}")
print("\n")#newline per separare

ls_vendite_magg = [(round(v*1.1)) for v in vendite.values()] #uso round per arrotondare
print(f"Importi delle vendite maggiorate del 10%: {ls_vendite_magg}")
print("\n")#newline per separare

massimo = max(vendite.values())#setto variabile con il valore di vendite più alto da usare nell'if successiva
print(f"Il dipendente che ha effettuato la vendita del valore più alto: {[(k,v) for k,v in vendite.items() if v == massimo]}")
#creazione tupla per trovare il dipendente con le vendite più alte
