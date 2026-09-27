pienin = None
suurin = None

syote = input("Anna luku: ")

while syote != "":
	luku = float(syote)

	if pienin is None or luku < pienin:
		pienin = luku

	if suurin is None or luku > suurin:
		suurin = luku

	syote = input("Anna luku: ")

if pienin is None:
	print("Et antanut lukuja.")
else:
	print("Pienin:", pienin)
	print("Suurin:", suurin)
