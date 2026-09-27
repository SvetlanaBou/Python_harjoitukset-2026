 sukupuoli = input("Oletko nainen vai mies? ")
arvo = float(input("Anna hemoglobiiniarvo:"))

if sukupuoli == "nainen":
	alaraja = 117
	ylaraja = 175
else:
	alaraja = 134
	ylaraja = 195

if arvo < alaraja:
	print("Alhainen")
elif arvo > ylaraja:
	print("Korkea")
else:
	print("Normaali")
