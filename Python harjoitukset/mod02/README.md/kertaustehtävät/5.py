tarina = " Olipa kerran kauan sitten suuri vihreä lohikäärme."
while True:
    sana = input ("anna sana: ")
    if sana == "loppu":
        break
    tarina += sana + " "
    print(tarina.strip())
    