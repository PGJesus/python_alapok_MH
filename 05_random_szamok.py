# 1. Feladat
# Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott,
# szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!


import random

# random_szam = random.randint(1, 3)
# szam = int(input("Adj egy számot! "))
#
# if random_szam < szam:
#     print("A megadott szám nagyobb mint a random.")
# elif random_szam == szam:
#     print("A megadott szam egyenlő a randommal.")
# else:
#     print("A megadott szam kisebb a randomnál.")
# print(random_szam)

erme =["fej", "írás"]
gep = random.choice(erme)

tipp = input("Fej vagy írás? ")

if gep == tipp:
    print("Win")
else:
    print("Lose")

print(f"Helyes: {gep}")