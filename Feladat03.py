szam = int(input("Adj meg egy számot!"))
if szam < 0:
    print("A megadott szám negatív.")
elif szam == 0:
    print("A megadott szám nulla.")
elif szam == 4:
    print("jhin")
else:
    print("A megadott szám pozitív.")
print("A program vége.")

"""1.1 Feladat
Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e! A válasz kétféle lehet:
igen vagy nem. A választól függően írjon ki üzenetet a gép!"""

valasz = input("Jó napja volt? (igen, nem) ")
valasz_lowercase = valasz.lower()
if valasz_lowercase == "igen":
    print("Neked a jó!")
elif valasz_lowercase == "nem":
    print("Ez van. Az élet néha fáj")
else:
    print("Sajnos nem értem a válaszod.")

"""2. Feladat
Készíts egy programot, ami bekér egy számot a felhasználótól, majd kiírja, hogy a megadott szám páros-e vagy páratlan!

[Tipp] A maradékos osztás segít! Mennyivel is kell elosztanod a számot maradékosan, hogy kiderüljön páros-e?
Ebben az esetben mennyi lesz a maradék?"""

adat = int(input("Adj egy számot!"))
if adat == //2
    print("A szám páros")