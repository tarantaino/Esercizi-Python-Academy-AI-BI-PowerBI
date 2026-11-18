"""2 - Scrivere un programma Python che gestisca un elenco di partecipanti a un corso di informatica.

Il programma deve svolgere le seguenti operazioni:
1. Creare una lista contenente alcuni nomi.
2. Stampare a video l'intera lista dei partecipanti.
3. Stampare il primo e l'ultimo nome della lista.
4. Stampare i primi tre nomi della lista.
5. Stampare gli ultimi due nomi della lista.
6. Stampare i nomi dei partecipanti dalla seconda alla quinta posizione.
7. Stampare il nome più lungo presente nella lista.
8. Creare una nuova lista contenente i nomi scritti in ordine inverso e stamparla.
9. Stampare il numero totale dei partecipanti.
"""

partecipanti = ["Bulbasaur", "Charmander", "Squirtle", "Caterpie", "Weedle", "Pidgey"]
print(partecipanti)
print(f"Dal primo all'ultimo: {partecipanti[0], partecipanti[5]}") #stampa primo e ultimo elemento
print(f"I primi tre: {partecipanti[0:3]}") #stampa i primi 3
print(f"Ultimi tre: {partecipanti[3:]}") #stampa gli ultimi
print(f"Dalla seconda alla quinta posizione: {partecipanti[1:5]}") #stampa dalla seconda alla quinta posizione
l=0
for nome in partecipanti:
    if len(nome)>l:
        l = len(nome)
        nome_piu_lungo = nome

nome_piu_lungo=set()
for nome in partecipanti:
    if len(nome) == l:
        nome_piu_lungo.add(nome)

if len(nome_piu_lungo)==1:
    print(f"Il nome più lungo dei partecipanti è: {max(partecipanti)}") #stampa il nome più lungo


print("\n")
partecipanti_reversed = partecipanti[::-1]
print(f"Lista inversa: {partecipanti_reversed}")

print("\n")
print(f"Numero totale di partecipanti: {len(partecipanti)}") #stampa il numero totale dei partecipanti