import datetime

print("Pozdrav")

opravila = {}

while True:
    zeliOpravilo = input("Želiš vnesti opravilo? (da/ne): ") == "da"

    if not zeliOpravilo:
        break

    imeOpravila = input("Vnesi opravilo: ")
    jeZakljuceno = input("Je zaključeno? (da/ne): ") == "da"

    if jeZakljuceno:
        casZakljucka = input("Čas zaključka: ")
        opravila[imeOpravila] = {True, casZakljucka}
    else:
        opravila[imeOpravila] = {False}

for imeOpravila in opravila:
    print()
    print("--> ",imeOpravila)
    opravilo = opravila[imeOpravila]
    if True in opravilo:
        opravilo.remove(True)
        for e in opravilo:
            print("  Zaključeno: " + e)
    else:
        print( "  Ni zaključeno.")
