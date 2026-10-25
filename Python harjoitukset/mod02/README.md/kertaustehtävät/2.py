luku = int(input("Anna kokonaisluku: "))
if luku % 3 == 0 and luku % 5 == 0:
    print("Jaollinen molemmilla luvuilla!")
elif luku % 3 == 0:
    print("Jaollinen kolmella!")
elif luku % 5 == 0:
    print("Jaollinen viidellä!")
else:
    print("Ei ole jaollinen eikä kolmella eikä viidellä.")
    