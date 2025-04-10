import random

tajne_cislo = random.randint(1, 10)
pokus = 0

print("Hádej číslo od 1 do 10!")

while True:
    tip = int(input("Zadej svůj tip: "))
    pokus += 1

    if tip == tajne_cislo:
        print(f"Správně! Uhodl(a) jsi číslo na {pokus}. pokus.")
        break
    elif tip < tajne_cislo:
        print("Myslím si větší číslo.")
    else:
        print("Myslím si menší číslo.")
