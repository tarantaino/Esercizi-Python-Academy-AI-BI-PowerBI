""" Ordina una lista di dizionari contenenti la coppia "eta: valore" per età crescente. """

ls_eta = [
    {"eta": 30},
    {"eta": 22},
    {"eta": 45},
    {"eta": 18},
]

ls_eta_cresc = sorted(ls_eta, key=lambda d: d["eta"])
print(ls_eta_cresc)


