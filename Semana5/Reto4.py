# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 20:25:53 2021

@author: Andres Salazar
"""
import json

# obras = {"t": 66, "u": 72, "d": 90, "r": 84, "j": 36, "g": 50, "s": 94, "q": 62, "f": 35}

obras1 = input("Obras: ")

obras = eval(obras1)

perdidas = input("perdidas: ").split()

# perdidas = ("d p h u i e t q").split()

perdidas_finales_keys = []
perdidas_finales_values = []

for p in perdidas: 
    # print(p)
    for k, v in obras.items():
        # print(k,' ', v,)
        if p == k:
            perdidas_finales_keys.append(k)
            perdidas_finales_values.append(v)
        else: 
            continue
        
valor_perdidas = sum(perdidas_finales_values)

# print(perdidas_finales_values)
# print(perdidas_finales_keys)
# print("-------------------------")
print(valor_perdidas)
str1 = ' '.join(map(str, perdidas_finales_keys))
print(str1)

            

