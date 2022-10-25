#aquest programa calcula l'àrea i perímetre d'un triangle Isòsceles -- a partir de la base i un dels seus catets

import math

base = float(input("Base: "))
catet = float(input("Catet: "))

altura = math.sqrt(catet**2 - (base/2)**2)

area = base * altura / 2
perimetre = catet * 2 + base

print("Perímetre: " + str(perimetre))
print("Àrea: " + str(area))


'''
Formulas:
A = base * altura / 2
P = costat * 2 + base

Disposo:
- base
- catets

Què necessito?
- altura = math.sqrt(catet**2 - (base/2)**2)

print(perimetre)
print(area)



'''