import datetime

print("Pozdrav!")

opravila = {}

while True:
    zeliOpravilo = input("Želiš vnesti opravilo? (da/ne): ") == "da"

    if not zeliOpravilo:
        break

    imeOpravila = input("Vnesi opravilo: ")    
    jeZakljuceno = input("Je zaključeno? (da/ne): ") == "da"

    if jeZakljuceno:
        casZakljucka = input("Čas zaključka: ")
        opravila[imeOpravila] = casZakljucka
    else:
        opravila[imeOpravila] = None

for imeOpravila in opravila:
    print()
    print("--> ",imeOpravila)
    opravilo = opravila[imeOpravila]
    print("  Zaključeno: " + opravilo if opravilo else "  Ni zaključeno.")
