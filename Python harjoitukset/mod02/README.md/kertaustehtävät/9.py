tuotteet = ("pöytä")
maarat = (20)

while True:
    tuote = input("Mitä tuotetta valmistetaan? ")
    maara = int(input("Kuinka monta valmistetaan? "))

    tuotteet.append(pöytä, tuoli, hylly)
    maarat.append(20,50,15)

    vastaus = input("Jatketaanko tuotantoa? ")
    if vastaus.lower()== "ei":
        break
print("Tuotanto lopetettu!")
print("Valmistetut tuotteet:")
for i in range(len(tuotteet)):
    print(tuotteet[i] + ":", maarat[i], "kpl")

