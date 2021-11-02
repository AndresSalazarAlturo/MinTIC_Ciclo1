# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 21:05:37 2021

@author: Andres Salazar
"""

abc_count = 0
xyz_count = 0
    
# ABC = input("Ingresar productos compañia ABC: ")
# XYZ = input("Ingresar productos compañia XYZ: ")
# productos_dia = input("Ingresar productos vendidos en el dia: ")
    
ABC = "HPCQX"
XYZ = "JPLNU"
productos_dia = "FQUVJFXSUPYAUDGAG" 

for i in productos_dia:
    
    if i in ABC and i in XYZ:
        abc_count += 1
        xyz_count += 1
        if abc_count > xyz_count :
            print("P", end="") 
        elif xyz_count > abc_count :
            print("N", end="")
        else : 
            print("I", end="")
            
        
    elif i not in ABC and i not in XYZ:
        if abc_count > xyz_count :
            print("P", end="") 
        elif xyz_count > abc_count :
            print("N", end="")
        else : 
            print("I", end="")
            

    elif i in ABC:
        abc_count += 1
        if abc_count > xyz_count :
            print("P", end="") 
        elif xyz_count > abc_count :
            print("N", end="")
        else : 
            print("I", end="")
            

    elif i in XYZ:
        xyz_count += 1
        if abc_count > xyz_count :
            print("P", end="") 
        elif xyz_count > abc_count :
            print("N", end="")
        else : 
            print("I", end="")           


        
        
        
    