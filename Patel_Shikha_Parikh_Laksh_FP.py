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
    inventoryList = []
    
    #create a list with all of the contents of the file
    while id_inventory!='':
        
        #append grade to list
        name_inventory = file.readline()
        stock_inventory = int(file.readline())
        price_inventory = float(file.readline())
        new_inventory = inventory.Inventory(id_inventory,name_inventory,stock_inventory,price_inventory)
        inventoryList.append(new_inventory.get_id().rstrip('\n'))
        inventoryList.append(new_inventory.get_name().rstrip('\n'))
        inventoryList.append(new_inventory.get_stock())
        inventoryList.append(new_inventory.get_price())
        #read newline
        id_inventory = file.readline() 
    file.close()
    
    
    return inventoryList
    
    
def print_inventory(list_inventory):
    
    
    print(format("ID", "5"), format("Item", '30'), format("Price", '10'), format("Stock", '15'))
    
    for i in range(0, (len(list_inventory)), 4):
        
        print(format(list_inventory[i], '5'), format(list_inventory[i+1], '30'), "$", format(list_inventory[i+3], '5'), format(list_inventory[i+2], '11'))
    print("Enter 0 when finished")
    
    
def get_item_id (list_inventory): 
    
    value = True
    while value: 
        try: 
            item_id = input("Please input the item ID you wish to purchase/return: ")
            
            if float(item_id) == 0: 
                value = False
            
            else:
                if item_id not in list_inventory: 
                    print("Input was invalid.")
                    value = True
                else: 
                    value = False
            
            
                
        except ValueError:
            print("Input was invalid.")
            value = True
           
    
def write_updated_inventory(): 
    file = open("UpdatedInventory.txt", "w")
    print()
    
def print_invoice(): 
    #insert code 
    print()
    
    
def main():   
    
    list_inventory = process_inventory()
    print_inventory(list_inventory)
    get_item_id(list_inventory)
    
main()