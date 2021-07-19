
# 1. A felhasználótól kérjen be két pozitív számot és nézze meg,
# hogy a nagyobbikkal osztható-e a kisebbik. Ha valamelyik
# nem pozitív, dobjon ki egy hibaüzenetet és menjen tovább!
print(" 1. feladat")
print()
a = int(input(" Adja meg az első számot: "))
b = int(input(" Adja meg a második számot: "))

def KisebbOsztja():
    if ( a <= 0 or b <= 0):
        print(" A megadott számok közül legalább az egyik negatív!")
    else:
       if(a>=b and a % b == 0) or (b>=a and b % a == 0):
           print(" A nagyobb szám osztható a kisebbel!")
       else:
           print(" A nagyobbik szám nem osztható a kisebbikkel!")
    print()
KisebbOsztja()

# 2.A titkosítás során szükség van különböző számokra.
# Kérjünk be egy szöveget, akkor azt el tudjuk tolni
# megadott érétkkel.
# Kérj be egy szöveget, majd generálj ki egy számot 1 és
# szöveg hossza között.
# Írj egy függvényt aminek az értéke ez: a szöveg elcsúsztatása.
import random
print(" 2. feladat")
print()
szoveg = input(" Adjon meg egy szöveget: ")
vel = random.randint(1,len(szoveg))-1
def Elcsusztatas():
    szovegeleje = szoveg[0:vel:1]
    szovegvege = szoveg[vel:len(szoveg):1]
    print(" Az elcsúsztatott szöveg: ", end='')
    print(szovegvege+szovegeleje)
    print()
Elcsusztatas()

# 3. adatok.txt állomány olvassa be és állapítsa meg a számok
# terjedelmét függvények segítségével!
# Van-e a számok között prím szám?         f.readline
# # list(map(int, f.readline.....
# global lista              beépített függvények: min(lista)
# lista = []                                      max(lista)
def Beolvasas():
    f = open("adatok.txt", "r")
    global adatok
    adatok = []
    adatok = list(map(int, f.readline().split(' ')))
    print(adatok)
    print()
Beolvasas()

def Terjedelem():
    maxi = 0
    for i in range(1,len(adatok)):
        if adatok[maxi] < adatok[i]:
            maxi = i
    print(adatok[maxi])
    mini = 0
    for i in range(1,len(adatok)):
        if adatok[mini] > adatok[i]:
            mini = i
    print(adatok[mini])
    print(" A beolvasott adatok terjedelme: ", str(adatok[maxi]-adatok[mini]))
    print()
Terjedelem()

def VanePrim():
    i = 2
    j = 0
    while j < len(adatok) and adatok[j] % i == 0:
            j += 1
    if j == len(adatok):
        print(" Nincs primszám!")
    else:
        print(" Van primszám!")
VanePrim()

lista = ['alma', 'körte', 'pöffeteg']
celfajl = open('adatok.txt', 'a') # 'a'- val a meglévő adatokhoz fűzi a beírásunkat
for elem in lista:                # 'w'- vel felülírja a meglévő fájlt
    print(elem, file=celfajl)
celfajl.close()
print("kész!")