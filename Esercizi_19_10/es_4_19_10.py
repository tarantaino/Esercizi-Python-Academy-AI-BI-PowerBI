"""
4 - Sei il programmatore di un videogioco Pokémon e devi realizzare un piccolo sistema per gestire una squadra di allenatori durante un torneo.

Ogni allenatore possiede una squadra di Pokémon e ogni Pokémon ha un nome, un livello e un numero di punti esperienza.
Per rappresentare i dati, crea un dizionario chiamato allenatori, in cui le chiavi siano i nomi degli allenatori e i valori siano liste contenenti i nomi dei Pokémon posseduti.

Crea almeno quattro allenatori, ognuno con almeno tre Pokémon. Alcuni Pokémon possono essere posseduti da più allenatori.

Successivamente, realizza un programma Python che visualizzi tutti gli allenatori con i rispettivi Pokémon
e permetta di aggiungere un nuovo Pokémon alla squadra di un allenatore esistente.

Il programma deve inoltre individuare tutti i Pokémon diversi presenti nel torneo, senza ripetizioni,
e salvarli in un set.
Utilizzando una set comprehension, crea un insieme contenente soltanto i Pokémon il cui nome contiene almeno cinque caratteri.

Per simulare la preparazione al torneo, crea poi un dizionario chiamato livelli, in cui ogni Pokémon presente nel torneo sia associato al proprio livello.
Utilizza una dictionary comprehension per creare un nuovo dizionario contenente soltanto i Pokémon che hanno raggiunto almeno il livello 30.

Infine, utilizza una list comprehension per creare una lista
contenente i nomi dei Pokémon che hanno raggiunto almeno il livello 30, ordinati in base ai dati presenti nel dizionario, e visualizza il risultato.

Il programma deve utilizzare liste, dizionari, set e tutte e tre le tipologie di comprehension studiate a lezione.

"""
#Creazione allenatori
import random #servirà dopo per i livelli

allenatori = {
    "Rosso" : ["Pikachu", "Pidgeot", "Charizard"],
    "Blu" : ["Pidgeot", "Blastoise", "Alakazam"],
    "Verde" : ["Venusaur", "Pidgeot", "Clefable"],
    "Billy" : ["Eevee", "Flareon", "Vaporeon"]
}

#visualizzazione allenatori
print(f"Allenatori e squadre del torneo:\n {allenatori}")
print("\n")

while True: #ciclo per l'input + controlli
    r = input("Vuoi aggiungere dei Pokémon? [S/N] ").strip() #richiesta eventuale inserimento pokemon per allenatore + controlli
    if r.lower() == "s":
        for k,v in allenatori.items():
            nom_pok = input(f"Inserisci nuovo Pokémon per {k}: ").strip() #ciclo per inserire i pokemon per allenatore
            nom_pok = nom_pok.capitalize() #prima lettera maiuscola
            allenatori[k].append(nom_pok) #aggiungiamo l'input alla lista
        break
    elif r.lower() == "n":
        break


print("\n") #creazione set pokemon unici
pokemon_unici = {p for v in allenatori.values() for p in v} #creazione set con i singoli pokemon, primo for che scorre i values e il secondo che scorre le liste appartenenti ai values
print(f"Lista Pokémon unici degli allenatori: {pokemon_unici}")
print("\n")

#set con pokemon che hanno un nome più lungo di 5 caratteri
pokemon_5_char = {p for p in pokemon_unici if len(p) >= 5}
print(f"Set di Pokémon con un nome più lungo di 5 caratteri:\n {pokemon_5_char}")
print("\n")

#importato random per inserire i livelli dei pokemon, random tra 25 e 100 per testare la richiesta successiva
print("Livello raggiunto dai Pokémon iscritti al torneo:\n")
lvl = {p: random.randint(25,100) for p in pokemon_unici}
print(lvl)
print("\n")

#creazione dizionario pokemon con livello superiore o uguale al 30
lvl_magg = {p: l for p, l in lvl.items() if l >=30}
print(f"Pokémon con Livello maggiore o uguale al 30:\n {lvl_magg}")
print("\n")

#creazione lista dei pokemon con livello superiore o uguale al 30
lvltrenta = [k for k,v in lvl.items() if v >= 30]
print(f"Lista dei Pokémon dal Livello 30 in su:\n {lvltrenta}")


