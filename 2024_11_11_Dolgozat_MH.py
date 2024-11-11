# A csoport:
# Készítsünk programot, amely dinnyék csomagolásához végez számításokat. A
# dinnyéket szalaggal kell átkötni úgy, hogy kétszer körbe érje őket, és a masni
# készítéséhez számolunk még 60 cm-t. A program kérje be a dinnye átmérőjét, a
# dinnyék számát, és a rendelkezésre álló szalag hosszát! Számítsa ki, és írja a
# képernyőre, hogy a bekért számú dinnye csomagolásához hány méter szalagra van
# szükség, valamint állapítsa meg, hogy elegendő szalagunk van-e a művelet
# elvégzéséhez, és ezt is közölje a felhasználóval!


def dinnye_doga():
    atmero = float(input("Add meg a dinnye átmérőjét!(cm-ben) "))
    dinnyek_szama = int(input("Add meg a dinnyék számát! "))
    szalag_hossz = float(input("Adja meg a rendelkezésre álló szalag hosszát!(méterben) ")) * 100

    szukseges_hossz_cm = (2 * 3.14 * (atmero / 2) * 2 + 60) * dinnyek_szama
    szukseges_hossz_m = szukseges_hossz_cm / 100

    print(f"A dinnyék csomagolásához szükséges szalag: {szukseges_hossz_m:.2f} méter.")

    if szalag_hossz >= szukseges_hossz_cm:
        print("Van elég szalag.")
    else:
        print("Nincs elegendő szalag.")

dinnye_doga()