# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 10:31:34 2021

@author: Andres Salazar
"""

Data_base = []
Only_product = []
cp = 's'

while(cp == 's'):
    
    New_products = int(input("Numero de articulos a agregar: "))
    
    for j in range(New_products):
        
        P_name = input("Nombre del producto: ")
        P_cost = input("Costo del producto: ")
        P_sell_price = input("Costo de venta al publico: ")
        P_stock = input("Unidades disponibles: ")
        
        for i in (P_name, P_cost, P_sell_price, P_stock):
            Only_product.append(i)
        
        Data_base.append(Only_product)
        
        Ganancia = int(P_sell_price) - int(P_cost)
        
        print("------------------------------------------------")
        print("Productos: ")
        print("Producto: ", Data_base[j][0])
        print("CU: $", Data_base[j][1])
        print("PVP: $", Data_base[j][2])
        print("Unidades disponibles: ", Data_base[j][3])
        print("Ganancia: ", Ganancia)
        print("------------------------------------------------")
        
        Only_product = []
        
        cp = input("Desa agregar un nuevo producto? s/n: ")
        
#%%

on = 's'
Data_base = []
cakes = []
while(on == 's'):
    
    sugar = int(input("Numero de tasas azucar: "))
    flour = 2*sugar + 4
    butter = (flour + sugar)//5

    for i in (sugar, flour, butter):
        cakes.append(i)

    Data_base.append(cakes)

    if (butter <= 20):
        pack = 'uno'
    elif(butter > 20 and butter <= 30):
        pack = 'dos'
    elif(butter > 30 and butter <= 50):
        pack = 'tres'
    else:
        pack = 'cuatro'
        
print(sugar, flour, butter)
print(pack)
    
print("Con " + str(sugar) + "  tasas de azucar se necesitan " + str(flour) + " de harina y " + str(butter) 
        + " de mantequilla y es de empaquetado " + pack + ".")

cakes = []

on = input("Desea agregar una nueva torta? s/n ")
    












        
    
    
    