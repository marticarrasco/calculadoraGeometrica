import math

def print2D(perimetre, area):
    print("Perímetre: " + str(perimetre))
    print("Àrea: " + str(area))

def quadrat(costat):
    perimetre = costat * 4
    area = costat ** 2

    print2D(perimetre, area)

def quadrilater(base, altura):
    perimetre = base*2 + altura*2
    area = base*altura

    print2D(perimetre, area)

def equilater_altura(altura):
    costat = (2*altura*(math.sqrt(3))) / 3

    perimetre = costat*3
    area = costat * altura / 2

    print2D(perimetre, area)

def equilater_costat(costat):
    altura = math.sqrt(costat**2 - (costat/2)**2)

    perimetre = costat*3
    area = costat * altura / 2

    print2D(perimetre, area)

def isosceles_altura_base(altura, base):
    catet = math.sqrt((base/2)**2 + altura**2)

    perimetre = base + catet*2
    area = base * altura / 2

    print2D(perimetre,area)

def isosceles_base_catet(base, catet):
    altura = math.sqrt(catet**2 - (base/2)**2)

    perimetre = catet*2 + base
    area = base * altura / 2

    print2D(perimetre, area)

def escale(altura, catet_1, catet_2, base):
    perimetre = catet_1 + catet_2 + base
    area = base * altura / 2

    print2D(perimetre, area)

def pentagon_radi(num_costats, costat, radi):
    apotema = math.sqrt((radi**2)-((costat/2)**2))

    perimetre = num_costats * costat
    area = costat*apotema/2*num_costats

    print2D(perimetre, area)

def pentagon_apotema(num_costats, costat, apotema):
    perimetre = costat * num_costats
    area = costat*apotema/2*num_costats

    print2D(perimetre, area)

def cercle_radi(radi):
    area = math.pi * radi**2
    perimetre = 2 * math.pi * radi

    print2D(perimetre, area)

def cercle_longitud(longitud):
    radi = longitud / (2*math.pi)

    area = math.pi * radi**2
    perimetre = 2 * math.pi * radi

    print2D(perimetre, area)

def cercle_diametre(diametre):
    radi = diametre/2

    area = math.pi * radi**2
    perimetre = 2 * math.pi * radi

    print2D(perimetre, area)

def cercle_area(area):
    radi = math.sqrt(area/math.pi)

    area = math.pi * radi**2
    perimetre = 2 * math.pi * radi

    print2D(perimetre, area)

def rombe(diagonal_1, diagonal_2):
    costat = math.sqrt((diagonal_1/2)**2 + (diagonal_2/2)**2)

    area = diagonal_1 * diagonal_2 / 2
    perimetre = costat*4

    print2D(perimetre, area)

def trapezi_h_a_b(h, a, b):
    costat = math.sqrt( ( (a-b) / 2)**2 + (h**2)  )

    area = ((a + b)/2)*h
    print("El perímetre només és correcte si el trapezi és regular.")
    perimetre = costat*2 + a + b

    print2D(perimetre, area)

def trapezi_a_b_c_d(a, b, c, d):
    altura = math.sqrt( c**2 - ( (c**2 - d**2 + (a-b)**2) / (2*(a-b)) )**2 )
    
    area = (a + b) / 2 * altura
    perimetre = a + b + c + d

    print2D(perimetre, area)