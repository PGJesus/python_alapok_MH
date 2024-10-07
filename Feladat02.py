"""1. Feladat
Thonny fejlesztői környezetben készíts egy rövid programot, amely a felhasználótól bekéri a kör sugarát,
és ennek alapján kiszámolja a kör kerületét és területét!"""

#Pi értéke
PI = 3.14
#sugár értéke cm-ben
r = int(input("Adjá egy számot! "))

#Kerület számítás
print("kerület:")
print(2*r*PI,"cm")

#Terület számítás
print("terület:")
print(r*r*PI,"cm^2")