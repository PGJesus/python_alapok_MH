# x = 1
# while x <= 4:
#     y = 1
#     while y <= 7:
#         print('O ', end='')
#         y += 1
#     print('')
#     x += 1

"""1. Feladat - Pocak
Készíts egy programot, amely a felhasználótól bekér egy páros számot, majd ennek megfelelően rajzol ki a képernyőre 
egy pocak szerű alakzatot az alábbiak szeri"""

# sor = int(input("Adj meg egy páros számot: "))


darab_karakter = 1
sor = 1
while sor <= 7:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('O ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1

