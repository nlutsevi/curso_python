siglos = ["XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI"]

años = range(1000, 2100, 100)

i = 0

for año in años:
    while i<=10:
        print("año " + str(año) + " - siglo " + siglos[i])
        año += 100
        i += 1
print("Fin del programa")