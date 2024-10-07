"""1. Feladat
Thonny fejlesztői környezetben készíts egy rövid programot, amely
kommentként tartalmazza a program funkciójának leírását,
konstansként tárolja PI értékét,
egy másik változóban tárolja egy kör sugarának nagyságát (cm-ben megadva),
kiszámolja és a képernyőre kiírja a kör kerületét és területét!"""

#Pi értéke
PI = 3.14
#sugár értéke cm-ben
r = 5

#Kerület számítás
print("kerület:")
print(2*r*PI,"cm")

#Terület számítás
print("terület:")
print(r*r*PI,"cm^2")

#2. Feladat
"""Készíts egy rövid programot, amely egy változóban eltárol egy szót. Próbáld meg ennek a változónak a tartalmát int 
értékké átalakítani. Mit tapasztalsz? Milyen üzenet jelenik meg a képernyőn?"""

a = "Dénes"
if a.isdigit():
    print(int(a))
else:
    print(a)
#ValueError: invalid literal for int() with base 10: 'Dénes'

"""3. Feladat
Készíts egy rövid programot, amelyben egy olyan változó értékét szeretnéd kiíratni, ami előzőleg nem is szerepel a kódodban. 
Hogyan jelöli a fejlesztői környezet a hibát? Futtasd! Milyen hibaüzenetet kapsz?"""

print(x)
x="rig"