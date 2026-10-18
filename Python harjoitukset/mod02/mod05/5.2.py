luvut = []
while True:
    luku = input("Anna luku (tyhjä lopettaa): ")
    if luku == "":
        break
    luvut.append(int(luku))
luvut.sort(reverse=True)
for luku in luvut:
    print(luku)
