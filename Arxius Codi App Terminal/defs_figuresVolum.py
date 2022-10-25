import math

def print3D(perimetre, area, volum):
    print("Perímetre: " + str(perimetre))
    print("Àrea: " + str(area))
    print("Volum: " + str(volum))

def cub(costat):
    volum = costat ** 3
    area = costat**2 * 6
    perimetre = costat * 12

    print3D(perimetre, area, volum)

def prisme(base, altura, height):
    volum = base * altura * height
    area = 2*(base*altura+base*height+altura*height)
    perimetre = 4*(base+altura+height)

    print3D(perimetre, area, volum)

def con_diametre_altura(diametre, altura):
    radi = diametre/2
    generatriu = math.sqrt((radi**2) + (altura**2))
    area = math.pi * radi * generatriu + math.pi * radi**2
    volum = math.pi * radi**2 * altura / 3
    perimetre = 2*math.pi*radi

    print3D(perimetre, area, volum)

def con_generatriu_altura(generatriu, altura):
    radi = math.sqrt(generatriu**2 - altura**2)
    area = math.pi * radi * generatriu + math.pi * radi**2
    volum = math.pi * radi**2 * altura / 3
    perimetre = 2*math.pi*radi

    print3D(perimetre, area, volum)

def con_generatriu_diametre(generatriu, diametre):
    radi = diametre/2
    altura = math.sqrt(((generatriu) **2) - (radi**2))
    area = math.pi * radi * generatriu + math.pi * radi**2
    volum = math.pi * radi**2 * altura / 3
    perimetre = 2*math.pi*radi

    print3D(perimetre, area, volum)

def con_generatriu_radi(generatriu, radi):
    altura = math.sqrt(((generatriu) **2) - (radi**2))
    area = math.pi * radi * generatriu + math.pi * radi**2
    volum = math.pi * radi**2 * altura / 3
    perimetre = 2*math.pi*radi

    print3D(perimetre, area, volum)

def con_radi_altura(radi, altura):
    generatriu = math.sqrt((radi**2) + (altura**2))
    area = math.pi * radi * generatriu + math.pi * radi**2
    volum = math.pi * radi**2 * altura / 3
    perimetre = 2*math.pi*radi

    print3D(perimetre, area, volum)

def cilindre_altura_radi(altura, radi):
    area = 2*math.pi * radi**2 + (altura * (2*math.pi*radi))
    volum = math.pi * radi**2 * altura 
    perimetre = 2*math.pi*radi*2

    print3D(perimetre, area, volum)

def cilindre_diametre_altura(diametre, altura):
    radi = diametre / 2
    area = 2*math.pi * radi**2 + (altura * (2*math.pi*radi))
    volum = math.pi * radi**2 * altura 
    perimetre = 2*math.pi*radi*2

    print3D(perimetre, area, volum)

def esfera(radi):
    cercleInt = math.pi*radi**2
    area = cercleInt*4 
    volum = (4*math.pi*radi**3) / 3
    perimetre = 0

    print3D(perimetre, area, volum)

def piramide_ap_h(ap, h, costat, num_costat):
    apB = math.sqrt(ap**2 - h**2)

    ab = apB * costat / 2 * num_costat
    al = (ap * costat) / 2 * num_costat
    gen = math.sqrt(  (costat/2)**2 + ap**2  )

    area = ab + al
    volum = 1 / 3 * ab * h
    perimetre = num_costat*gen + num_costat*costat

    print3D(perimetre, area, volum)

def piramide_apB_h(apB, h, costat, num_costat):
    ap = math.sqrt(h**2 + apB**2)

    ab = apB * costat / 2 * num_costat
    al = (ap * costat) / 2 * num_costat
    gen = math.sqrt(  (costat/2)**2 + ap**2  )

    area = ab + al
    volum = 1 / 3 * ab * h
    perimetre = num_costat*gen + num_costat*costat

    print3D(perimetre, area, volum)

def piramide_apB_ap(apB, ap, costat, num_costat):
    h = math.sqrt(ap**2 - apB**2)

    ab = apB * costat / 2 * num_costat
    al = (ap * costat) / 2 * num_costat
    gen = math.sqrt(  (costat/2)**2 + ap**2  )

    area = ab + al
    volum = 1 / 3 * ab * h
    perimetre = num_costat*gen + num_costat*costat
    
    print3D(perimetre, area, volum)
