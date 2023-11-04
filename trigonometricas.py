import numpy as np
import matplotlib.pyplot as plt
def factorial(f):
    if f == 0:
        return 1
    else:
        return f * factorial(f-1)
    
def gradtorad(g):
    rad = (g * 3.1415926535897932)/180
    return rad

def cosenoty(coser):
    coser = gradtorad(coser)
    n = 6
    sumcos = 0
    for x in range(0, n+1):
        numerador = (-1)**x
        denominador = factorial(2*x)
        multi = coser ** (2*x)
        sumcos = sumcos + (numerador*multi / denominador)
    return sumcos

def senoty(sener):
    sener = gradtorad(sener)
    n = 6
    sumsen = 0
    for x in range(0, n+1):
        numerador = (-1)**x
        denominador = factorial(2*x +1)
        multi = sener ** (2*x + 1)
        sumsen = sumsen + (numerador*multi / denominador)
    return sumsen

def tangentety(tanger):
    tan = senoty(tanger)/cosenoty(tanger)
    return tan

def secantety(secanter):
    sec = 1/cosenoty(secanter)
    return sec

def cosecantety(cosecanter):
    csc = 1/senoty(cosecanter)
    return csc

print(cosenoty(60))
print(senoty(60))
print(tangentety(60))
print(secantety(60))
print(cosecantety(60))