#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:12:42 2022

@author: shikhapatel
"""

#Laksh & Shikha final project
#hi
import inventory

def process_inventory(): 
    
    
    file = open("Inventory.txt", "r")
    id_inventory = file.readline()
    inventoryDict = {}
    
    #create a list with all of the contents of the file
    while id_inventory!='':
        
        #append grade to list
        name_inventory = file.readline()
        stock_inventory = int(file.readline())
        price_inventory = float(file.readline())
        new_inventory = inventory.Inventory(id_inventory,name_inventory,price_inventory, stock_inventory)
        inventoryDict.update({new_inventory.get_id().rstrip('\n'): [new_inventory.get_name().rstrip('\n'), new_inventory.get_stock(), new_inventory.get_price()]} )
        
        id_inventory = file.readline() 
    file.close()
    
    print(inventoryDict)
    return inventoryDict
    
    
def print_inventory(dict_inventory):
    
    
    print(format("ID", "5"), format("Item", '30'), format("Price", '10'), format("Stock", '15'))
    
    for i in dict_inventory:
        
        print(format(i, '5'), format(dict_inventory[i][0], '30'), "$", format(dict_inventory[i][1], '5'), format(dict_inventory[i][2], '11'))
    print("Enter 0 when finished")
    
    
def get_item_id (dict_inventory): 
    
    value = True
    while value: 
        try: 
            item_id = input("Please input the item ID you wish to purchase/return: ")
            
            if float(item_id) == 0: 
                value = False
            
            else:
                if item_id not in dict_inventory: 
                    print("Input was invalid.")
                    value = True
                else: 
                    value = False
            
            
                
        except ValueError:
            print("Input was invalid.")
            value = True
           
    return item_id


def get_quantity (list_inventory): 
    
    item_quantity = float(input("Please enter the desired quantity (negative quantity for return): "))
    return item_quantity
    #do we do validate the quanity 
    #when it says new the only new thing is the quantity rigth? 
    
def write_updated_inventory(): 
    file = open("UpdatedInventory.txt", "w")
    print()
    
def print_invoice(): 
    #insert code 
    print()
    
    
def main():   
    
    dict_inventory = process_inventory()
    print_inventory(dict_inventory)
    iduser = get_item_id(dict_inventory)
    quanityuser = get_quantity(dict_inventory)
    
    
main()