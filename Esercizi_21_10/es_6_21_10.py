"""
Un'applicazione permette di accedere a una funzione riservata esclusivamente agli utenti amministratori.
Creare un decorator chiamato solo_admin che controlli il valore del parametro ruolo.
Se il ruolo è "admin", la funzione deve essere eseguita; altrimenti, deve essere visualizzato un messaggio che indichi che l'accesso è negato.
 Creare una funzione visualizza_report che riceva il ruolo dell'utente e stampi il contenuto di un report riservato.
 Applicare il decorator e provare la funzione sia con un utente amministratore sia con un utente normale.
 Infine, utilizzare una funzione lambda per verificare se un ruolo corrisponde a "admin"
"""

verifica_admin = lambda role: role == "admin"
#lambda che verifica il ruolo

def solo_admin(func):#decorator
    def wrapper(role, *args, **kwargs): #wrapper
        if verifica_admin(role):
            return func(role, *args, **kwargs)
        else:
            print("<!> - Accesso negato. Utente non autorizzato. - <!>")

    return wrapper

@solo_admin #posizionamento wrapper
def visualizza_report(role):
    print("Ecco il tuo report:\n")
    print("RECEIVING TRANSMISSION..."
          "\n\n"
          "I've seen things you people wouldn't believe.\n"
          "Attack ships on fire off the shoulder of Orion.\n"
          "I watched c-beams glitter in the dark near the Tannhäuser Gate.\n"
          "All those moments will be lost in time, like tears in rain.\n"
          "Time to die.\n"
          "\n"
          "...END OF TRANSMISSION"
          )

utente_role = input("Per visualizzare il report inserisci il tuo ruolo utente: ").strip()
visualizza_report(utente_role) #invoke