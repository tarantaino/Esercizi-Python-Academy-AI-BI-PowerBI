"""
3 - Scrivi un programma che permette un  massimo di 5 tentativi per inserire una password.
    Se la password è vuota stampa "Password non valida".
    Se la password è "admin123" stampa "Accesso consentito" ed interrompe il programma.
    Se finisce i tentativi senza successo stampa "Accesso negato".
"""

for i in range(5):
    psw = input("Inserisci password: ")
    if psw == "admin123":
        print("Accesso consentito.\n")
        break
    elif psw == "" or psw == " ":
        print("Password non valida.")
    else:
        print("Accesso negato.\n")
        continue

