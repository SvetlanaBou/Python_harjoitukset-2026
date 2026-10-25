tuntipalkka = float (input("Anna tuntipalkka: "))
tunnit = float(input("Anna työtunnit: "))
paiva = input ("Anna viikonpäivä: ")

if paiva.lower ()== "sunnuntai":
    palkka = tuntipalkka * tunnit * 2
else:
    palkka = tuntipalkka * tunnit
    print ("Paiväpalkka:",palkka, " euroa")

