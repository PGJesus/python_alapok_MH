"""2. Feladat - \
Készíts egy programot, amely egymásba ágyazott ciklusok segítségével rajzolja ki egy 5 x 5-ös mezőben az alábbi alakzatot!
O . . . .
. O . . .
. . O . .
. . . O .
. . . . O """

# for i in range(5):
#     for j in range(5):
#         print(f"{i}{j}", end=" ")
#     print()


# for i in range(5):
#     for j in range(5):
#         if i == j:
#             print("O", end=" ")
#         else:
#             print(".", end=" ")
#     print()


"""3. Feladat - X
Készíts egy programot, amely egymásba ágyazott ciklusok segítségével rajzolja ki egy 7 x 7-es mezőben az alábbi alakzatot!

O . . . . . O 
. O . . . O .
. . O . O . .
. . . O . . .
. . O . O . .
. O . . . O .
O . . . . . O """

size = int(input("Adj egy számot!"))

for x in range(size):
    for y in range(size):
        if x == y or (x+y) == size -1:
            print("O", end=" ")
            print("O", end=" ")
        else:
            print(".", end=" ")
    print()