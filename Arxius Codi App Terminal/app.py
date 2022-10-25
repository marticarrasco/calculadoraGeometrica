import math

from defs_figuresPlanes import *
from defs_figuresVolum  import *

def inputNoCorrecte():
    print("Input no correcte!")

print("1. Figures Planes  2. Figures amb Volum")
chose1 = int(input())

if (chose1 == 1):
    print("1. Quadrat  2. Quadrilàter  3. Triangle  4. Pentàgon")
    print("5. Cercle   6. Rombe        7. Trapezi")

    chose2 = int(input())

    if (chose2 == 1):
        costat = int(input("Costat: "))
        quadrat(costat)

    elif (chose2 == 2):
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        quadrilater(base, altura)

    #TRIANGLES
#region
    elif (chose2 == 3):
        print("1. Equilàter  2. Isòsceles  3. Escalè")
        chose3 = int(input())

        if (chose3 == 1):
            print("1. Catet  2. Altura")
            chose4 = int(input())
            if(chose4 == 1):
                costat = float(input("Catet: "))
                equilater_costat(costat)
            elif(chose4 == 2):
                altura = float(input("Altura: "))
                equilater_altura(altura)
            else:
                inputNoCorrecte()
        
        elif(chose3 == 2):
            print("1. Altura + Base   2. Catet + Base")
            chose5 = int(input())
            if(chose5 == 1):
                altura = float(input("Altura: "))
                base = float(input("Base: "))
                isosceles_altura_base(altura, base)
            elif(chose5 == 2):
                catet = float(input("Catet: "))
                base = float(input("Base: "))
                isosceles_base_catet(base, catet)
            else:
                inputNoCorrecte()
        
        elif(chose3 == 3):
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            catet_1 = float(input("Catet 1: "))
            catet_2 = float(input("Catet 2: "))
            escale(altura, catet_1, catet_2, base)

        else:
            inputNoCorrecte()
#endregion

    elif (chose2 == 4):
        print("1. Apotema  2. Radi")
        chose6 = int(input())
        if(chose6 == 1):
            apotema = float(input("Apotema: "))
            costat = float(input("Costat: "))
            num_costats = float(input("Num Costats: "))
            pentagon_apotema(num_costats, costat, apotema)
        elif(chose6 == 2):
            radi = float(input("Radi: "))
            costat = float(input("Costat: "))
            num_costats = float(input("Num Costat: "))
            pentagon_radi(num_costats, costat, radi)
        else:
            inputNoCorrecte()
    
    elif (chose2 == 5):
        print("1. Radi  2. Longitud  3. Diàmetre  4. Àrea")
        chose7 = int(input())
        if(chose7 == 1):
            radi = float(input("Radi: "))
            cercle_radi(radi)
        elif(chose7 == 2):
            longitud = float(input("Longitud: "))
            cercle_longitud(longitud)
        elif(chose7 == 3):
            diametre = float(input("Diàmetre: "))
            cercle_diametre(diametre)
        elif(chose7 == 4):
            area = float(input("Àrea: "))
            cercle_area(area)
        else:
            inputNoCorrecte()

    elif (chose2 == 6):
        diagonal_1 = float(input("Diagonal 1: "))
        diagonal_2 = float(input("Diagonal 2: "))
        rombe(diagonal_1, diagonal_2)
    
    elif (chose2 == 7):
        print("1. h + a + b ")
        print("2. a + b + c + d")
        chose8 = int(input())
        if(chose8 == 1):
            h = float(input("h: "))
            a = float(input("a: "))
            b = float(input("b: "))
            trapezi_h_a_b(h, a, b)
        elif(chose8 == 2):
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            d = float(input("d: "))
            trapezi_a_b_c_d(a, b, c, d)
        else:
            inputNoCorrecte()
    
    else:
        inputNoCorrecte()

elif (chose1 == 2):
    print("1. Cub  2. Prisme  3. Piràmide")
    print("4. Con  5. Cilindre  6. Esfera")
    
    chose9 = int(input())

    if(chose9 == 1):
        costat = float(input("Costat: "))
        cub(costat)

    elif(chose9 == 2):
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        height = float(input("Height: "))
        prisme(base, altura, height)
    
    elif(chose9 == 3):
        print("1. ap + h  2. apB + h  3. ap + apB")
        chose10 = int(input())
        if (chose10 == 1):
            ap = float(input("ap: "))
            h = float(input("h: "))
            costat = float(input("Costat: "))
            num_costat = float(input("Num Costats: "))
            piramide_ap_h(ap, h, costat, num_costat)
        elif(chose10 == 2):
            apB = float(input("apB: "))
            h = float(input("h: "))
            costat = float(input("Costat: "))
            num_costat = float(input("Num Costats: "))
            piramide_apB_h(apB, h, costat, num_costat)
        elif(chose10 == 3):
            ap = float(input("ap: "))
            apB = float(input("apB: "))
            costat = float(input("Costat: "))
            num_costat = float(input("Num Costats: "))
            piramide_apB_ap(apB, ap, costat, num_costat)
        else:
            inputNoCorrecte()
        
    elif(chose9 == 4):
        print("1. Diàmetre + altura  2. Generatriu + Altura  3. Generatriu + Diàmetre")
        print("4. Generatriu + radi  5. Radi + Altura")
        chose11 = int(input())
        if(chose11 == 1):
            diametre = float(input("Diàmetre: "))
            altura = float(input("Altura: "))
            con_diametre_altura(diametre, altura)
        elif(chose11 == 2):
            generatriu = float(input("Generatriu: "))
            altura = float(input("Altura: "))
            con_generatriu_altura(generatriu, altura)
        elif(chose11 == 3):
            diametre = float(input("Diàmetre: "))
            generatriu = float(input("Generartiu: "))
            con_generatriu_diametre(generatriu, diametre)
        elif(chose11 == 4):
            generatriu = float(input("Generatriu: "))
            radi = float(input("Radi: "))
            con_generatriu_radi(generatriu, radi)
        elif(chose11 == 5):
            radi = float(input("Radi: "))
            altura = float(input("Altura: "))
            con_radi_altura(radi, altura)
        else:
            inputNoCorrecte()

    elif(chose9 == 5):
        print("1. Altura + radi  2. Diàmetre + altura")
        chose12 = int(input())
        if(chose12 == 1):
            radi = float(input("Radi: "))
            altura = float(input("Altura: "))
            cilindre_altura_radi(altura, radi)
        elif(chose12 == 2):
            diametre = float(input("Diàmetre: "))
            altura = float(input("Altura: "))
            cilindre_diametre_altura(diametre, altura)
        else:
            inputNoCorrecte()
    
    elif(chose9 == 6):
        radi = float(input("Radi: "))
        esfera(radi)
    
    else:
        inputNoCorrecte()

else:
    inputNoCorrecte()