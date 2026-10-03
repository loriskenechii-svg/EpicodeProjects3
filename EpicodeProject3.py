
#Parte 1- Variabile e tipi di dati

nome = "Mario Rossi"
eta = 34
saldo = 2500.75
vip = True

destinazioni = [ "Roma", "Parigi", "Tokyo", "New York", "Cairo", "Bangkok", "Londra", "Los Angeles"]

prezzi_medi = { "Roma": 500.99, "Parigi": 650.40, "Tokyo": 1500.50, "New York": 1400.99, "Cairo": 900.0, "Bangkok": 1300.50, 
"Londra": 700.60, "Los Angeles": 1600.0}


#Parte 2 - Programmazione ad oggetti (OOP)

class Cliente:
    def __init__(self, nome, eta, vip):
        self.nome = nome
        self.eta = eta
        self.vip = vip

    def stampa_informazioni(self):
        print("Nome:", self.nome)
        print("Età:", self.eta)
        print("VIP:", self.vip)

class Viaggio:
    def __init__(self, destinazione, prezzo, durata):
        self.destinazione = destinazione
        self.prezzo = prezzo
        self.durata = durata

class Prenotazione:
    def __init__(self, cliente, viaggio):
        self.cliente = cliente
        self.viaggio = viaggio

    def calcola_importo_finale(self):
        if self.cliente.vip:
            return self.viaggio.prezzo * 0.90
        else:
            return self.viaggio.prezzo

    def dettagli(self):
        print("Cliente:", self.cliente.nome)
        print("Destinazione:", self.viaggio.destinazione)
        print("Prezzo:", self.viaggio.prezzo)
        print("Durata:", self.viaggio.durata)
        print("Importo finale:", self.calcola_importo_finale())

cliente1 = Cliente("Mario Rossi", 34, True)
viaggio1 = Viaggio("Parigi", 650.0, 5)
prenotazione1 = Prenotazione(cliente1, viaggio1)

cliente1.stampa_informazioni()
prenotazione1.dettagli()


#Parte 3 - NumPy

import numpy as np

prezzi_prenotazioni = np.random.uniform(200, 2000, 100)

prezzo_medio = np.mean(prezzi_prenotazioni)
print("Prezzo medio:", prezzo_medio)

prezzo_minimo = np.min(prezzi_prenotazioni)
prezzo_massimo = np.max(prezzi_prenotazioni)
print("Prezzo minimo:", prezzo_minimo)
print("Prezzo massimo:", prezzo_massimo)

deviazione_standard = np.std(prezzi_prenotazioni)
print("Deviazione standard:", deviazione_standard)

prenotazioni_sopra_media = np.sum(prezzi_prenotazioni > prezzo_medio)
percentuale_sopra_media = prenotazioni_sopra_media / 100 * 100
print("Percentuale di prenotazioni sopra la media:", percentuale_sopra_media)


# Parte 4 - Pandas

import pandas as pd

dati = { "Cliente": [ "Mario Rossi", "Anna Bianchi", "Luca Verdi", "Sara Neri", "Paolo Gialli", "Giulia Blu", "Marco Rosa", "Elena Viola", "Mario Rossi",
"Anna Bianchi", "Mario Rossi", "Luca Verdi"],

    "Destinazione": [ "Roma", "Parigi", "Tokyo", "New York", "Cairo", "Bangkok", "Londra", "Los Angeles", "Parigi", "Tokyo", "Cairo", "Parigi"],

    "Prezzo": [ 500.99, 650.40, 1500.50, 1400.99, 900.0, 1300.50, 700.60, 1600.0, 650.0, 1500.50, 900.0, 650.40],

    "Giorno_Partenza": [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ],

    "Durata": [ 4, 5, 10, 8, 7, 12, 5, 10, 6, 11, 8, 5 ],

    "Incasso": [ 450.50, 650.30, 1500.20, 1260.90, 900.80, 1300.10, 700.60, 1600.40, 585.10, 1500.20, 810.80, 650.30]
}

df = pd.DataFrame(dati)

incasso_totale = df["Incasso"].sum()
print("Incasso totale dell'agenzia:", incasso_totale)

incasso_medio_destinazione = df.groupby("Destinazione")["Incasso"].mean()
print("Incasso medio per destinazione:")
print(incasso_medio_destinazione)

top_3_destinazioni = df["Destinazione"].value_counts().head(3)
print("Top 3 destinazioni più vendute:")
print(top_3_destinazioni)


# Parte 5 - Matplotlib

import matplotlib.pyplot as plt

incasso_destinazione = df.groupby("Destinazione")["Incasso"].sum()

plt.bar(incasso_destinazione.index, incasso_destinazione.values)
plt.title("Incasso per destinazione")
plt.xlabel("Destinazione")
plt.ylabel("Incasso")
plt.xticks(rotation=45)
plt.show()

incasso_giornaliero = df.groupby("Giorno_Partenza")["Incasso"].sum()

plt.plot(incasso_giornaliero.index, incasso_giornaliero.values)
plt.title("Andamento giornaliero degli incassi")
plt.xlabel("Giorno")
plt.ylabel("Incasso")
plt.show()

vendite_destinazione = df["Destinazione"].value_counts()

plt.pie(
    vendite_destinazione.values,
    labels=vendite_destinazione.index,
    autopct="%1.1f%%"
)
plt.title("Percentuale di vendite per destinazione")
plt.show()


# Parte 6 - Analisi avanzata

categorie = { "Roma": "Europa", "Parigi": "Europa", "Tokyo": "Asia", "New York": "America", "Cairo": "Africa", "Bangkok": "Asia", "Londra": "Europa", "Los Angeles": "America"}

df["Categoria"] = df["Destinazione"].map(categorie)

incasso_totale_categoria = df.groupby("Categoria")["Incasso"].sum()
print("Incasso totale per categoria:")
print(incasso_totale_categoria)

durata_media_categoria = df.groupby("Categoria")["Durata"].mean()
print("Durata media dei viaggi per categoria:")
print(durata_media_categoria)

df.to_csv("prenotazioni_analizzate.csv", index=False)


# Parte 7 - Estensioni

def clienti_con_piu_prenotazioni(dataframe, N):
    prenotazioni_clienti = dataframe["Cliente"].value_counts()
    return prenotazioni_clienti.head(N)

N = 3

top_clienti = clienti_con_piu_prenotazioni(df, N)

print("Clienti con più prenotazioni:")
print(top_clienti)

incasso_medio_categoria = df.groupby("Categoria")["Incasso"].mean()
durata_media_categoria = df.groupby("Categoria")["Durata"].mean()

plt.bar(
    incasso_medio_categoria.index,
    incasso_medio_categoria.values,
    label="Incasso medio"
)

plt.plot(
    durata_media_categoria.index,
    durata_media_categoria.values,
    marker="o",
    label="Durata media"
)

plt.title("Incasso medio e durata media per categoria")
plt.xlabel("Categoria")
plt.ylabel("Valori")
plt.legend()
plt.show()