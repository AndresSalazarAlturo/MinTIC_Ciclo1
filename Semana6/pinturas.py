# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 02:07:34 2021

@author: Andres Salazar
"""
def pintores(a):
    
    res = [i for n, i in enumerate(a) if i not in a[:n]]
    # print(res)
    return res

def mefaltandeunpintor(lista,Autores,autor):
    faltan=[]
    for i in lista:
        p = Autores[i]
        if p == autor:
            pos = Autores.index(p,i)
            faltan.append(pos)
        else:
            continue
    return faltan

def meinteresan(otromuseo,mimuseo):
    notengo=[]
    for i in otromuseo:
        if i not in mimuseo:
            notengo.append(i)
        else:
            continue
    return notengo

def paracambiar(otromuseo,mimuseo):
    tengo=[]
    tiene=[]
    intercambiables = 0
    for i in otromuseo:
        if i not in mimuseo:
            tengo.append(i)
    for j in mimuseo:
        if j not in otromuseo:
            tiene.append(j)
    intercambiables = min(len(tengo), len(tiene))
    print(len(tengo))
    print(len(tiene))
    return intercambiables






