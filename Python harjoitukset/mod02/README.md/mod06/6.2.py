import random
def heita_noppaa(tahkoja):
    return random.randint(1, tahkoja)

#pääohjelma
tahkoja = int(input("Anna nopan tahkojen määrä: "))
maksimi = int(input("Anna maksimisilmäluku, johon lopetetaan: "))

while True:
    silmaluku = heita_noppaa(tahkoja)
    print(f"Heitto: {silmaluku}")
    if silmaluku == maksimi:
        break